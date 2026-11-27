# Independent Living — Project Context

## Project goal

Design a human-centered service that helps people over 70 live independently at home with appropriate safety and support, without making them feel monitored or reducing their autonomy.

Guiding question: **How might we help a person over 70 live independently at home without making them feel controlled?**

The project is part of the Smart Home & Connected Living AI-Augmented Design Challenge. The service is for older adults and the people they choose to involve in their support. The Research Ops Agent is an internal tool for the UX design team; it is not the product intended for older adults or caregivers.

## Source material and limitations

- Figma, page **01. Brainstorming Azzurra**, node `9:3`: [Independent Living — Eng](https://www.figma.com/design/XPH6H7C0SX9qvFE0pZPRye/Independent-Living----Eng?node-id=9-3).
- `Independent_Living_Research_Kit.docx`: project brief, initial simulated research kit, memory structure, metrics, and agent prompt.
- `Team3.pdf` (4 image-only slides, reviewed 2026-11-24 by rendering the pages): Brief 3/6 of the AI-Augmented Design Challenge, client brief Bticino / Riello. Ask the designer to resolve any discrepancy between it and the DOCX or Figma page.

## Client brief (from `Team3.pdf`)

- **Scenario:** a home-systems company wants to enter Smart Home & Connected Living with services that help people over 70 live autonomously at home, supporting autonomy and safety without creating a perception of control.
- **Challenge:** design an experience already projected to an agentic model, in which AI agents support independent living without replacing the person's choices.
- **Constraint:** during the project the client requires an **optional** mode for involving caregivers.
- **Possible design areas:** smart home, behavioral monitoring, communication with caregivers, wellbeing and prevention, support for daily activities.
- **Asset to build:** the Research Ops Agent, which prepares the research protocol, synthesizes interviews and tests, and keeps the needs map of older adults and caregivers up to date. It may integrate with GitHub Copilot, Eng Code, or Figma, and may start from Open Claw or GitHub agent libraries.
- **Measures:** time from protocol to synthesis, insights traceable to the source, and human revisions needed.
- **Designer's role:** checks syntheses against sources and decides what is truly an insight, starting from the theme of perceived control.
- **Reference:** Università di Bologna, a broader user-research method to guide questions, listening, and choices.

## People and needs to consider

- **People over 70**, especially those living alone or mostly alone. Their abilities, routines, technology familiarity, accessibility needs, and preferences vary; do not treat them as one persona.
- **Caregivers**, including relatives and professional caregivers. They may need reassurance and coordination, but involvement and access to information must be chosen by the older adult.

Initial design tensions to explore, not assume as universal truths:

- Independence and control versus safety and timely help.
- Reassurance for caregivers versus continuous monitoring.
- Useful automation versus opaque or unwanted decisions.
- Accessible support versus stigmatizing or burdensome devices.
- Coordinating care versus fragmented communications and false alarms.

## Non-negotiable principles

1. The older adult is the decision-maker about their home, support, and data.
2. Caregivers support; they do not have an automatic right to monitor.
3. Sharing is optional, specific, understandable, and revocable. Default to no sharing unless the person explicitly enables it.
4. Any emergency procedure or escalation path must be agreed in advance. A safety concern is not blanket permission for surveillance.
5. Prefer proportionate, low-intrusion support. Do not propose invasive cameras or continuous data feeds as a default.
6. Make automated actions explainable and easy to disable; do not let an agent make consequential decisions on a person's behalf.
7. Respect dignity and identity. Avoid paternalistic language and stigmatizing framing such as assuming that a wearable or device is appropriate because of age.
8. Design for varied vision, hearing, dexterity, and digital confidence. Do not make a screen, small buttons, or fast speech the only way to use an essential feature.
9. Minimize personal data. Obtain informed consent before collecting or sharing interview material; protect or de-identify personal information.

## Product direction from the design exploration

Do not start by assuming that the solution is a sensor or another monitoring device. Explore the complete service and the relationship between the older adult and caregivers.

The Figma page describes two experience directions: one for the older adult and one for the caregiver. These are visual references, not validated or final wireframes. A promising direction is to provide ambient, unobtrusive support (for example, pathway lighting at night), transparent controls, and concise, consent-based reassurance rather than a stream of activity data.

Example of proportionate agentic behavior: if a routine appears different, check only appropriate non-invasive signals, ask the person whether they need help, wait for a response, and contact a caregiver only when necessary and within permissions agreed beforehand. Do not automatically turn an anomaly into a caregiver alert.

## Research Ops Agent purpose and workflow

The agent helps the UX team prepare and organize research, analyze source material, and maintain reusable research outputs. It supports, but does not replace, real interviews, designer judgment, or participant consent.

Use this cycle:

**ASCOLTA → RACCOGLI → SINTETIZZA → AGGIORNA → VALIDA → RIGENERA**

1. **Ascolta:** use gaps and open questions in `research-memory.md` to prepare a research protocol.
2. **Raccogli:** support real interviews, tests, observations, and notes. Keep older-adult and caregiver protocols appropriately distinct.
3. **Sintetizza:** separate observation, interpretation, and hypothesis; connect each item to its source.
4. **Aggiorna:** propose updates to the needs map, personas, journey, user stories, and research memory.
5. **Valida:** the designer confirms, rejects, or reframes proposed insights. Only then may an insight be marked validated.
6. **Rigenera:** turn unresolved questions, contradictions, and designer corrections into the next cycle's inputs and rules.

### Agent modules

- **Research protocol:** objectives, hypotheses, recruitment, method and rationale, open non-leading questions, privacy/accessibility notes, consent, and a note-taking template.
- **Simulated interviews:** only on explicit request and when real participants are unavailable. Label every output `Simulato – da validare`; assign `Pxx` to older adults and `Cxx` to caregivers.
- **Synthesis:** for each source, distinguish `OSSERVAZIONE`, `INTERPRETAZIONE`, and `IPOTESI DI INSIGHT`; cite `[ID – profile – line]`; surface emotions, workarounds, friction, differences, and contradictions without overgeneralizing.
- **Personas:** create or update only from evidence in the memory. Record profile, goals, needs, barriers, support required, sources, and status (`Proto-persona` or `Validata`).
- **User journey:** describe moments, actions, emotions, and agent opportunities for the older adult-caregiver relationship.
- **User stories:** use `Come [persona] voglio [azione] così da [beneficio]`, add an acceptance criterion and sources, and check that the story preserves the older adult's autonomy.
- **Needs map:** `Bisogno | Attore | Ambito | Evidenze | Confidenza | Impatto sul controllo percepito | Stato | Ciclo`.

## Evidence and status rules

- Treat `research-memory.md` as the persistent project state. Read it in full at the start of each task; do not restart from zero.
- Every new source or research output must identify its source and cycle.
- Keep observations, interpretations, hypotheses, and designer-validated insights separate.
- The initial interviews and personas in the Research Kit are **simulated proto-personas**, not real user research. Preserve that label whenever referring to them.
- Do not invent participants, quotes, findings, dates, source lines, or confidence. Do not present an individual experience as representative.
- If support is missing, write **“dato non presente nelle fonti”** and turn the gap into an open research question.
- New insights remain `Ipotesi` until the designer confirms them. Record rejected or reframed insights and the designer's lesson for future cycles.
- Do not infer consent, preferences, diagnoses, or needs from age, caregiver reports, or a simulated persona.

## Initial research state

The Research Kit contains six semistructured simulated interviews: three older adults (`P01`–`P03`) and three caregivers (`C01`–`C03`). It also contains proto-personas, a user journey for Anna and Marco, 12 draft user stories, an initial needs map, three hypotheses, and open questions. Their details and status are recorded in `research-memory.md`.

The initial needs and insight statements are hypotheses from simulated material. They are useful for planning validation, not for claiming that a user need has been established.

## Open questions for future cycles

- What signals, if any, is each older adult willing to share, with whom, and under what conditions?
- Where does each person draw the line between help and control in everyday routines?
- What escalation is acceptable in a critical event, and how should it be agreed in advance?
- Do the simulated personas and hypotheses match real participants?

## Evaluation metrics

Track actual values; never invent improvement percentages:

- Time from protocol to designer-validated synthesis.
- Percentage of insights traceable to a source ID.
- Number of human corrections per cycle.
- Number of open questions closed relative to the previous cycle.

## Relationship between project files

- `context.md` is the stable project brief and rules.
- `research-memory.md` is the evolving, evidence-linked record for each research cycle.
- `.github/agents/research-ops-agent.agent.md` defines the Copilot agent. It must read both files before working and follow their evidence, consent, and validation rules.
