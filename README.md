# Independent Living

## Controllo delle citazioni

Con Python 3, senza dipendenze esterne:

```text
python tools/check_citations.py percorso\output.md percorso\fonti
```

Le fonti sono file UTF-8 chiamati `ID.md` nella cartella indicata. I riferimenti usano `[ID – profilo – riga] «estratto letterale»`: la riga è fisica, numerata da 1, e l'estratto immediatamente successivo contiene al massimo 15 parole. Il controllo cerca l'estratto nella riga indicata o in quella immediatamente precedente o successiva. I riferimenti a una sezione invece di una riga sono classificati come non verificabili; una fonte mancante o illeggibile è anch'essa non verificabile.

Ogni insight prioritario inizia con `### INSIGHT I01`, con ID univoco; le sue citazioni devono comparire prima del titolo successivo di livello 1–3. Ogni candidato non prioritario è su una riga `- **CANDIDATO I06**: ...`, con ID univoco e citazioni sulla stessa riga. La percentuale è il numero di insight e candidati con almeno una citazione e tutte le citazioni valide, diviso il totale degli insight e candidati dichiarati. Un insight senza citazioni non è tracciabile; senza insight e candidati la percentuale non è calcolabile.

Il report distingue citazioni valide, non valide e non verificabili. Il comando restituisce 0 se tutti i riferimenti e gli insight dichiarati superano il controllo, 1 se sono presenti citazioni non valide o non verificabili oppure insight senza citazioni, e 2 per errori negli input. Il controllo è testuale: il designer deve comunque verificare la fedeltà della parafrasi, il profilo e il significato dell'insight.
