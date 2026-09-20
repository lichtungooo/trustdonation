# Das Profil

**Status:** Normativer Entwurf · Dritte Fassung, 20.09.2026

Timo am 18.09.2026: *"Ich will so eine Karte haben, wo alles draufsteht, was eine Stiftung macht."*

Nach zwei Fehlversuchen am 20.09.2026: *"Guck dir mal richtig gute Profile an, wie die sein müssen. Es geht ja nicht darum, eine Stiftung darzustellen und dann ein spezielles Profil daraus zu bauen, sondern wie allgemein Profile sind, wie sie sich erklären. Du kannst Facebook, Insta, alles Mögliche anschauen."*

---

## Was zweimal schiefging

**Erste Fassung:** sechs Abschnitte untereinander, jeder mit seiner Frage als Untertitel. Ein Fragebogen mit Farbe darauf.

**Zweite Fassung:** Hero, Kennzahlen, Reiter. Besser gegliedert, und trotzdem ein Datenblatt: Beschriftung links, Wert rechts, bis nach unten.

**Der gemeinsame Fehler:** Beide zeigten *Angaben über* eine Einrichtung. Ein Profil zeigt **einen Akteur mit Gesicht, Stimme, Zahlen und Werk**.

---

## Die Anatomie, nachgesehen bei echten Profilen

Instagram, LinkedIn, GitHub und Facebook bauen ihre Profile gleich. Acht Teile in dieser Reihenfolge:

| Teil | Instagram | GitHub (Organisation) | Bei uns |
|---|---|---|---|
| **Cover** | — | — | Band in der Hausfarbe |
| **Bild** | rund, überlappend | Avatar links | Logo, überlappt das Band |
| **Name** | Name + Handle | Name + verifiziert | Name |
| **Einordnung** | Kategorie | Standort, Website | Art · fördernd · Sitz · Reichweite |
| **Bio** | 150 Zeichen | Beschreibung | der Zweck, in eigener Stimme |
| **Aktionen** | Folgen · Nachricht | Follow · Sponsor | Website · Antrag · Schreiben |
| **Zahlen** | Beiträge · Follower · Gefolgt | Follower · Repos | Förderung · Bereiche · Vorhaben |
| **Themen** | Story-Highlights (runde Kacheln) | Topics | Förderbereiche als runde Kacheln |
| **Reiter** | Beiträge · Reels · Markiert | Overview · Repos · People | Gefördert · Antrag · Geben |
| **Werk** | Bild-Raster | Repository-Karten | geförderte Vorhaben als Karten |

### Das Werk ist das Herz

**Ein GitHub-Profil ohne Repositories wäre sinnlos.** Ein Instagram-Profil ohne Raster auch. Der Hauptteil jedes Profils ist das, was jemand **getan** hat, nicht was über ihn ausgefüllt wurde.

Bei einer Stiftung ist das Werk, was sie gefördert hat (`bisherGefoerdert`). Bei einem Projekt, was sich dadurch ändert (`wirkung`).

Die ersten zwei Fassungen versteckten das Werk als Stichwort-Chips in einer Zeile. Jetzt steht es als Karten-Raster im ersten Reiter.

### Zahlen werden gezählt, nicht nur abgelesen

*"1.234 Beiträge"* bei Instagram ist gezählt, nicht eingegeben. Eine gezählte Zahl ist **immer wahr und immer aktuell**, und sie füllt die Leiste auch bei einem Eintrag, der sonst wenig trägt.

| Zahl | Woher |
|---|---|
| Förderung | `summeVon` bis `summeBis`, angegeben |
| Förderbereiche | gezählt aus `foerderbereiche` |
| Vorhaben gefördert | gezählt aus `bisherGefoerdert` |

Eine Zahl ohne Grundlage fehlt. Höchstens drei: Vier Zahlen nebeneinander sind keine Signale mehr, sondern eine Tabelle.

### Themen als runde Kacheln

Instagram nennt sie Story-Highlights und stellt sie direkt unter die Bio: runde Kreise mit einem Wort darunter. Sie sagen in einer Zeile, worum es geht, und sie sehen lebendig aus, wo eine Chip-Reihe nur Text ist.

### Eine Aktion steht immer hervorgehoben

Instagram hebt *Folgen* hervor, GitHub *Sponsor*. Ein Profil, dessen Aktionen alle gleich aussehen, sagt nicht, was man als Nächstes tut. Fehlt die vorgesehene starke Aktion, rückt die erste vorhandene nach.

---

## Die Fragen sind das Raster, nicht die Oberfläche

Jeder Reiter trägt im Bauplan seine Frage. Sie sagt, welche Felder hineingehören. **Auf den Bildschirm kommt sie nie.** Wer sie anzeigt, macht aus einem Profil einen Fragebogen.

| Reiter (Förderer) | Die Frage dahinter | Was darin steht |
|---|---|---|
| **Gefördert** | Was habt ihr bisher getan? | das Werk als Karten, `zielgruppen` |
| **Antrag** | Was muss ich tun, und an wen wende ich mich? | `antragstellung`, `antragsweg`, `fristen`, `unterlagen`, `eigenmittel`, `ansprache` |
| **Geben** | Und wenn ich etwas beitragen will? | `zustiftung`, `spende`, `treuhand`, `volumenJahr` |

| Reiter (Projekt) | Die Frage dahinter |
|---|---|
| **Vorhaben** | Was soll geschehen, und was ändert sich dadurch? |
| **Mittel** | Wie weit ist es, und was fehlt? |
| **Beteiligte** | Wer steht dahinter? |

---

## Der Satz, der zieht

**Bei einer Stiftung: `hinweis`.** *"Woran erkennt ein Projekt, dass es zu uns passt"*, in ihren Worten. Er steht nirgends sonst und bekommt darum eine eigene Farbfläche mit einem Balken in der Hausfarbe.

**Bei einem Projekt: `beduerfnis`.** Es beschreibt eine **Lücke, kein Projekt**: *"Vierzig Bäche bleiben unbetreut"* zieht, *"wir sind ein Verein für Umweltbildung"* nicht.

---

## Wo ein Profil erscheint

| Was | Wo es steht |
|---|---|
| Profil eines Menschen | Panel rechts, über das Nutzermenü (Antons Spec 12) |
| Profil eines Space | Panel rechts, über die Taste in der Kopfzeile (`?profil={spaceId}`) |
| Profil eines recherchierten Eintrags | in seinem Item-Detail, an der Stelle der Meta-Box |

**Ohne Namen kein Cover.** Im Item-Detail trägt die Ansicht den Titel schon; die Fläche beginnt dann bei der Einordnungszeile.

**Die Felder messen ihren Kasten.** Container-Anfragen statt Fensterbreite: Eng steht die Beschriftung über dem Wert, breit daneben. Dieselbe Fläche passt in ein Panel von 480 Pixeln und auf eine Seite von 768.

---

## Wer ein Profil trägt

**Wer keinen Bauplan hat, hat kein Profil.** Die Regel steht in `bauplanFuer` und `traegtProfil`.

| Wer | Woran erkannt | Bauplan |
|---|---|---|
| Ein Space mit Art | `kind: "stiftung"` oder `"projekt"` | Förderer, Projekt |
| Ein recherchierter Eintrag | `foerdererart` trägt eine Angabe | Förderer |
| Ein Vorhaben | `beduerfnis` trägt eine Angabe | Projekt |
| **Ein Netzwerk** | nichts davon | **keiner** |

Erkannt wird über Feld-Präsenz, nicht über den Typ (Antons Muster 4).

---

## Eine Komponente, kein Modul

| | Modul | Komponente |
|---|---|---|
| **Was** | eine Arbeitsfläche | ein Stück, das woanders erscheint |
| **Wo** | als Reiter in der Kopfzeile | im Panel, im Dialog, auf der Karte, in einer Liste |
| **Wer wählt es** | ein Space, über `Group.data.modules` | niemand: Es erscheint, wo es gebraucht wird |

Die Reiter **im** Profil sind etwas anderes als die Reiter der App. Sie gliedern eine Fläche, sie wechseln keinen Arbeitsort.

---

## Die Regeln

1. **Ein leeres Feld erscheint nicht.** Feld-Präsenz statt Typ-Verzweigung.
2. **Ein leerer Reiter erscheint nicht.** Ein Werk allein füllt seinen Reiter.
3. **Ein einzelner Reiter bekommt keine Leiste.** Eine Reiterleiste mit einem Reiter ist Zierrat.
4. **Höchstens drei Zahlen.** Mehr ist eine Tabelle.
5. **Eine Aktion steht immer hervorgehoben.**
6. **Ein Nein ist eine Antwort.** „Treuhandstiftung: nein" erspart jemandem eine Anfrage.
7. **Ein Gedankenstrich ist keine Antwort.**
8. **Keine Frage steht auf dem Bildschirm.**
9. **Jedes Feld steht an genau einer Stelle.** Doppelt gesagt ist halb geglaubt.
10. **Ein recherchierter Eintrag trägt seine Quelle**, leise am Fuß.
11. **Kein Feld wird erfunden, um die Karte zu füllen.** Was fehlt, fehlt sichtbar.

---

## Das Aussehen

**Die Design-Doktrin gilt** (`memory/feedback_design_doktrin.md`, seit 12.05.2026): Farbflächen statt weißer Karten mit Rahmen, Atemraum statt Trennstriche, `rounded-2xl`, keine schwarzen Umrandungen.

**Die Hausfarbe reist als CSS-Variable.** Eine Hausfarbe ist für weißen Grund gewählt; auf einer dunklen Fläche verschwindet sie. Die dunkle Ansicht greift darum auf den Vordergrund zurück.

---

## Verwandt

- `docs/03-datenmodell.md` — die Felder im Einzelnen
- Skill `/td-profil` — der Weg von der Frage zum Feld
- `DEFINITION.md` Teil 9 im Stack-Repo — warum ein Space das Profil ist
