# Das Profil

**Status:** Normativer Entwurf

Timo am 18.09.2026: *"Wenn ich jetzt sage, ich will so eine Karte haben, wo alles draufsteht, was eine Stiftung macht. Wo ein Projekt sich komplett vorstellen kann. Das müssen wir dann auch definieren. Was es dafür alles braucht."*

---

## Was ein Profil ist

**Das Profil einer Einrichtung ist ihr Space.** Die Angaben stehen in `Group.data`, nach den Vokabularen ihrer Art. Ein zweites Profil-Item daneben wäre eine zweite Wahrheit (`DEFINITION.md` Teil 9).

**Das Profil eines Menschen ist ein Item.** Das regelt Antons [Spec 12](https://github.com/real-life-org/real-life-stack): ein `person`-Item im persönlichen Space, mit Spiegeln in die Gruppen, für die er es freigibt.

Beide werden von **demselben Feld-Register** dargestellt, damit sie sich gleich anfühlen.

---

## Die sechs Abschnitte

Ein Projekt, das eine Stiftung ansieht, stellt sechs Fragen in dieser Reihenfolge. Die Abschnitte antworten darauf.

### 1. Wer ist das

| Feld | Form |
|---|---|
| `name` | Text |
| `foerdererart` | Auswahl: Stiftung, Kommune, Land, Bund, EU, Lotterie, Kirche, Wohlfahrt, Verband, Kammer, Unternehmen |
| `art` | Auswahl: fördernd, operativ, beides |
| `sitz` | Text: Stadt, Bundesland, Land |
| `position` | Ort für die Karte |
| `website` | URL |

### 2. Was gefördert wird

| Feld | Form |
|---|---|
| `zweck` | Text, eigene Zusammenfassung |
| `foerderbereiche` | Tags aus dem gemeinsamen Vokabular |
| `zielgruppen` | Tags |
| `reichweite` | Tags: lokal, regional, national, international |
| `hinweis` | Text: „Woran erkennt ein Projekt, dass es zu uns passt", in ihren Worten |
| `bisherGefoerdert` | Tags: Themen, keine kopierten Projektbeschreibungen |

**`hinweis` ist das wertvollste Feld der ganzen Karte.** Es steht nirgends sonst, und es beantwortet die Frage, die jedes Projekt wirklich hat.

### 3. Wie viel

| Feld | Form |
|---|---|
| `summeVon`, `summeBis` | Zahl |
| `volumenJahr` | Zahl, wenn öffentlich bekannt |
| `eigenmittel` | ja, nein, teilweise |

### 4. Wie beantragt wird

| Feld | Form |
|---|---|
| `antragstellung` | ja, nein, offen |
| `antragsweg` | offen, Wettbewerb, Anfrage, eingeladen, operativ, Kooperation, Träger-Partnerschaft, Boden |
| `fristen` | laufend, Stichtag, Fenster |
| `unterlagen` | Liste |
| `antragsportal` | URL |

### 5. Wie man Kontakt aufnimmt

| Feld | Form |
|---|---|
| `ansprache` | Text: **Funktion statt Name**, solange kein Profil übernommen ist |
| `mail` | Mailadresse |

### 6. Was man geben kann

| Feld | Form |
|---|---|
| `spende`, `zustiftung`, `treuhand` | ja, nein |

---

## Die Regeln

1. **Ein leeres Feld erscheint nicht.** Feld-Präsenz statt Typ-Verzweigung (Antons Muster 4). Eine Karte mit zwanzig Strichen wirkt leerer als eine mit sechs Angaben.
2. **Ein leerer Abschnitt erscheint nicht.** Dieselbe Regel eine Ebene höher.
3. **Die Karte kennt keine Reihenfolge nach Wichtigkeit einzelner Felder.** Die Abschnitte stehen fest, innerhalb eines Abschnitts steht, was da ist.
4. **Was andere über die Einrichtung sagen, steht daneben, nie darin.** Bestätigungen und Relationen sind eine eigene Ebene (`DEFINITION.md` Teil 9, Regel 4).
5. **Ein recherchierter Eintrag trägt seine Quelle.** Solange niemand ihn übernommen hat, steht auf der Karte, woher die Angaben stammen.
6. **Kein Feld wird erfunden, um die Karte zu füllen.** Was fehlt, fehlt sichtbar.

---

## Ein Projekt stellt sich vor

Dieselben sechs Abschnitte, andere Fragen:

| Abschnitt | Felder |
|---|---|
| **Wer** | `name`, `kurz`, `position`, `region`, `anstifter`, `gruppe` |
| **Warum** | `beduerfnis` (was fehlt hier ohne dieses Projekt), `themen`, `zielgruppen` |
| **Was es kostet** | `bedarfe` (mit Art: Hände, Wissen, Sachen, Raum), `bedarfGesamt`, `eigenmittel`, `luecke` |
| **Was schon steht** | `vorhandenes`, `foerderer`, `zustifter` |
| **Wann** | `zeitraum`, `termine`, `schritte` |
| **Was sich ändert** | `wirkung`: zwei bis drei nachprüfbare Dinge |

**`beduerfnis` trägt den Rest.** Es beschreibt eine Lücke, kein Projekt: *„Vierzig Bäche bleiben unbetreut"* zieht, *„wir sind ein Verein für Umweltbildung"* nicht.

---

## Wo das Profil erscheint

| Ort | Form |
|---|---|
| **In der App** | als Fläche im Space, über das Modul `profil` |
| **Auf der Karte** | als Vorschau beim Klick auf die Nadel |
| **Als eigene Seite** | die Landingpage einer Stiftung, aus denselben Feldern |
| **In der Liste** | als Zeile mit Name, Art, Sitz und der einen entscheidenden Angabe |

**Alle vier lesen dieselben Felder.** Wer eine Angabe ändert, ändert sie überall.

---

## Was es zum Bauen braucht

| Schicht | Was |
|---|---|
| Felder | stehen: `baukasten/felder/felder.json`, 26 für Förderer, 21 für Projekt |
| Muster | stehen: Profilkopf, Projektvorstellung, Kontaktblock, Förderaufruf |
| Bauteile | stehen: Eingabefeld, Avatar, Kartennadel, Vertrauens-Anzeiger |
| **Modul `profil`** | **fehlt.** Die Fläche, die alles zusammensetzt |
| **Skill `/td-profil`** | **fehlt.** Der Generator, der aus einer Beschreibung ein Profil baut |

---

## Verwandt

- [03-datenmodell.md](03-datenmodell.md) — die Felder im Einzelnen
- [12-baukasten.md](12-baukasten.md) — woraus gebaut wird
- `DEFINITION.md` Teil 6, 7 und 9 im Stack-Repo — Arten, Feld-Register, Profile
