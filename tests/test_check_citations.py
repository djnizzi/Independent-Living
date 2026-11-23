import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "tools" / "check_citations.py"
SOURCES = ROOT / "tests"


class CitationCheckerTests(unittest.TestCase):
    def run_checker(self, output):
        with tempfile.TemporaryDirectory() as directory:
            output_file = Path(directory) / "output.md"
            output_file.write_text(output, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(CHECKER), str(output_file), str(SOURCES)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                env={**os.environ, "PYTHONIOENCODING": "utf-8"},
                check=False,
            )

    def test_valid_line_and_adjacent_line(self):
        result = self.run_checker(
            "### INSIGHT I01\n"
            "[T2 – caregiver – 2] «Vorrei vedere ogni attività.»\n"
            "[T2 – persona anziana – 2] «Non voglio condividere le mie attività.»\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Citazioni valida: 2", result.stdout)
        self.assertIn("Insight tracciabili: 1/1 (100.0%)", result.stdout)

    def test_invalid_line_and_excerpt(self):
        result = self.run_checker(
            "### INSIGHT I01\n"
            "[T2 – caregiver – 99] «Vorrei vedere ogni attività.»\n"
            "[T1 – persona anziana – 2] «Questo testo non esiste.»\n"
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Citazioni non valida: 2", result.stdout)
        self.assertIn("Insight tracciabili: 0/1 (0.0%)", result.stdout)

    def test_missing_source_and_section_are_unverifiable(self):
        result = self.run_checker(
            "### INSIGHT I01\n"
            "[ASSENTE – persona – 1] «estratto»\n"
            "[T1 – persona – sezione 1] «Poi apro la finestra.»\n"
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Citazioni non verificabile: 2", result.stdout)
        self.assertIn("Insight tracciabili: 0/1 (0.0%)", result.stdout)

    def test_missing_and_overlong_excerpts(self):
        long_excerpt = " ".join(["parola"] * 16)
        result = self.run_checker(
            "### INSIGHT I01\n"
            "[T1 – persona – 2]\n"
            f"[T1 – persona – 2] «{long_excerpt}»\n"
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Citazioni non valida: 2", result.stdout)

    def test_uncited_insight_counts_in_denominator(self):
        result = self.run_checker(
            "### INSIGHT I01\n"
            "[T2 – caregiver – 2] «Vorrei vedere ogni attività.»\n"
            "### INSIGHT I02\nNessuna fonte.\n"
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Insight tracciabili: 1/2 (50.0%)", result.stdout)
        self.assertIn("I02: nessuna citazione riconosciuta", result.stdout)

    def test_no_insights_has_no_percentage(self):
        result = self.run_checker("Nessun insight.\n")
        self.assertEqual(result.returncode, 0)
        self.assertIn("non calcolabile", result.stdout)

    def test_duplicate_insight_is_an_input_error(self):
        result = self.run_checker("### INSIGHT I01\n### INSIGHT I01\n")
        self.assertEqual(result.returncode, 2)
        self.assertIn("ID insight duplicato", result.stderr)

    def test_candidate_counts_and_does_not_absorb_later_citations(self):
        result = self.run_checker(
            "### INSIGHT I01\n"
            "[T2 – caregiver – 2] «Vorrei vedere ogni attività.»\n"
            "## Candidati non prioritari\n"
            "- **CANDIDATO I02**: Nessuna citazione.\n"
            "[T2 – caregiver – 2] «Vorrei vedere ogni attività.»\n"
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Insight tracciabili: 1/2 (50.0%)", result.stdout)
        self.assertIn("I02: nessuna citazione riconosciuta", result.stdout)

    def test_zero_line_is_invalid(self):
        result = self.run_checker(
            "### INSIGHT I01\n[T1 – persona – 0] «Poi apro la finestra.»\n"
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Citazioni non valida: 1", result.stdout)


if __name__ == "__main__":
    unittest.main()
