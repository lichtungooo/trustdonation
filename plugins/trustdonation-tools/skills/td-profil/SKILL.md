---
name: td-profil
description: "Ein Profil fuer eine Stiftung oder ein Projekt bauen. Fuehrt durch die Fragen, schreibt die Felder nach docs/13-profil.md, waehlt die Bausteine aus Antons Vorlage. Fuer recherchierte Eintraege und fuer uebernommene Spaces."
---

# Ein Profil bauen

Timo am 20.09.2026: *"Ich würde echt gerne einen richtig guten Profilskill bauen, damit wir für die Projekte und auch für die Stiftungen saubere Profile haben, wo wirklich alles schön strukturiert ausgefüllt ist."*

**Der wichtigste Satz vorweg:** Ein Profil wird **gefragt, nicht erfunden**. Jedes Feld hat eine Frage, und wo die Antwort fehlt, bleibt das Feld leer. Eine Karte mit zwanzig Strichen wirkt leerer als eine mit vier Angaben.

---

## 1. Was ein Profil ist

| | |
|---|---|
| **Eine Einrichtung** | Ihr Profil **ist ihr Space**. Die Angaben stehen in `Group.data` |
| **Ein Mensch** | Sein Profil ist ein `person`-Item. Das regelt Antons Spec 12 |
| **Ein recherchierter Eintrag** | Ein `place`-Item mit Position, Namen und dem, was öffentlich bekannt ist |

Die Definition steht in `docs/13-profil.md` (Instanz-Repo) und `DEFINITION.md` Teil 9 (Stack).

---

## 2. Die Fragen stellen

**Für eine Stiftung:** `docs/fragen/stiftung.md`, dreizehn W-Fragen.
**Für ein Projekt:** `docs/fragen/projekt.md`, vierzehn Fragen in drei Runden.

Beide Bögen sind gelöst nachzulesen: `fragen/beispiel-stiftung.md` und `fragen/beispiel-projekt.md`.

### Die Reihenfolge, die trägt

Ein Profil wird in der Reihenfolge gefüllt, in der ein Besucher liest:

| Abschnitt | Die Frage | Felder |
|---|---|---|
| **Wer ist das** | Mit wem habe ich es zu tun? | `foerdererart`, `art`, `sitz`, `website` |
| **Was gefördert wird** | Passt mein Vorhaben dazu? | `zweck`, `foerderbereiche`, `zielgruppen`, `reichweite`, `hinweis`, `bisherGefoerdert` |
| **Wie viel** | Reicht das für mein Vorhaben? | `summeVon`, `summeBis`, `volumenJahr`, `eigenmittel` |
| **Wie beantragt wird** | Was muss ich tun? | `antragstellung`, `antragsweg`, `fristen`, `unterlagen`, `antragsportal` |
| **Wie man Kontakt aufnimmt** | An wen wende ich mich? | `ansprache`, `mail` |
| **Was man geben kann** | Und wenn ich etwas beitragen will? | `zustiftung`, `spende`, `treuhand` |

Ein Projekt stellt dieselben sechs Fragen mit anderen Feldern. Der Bauplan steht in `packages/td-core/src/profil.ts` als `BAUPLAN_PROJEKT`.

### Die zwei Felder, die alles tragen

**Bei einer Stiftung: `hinweis`.** *„Woran erkennt ein Projekt, dass es zu uns passt"*, in ihren Worten. Es steht nirgends sonst und beantwortet die Frage, die jedes Projekt wirklich hat.

**Bei einem Projekt: `beduerfnis`.** Es beschreibt eine **Lücke, kein Projekt**: *„Vierzig Bäche bleiben unbetreut"* zieht, *„wir sind ein Verein für Umweltbildung"* nicht.

Wenn eines der beiden fehlt, ist das Profil nicht fertig, gleich wie voll der Rest ist.

---

## 3. Die Felder schreiben

Jedes Feld kennt seine Form. Sie steht in `baukasten/felder/felder.json` und entscheidet, wie es dargestellt wird.

| Form | Wofür | Beispiel |
|---|---|---|
| `text` | eine Zeile | `sitz: "Kassel, Hessen"` |
| `longtext` | ein Absatz | `zweck`, `hinweis`, `beduerfnis` |
| `tags` | mehrere Schlagworte | `foerderbereiche: ["Jugend", "Handwerk"]` |
| `select` | eine Auswahl | `antragsweg: "offen"` |
| `money` | Euro | `summeVon: 2000` |
| `bool` | ja oder nein | `zustiftung: true` |
| `list` | eine Aufzählung | `unterlagen: ["Skizze", "Finanzplan"]` |
| `url`, `email` | eine Adresse | `website`, `mail` |
| `position` | ein Ort | `{ lat, lng }` |

### Fünf Regeln beim Schreiben

1. **Was fehlt, bleibt leer.** Kein Platzhalter, kein „unbekannt", kein Strich. `profilAbschnitte` lässt leere Felder und leere Abschnitte weg.
2. **`false` ist eine Antwort.** „Treuhandstiftung: nein" gehört auf die Karte, denn es erspart jemandem eine Anfrage. Es steht als `false`, nicht als leeres Feld.
3. **Eigene Worte, kein Zitat.** `zweck` ist eine Zusammenfassung, keine kopierte Satzung. Siehe `docs/04-recht.md`.
4. **Eine Funktion statt eines Namens**, solange kein Profil übernommen ist. Wer aus einem Impressum abschreibt, veröffentlicht die Daten eines Menschen, der nie gefragt wurde.
5. **Die Quelle mitschreiben.** Solange niemand den Eintrag übernommen hat, trägt `quelle`, woher die Angaben stammen.

---

## 4. Die Bausteine wählen

**Antons Vorlage liegt in `apps/prototype/src/components/profile/`.** Sie führt vierzehn Bausteine und wählt sie nach demselben Prinzip wie wir: Was keine Daten hat, erscheint nicht.

| Baustein | Wann er erscheint |
|---|---|
| Über (Text) | es gibt `zweck` oder `beduerfnis` |
| Galerie | es gibt Bilder |
| Karte | es gibt `position` |
| Kontakt | es gibt `mail` oder `ansprache` |
| Mitglieder | der Space hat mehr als ein Mitglied |
| Projekte | die Einrichtung trägt Relationen auf Projekte |
| Funding | ein Projekt trägt `bedarfGesamt` und `luecke` |
| Events | es gibt Termine |
| Badges, Quests | im Real Life Network, hier noch ungenutzt |

**Die Muster für die Darstellung** stehen im Baukasten: Profilkopf, Projektvorstellung, Kontaktblock, Förderaufruf. Jedes trägt seine Absicht, und die entscheidet, ob eine Änderung erlaubt ist.

---

## 5. Das Aussehen

**Die Design-Doktrin gilt** (`memory/feedback_design_doktrin.md`, seit 12.05.2026):

| Was raus muss | Was rein kommt |
|---|---|
| `border` auf Containern | Farbfläche `bg-<farbe>-50/60` |
| `border-t` als Trennstrich | Atemraum durch Padding |
| `bg-card` als Widget-Schale | `rounded-2xl` ohne Rahmen |
| Counter-Footer | nichts |

Die Farben je Abschnitt stehen in `packages/td-ui/src/profil-flaeche.tsx` als `FLAECHEN`: wer (bernstein), was (grün), wie viel (orange), Antrag (blau), Kontakt (violett), Geben (smaragd).

**Immer `/60`**, damit ein Verlauf dahinter durchscheint.

---

## 6. Der Ablauf

### Für einen recherchierten Eintrag

1. Die Angaben aus öffentlichen Quellen sammeln, jede mit ihrer Herkunft
2. Die Felder nach dem Bauplan schreiben, leere leer lassen
3. `quelle` setzen
4. Als `place`-Item anlegen, mit `data.color` in der Farbe seiner Art
5. Den Eintrag prüfen: Trägt er `hinweis`? Ohne ihn fehlt das Wertvollste

### Für einen übernommenen Space

1. Die Fragen aus `docs/fragen/` mit der Einrichtung durchgehen
2. Die Felder in `Group.data` schreiben
3. Das Modul `profil` in `Group.data.modules` aufnehmen
4. `quelle` entfernen: Ab jetzt sagt die Einrichtung selbst, was gilt
5. Sie zum Admin ihres Space machen

### Prüfen

```bash
cd packages/td-core && npx vitest run tests/profil.test.ts
python td-tools/pruefen.py
```

Der erste Lauf prüft die Regeln (leere Felder, leere Abschnitte, `false` als Antwort). Der zweite fährt alle acht Tore.

---

## 7. Was ein Profil niemals trägt

- **Keine Bewertung.** Kein Stern, kein Balken, keine Note. Grundsatz 1 und 2
- **Keine erfundene Angabe**, um die Karte zu füllen
- **Keinen kopierten Text** aus einer fremden Satzung
- **Keinen Namen eines Menschen**, der nie gefragt wurde
- **Keine Zahl, die man erhöhen kann.** Der Stand („22 von 24 Angaben") ist eine Auskunft für den, der pflegt, keine Note für den, der liest

---

## Verwandt

- `docs/13-profil.md` — die Definition, sechs Abschnitte, alle Regeln
- `docs/03-datenmodell.md` — die Felder im Einzelnen
- `docs/fragen/` — die Bögen, zwei davon gelöst
- `baukasten/` — Felder, Muster, Bauteile
- Skill `/td-definieren` — bevor ein neues Feld entsteht
- Skill `/td-test` — was geprüft wird
