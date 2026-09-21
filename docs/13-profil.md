# Das Profil

**Status:** Normativer Entwurf · Vierte Fassung, 21.09.2026 · Vorgabe von Janosch

Timo am 18.09.2026: *"Ich will so eine Karte haben, wo alles draufsteht, was eine Stiftung macht."*

Nach drei Fehlversuchen von Eli hat Janosch (UX im Kernteam) am 21.09.2026 die Vorgabe gemacht. Diese Fassung setzt sie um. Die Sackgassen davor stehen in `13-profil-uebergabe.md`.

---

## Janoschs Vorgabe im Wortlaut

> Es gibt ein Bild. Wenn kein Bild vorhanden ist, dann ist dort ein Platzhalterbild, sodass man das Bild manuell ergänzen kann. Es gibt einen Namen. Es gibt Mitwirkende. Es gibt eine Liste relevanter Details, die sich aus den Texten ergibt, die zu finden sind. Es gibt eine Hashtag-Funktion für wesentliche Inhalte, beispielsweise Themen, der Name, der Gründer. Hashtags können vorgeschlagen werden von Anfang an und manuell ergänzt werden. Es gibt ein Datum, wann die Stiftung gegründet wurde, und eine Zusammenfassung wesentlicher Meilensteine. Es gibt eine Karte, wo gezeigt wird, wo diese Stiftung sich befindet. Es gibt ein Feld für Stiftungsdetails rechtlicher Art und ein Textfeld, um Details selbstständig zu ergänzen. Dann ein Kontaktinformationsfeld inklusive Verweis auf die Internetseite, Adresse, Telefonnummer, E-Mail. Das Profil ist so angeordnet, dass die wichtigen Informationen ganz oben stehen und je mehr es ins Detail geht, weiter unten. In einer Art Collage. Diese Collage kann man manuell abändern, sodass man Informationen per Drag and Drop nach oben ziehen kann und umgekehrt.

---

## Die Anatomie

**Ein Kopf, der steht, und eine Collage, die sich bewegt.**

```
+----------------------------------------------+
| ######## Farbband in der Hausfarbe ######### |
|  +----+                                      |
|  | SA |   Software AG-Stiftung               |  Kopf, fest
|  +----+   Stiftung · fördernd · Darmstadt    |
+----------------------------------------------+
|  [ SCHLAGWORTE                             ] |
|  [ #Bildung #KinderUndJugend #PeterSchnell ] |
|  [ WAS SIE WISSEN SOLLTEN                  ] |
|  [ Hinweis, Zweck, Förderbereiche, Antrag  ] |  Collage,
|  [ GESCHICHTE  Zeitstrahl 1992 … 2022      ] |  verschiebbar
|  [ WO          Karte mit Nadel             ] |
|  [ MITWIRKENDE ]  [ KONTAKT               ] |
|  [ RECHTLICHES ]  [ EIGENE NOTIZ          ] |
+----------------------------------------------+
```

### Der Kopf

Bild, Name, Einordnungszeile. Er ist die Identität und bleibt oben.

**Das Bild hat einen Platzhalter.** Fehlt es, steht dort das Kürzel auf der Hausfarbe, und wer das Profil pflegt, sieht beim Darüberfahren *„Bild ergänzen"*. Keine von 234 recherchierten Stiftungen trägt ein Bild; der Platzhalter ist der Normalfall.

### Die Kacheln, in ihrer Rangfolge

| Kachel | Was darin steht | Breite |
|---|---|---|
| **Schlagworte** | vorgeschlagen aus Förderbereichen, Zielgruppen, Gründer, Sitz; von Hand ergänzte stehen vorn | breit |
| **Was Sie wissen sollten** | der Hinweis zuerst, dann Zweck, Förderbereiche, Zielgruppen, Förderrahmen, Antrag, Zustiftung | breit |
| **Geschichte** | Gründungsjahr und Meilensteine als Zeitstrahl, alt nach neu | breit |
| **Wo** | Karte mit Nadel und Anschrift | breit |
| **Mitwirkende** | Menschen, Gründer | schmal |
| **Kontakt** | Website, Mail, Telefon, Ansprache | schmal |
| **Rechtliches** | Rechtsform, Register, Aufsicht, Gemeinnützigkeit, Steuernummer | schmal |
| **Eigene Notiz** | freier Text dessen, der pflegt | breit |

Die Rangfolge ist Janoschs Regel: *wichtig oben, Details unten*. Ein Projekt hat dieselben acht Kacheln mit seinen eigenen Feldern (`BAUPLAN_PROJEKT`).

**Eine Kachel ohne Inhalt erscheint nicht.** Ein recherchierter Eintrag zeigt in der Regel drei: Schlagworte, Details, Wo. Ein gepflegtes Profil zeigt alle acht.

### Die Collage

Jede Kachel lässt sich greifen und woanders ablegen. Die gewählte Reihenfolge bleibt im Browser dessen, der sie gewählt hat (`localStorage`, je Profil). Ein recherchierter Eintrag gehört niemandem, also darf niemand die Reihenfolge für alle festlegen.

**Eine gespeicherte Reihenfolge ist eine Wunschliste, kein Bestand.** Sie nennt Kacheln, die es nicht mehr gibt, und kennt neue nicht. Was genannt ist und existiert, kommt in der genannten Reihenfolge; alles Übrige folgt der Rangfolge des Bauplans. Nichts geht verloren.

Das Ziehen läuft über die HTML5-Schnittstelle des Browsers, wie bei Antons Kanban-Brett. Die Kennung der gezogenen Kachel trägt der Browser selbst mit (`dataTransfer`); React-Zustand zwischen `dragstart` und `drop` ist fragil.

---

## Die Schlagworte

Vorgeschlagen wird aus dem, was dasteht. Aus einem Wort wird ein Schlagwort: *„Kinder und Jugend"* wird `#KinderUndJugend`, *„umwelt"* wird `#Umwelt`, *„SAGST"* bleibt `#SAGST`. Umlaute bleiben, sie sind Teil des Wortes.

**Von Hand ergänzte stehen vorn.** Ein Vorschlag ist geraten, eine Ergänzung ist gemeint. Doppelte fallen weg, auch bei unterschiedlicher Schreibweise.

---

## Die Karte

Ein Mosaik aus Kartenkacheln, denselben, die Antons Leaflet-Adapter lädt (`tile.openstreetmap.org`). Welche Kacheln und wo die Nadel steht, rechnet `kartenAusschnitt` in `td-core`, geprüft gegen eine unabhängige Rechnung.

**Warum kein eingebetteter Rahmen:** Die App läuft mit COEP, und das blockiert jedes iframe ohne passende Kopfzeilen. Gemessen am 21.09.2026: `ERR_BLOCKED_BY_RESPONSE`.

**Warum keine Kartenbibliothek:** Sie wiegt ein Megabyte. Sechs Bilder tun dasselbe.

---

## Wo ein Profil erscheint

| Was | Wo es steht |
|---|---|
| Profil eines Menschen | Panel rechts, über das Nutzermenü (Antons Spec 12) |
| Profil eines Space | Panel rechts, über die Taste in der Kopfzeile (`?profil={spaceId}`) |
| Profil eines recherchierten Eintrags | in seinem Item-Detail, an der Stelle der Meta-Box |

**Ohne Namen kein Kopf.** Im Item-Detail trägt die Ansicht den Titel schon; die Collage beginnt dann bei der Einordnungszeile.

---

## Wer ein Profil trägt

**Wer keinen Bauplan hat, hat kein Profil.** Die Regel steht in `bauplanFuer` und `traegtProfil`.

| Wer | Woran erkannt | Bauplan |
|---|---|---|
| Ein Space mit Art | `kind: "stiftung"` oder `"projekt"` | Förderer, Projekt |
| Ein recherchierter Eintrag | `foerdererart` trägt eine Angabe | Förderer |
| Ein Vorhaben | `beduerfnis` trägt eine Angabe | Projekt |
| **Ein Netzwerk** | nichts davon | **keiner** |

---

## Die Felder, die diese Fassung neu einführt

| Feld | Form | Kachel |
|---|---|---|
| `image` | url | Kopf |
| `hashtags` | tags | Schlagworte (von Hand ergänzt) |
| `gegruendet` | text | Geschichte |
| `meilensteine` | list, je `"1992: Was geschah"` oder `{ jahr, was }` | Geschichte |
| `address` | text | Wo |
| `mitwirkende` | list | Mitwirkende |
| `gruender` | text | Mitwirkende, und als Schlagwort |
| `telefon` | tel | Kontakt |
| `rechtsform`, `register`, `aufsicht`, `steuernummer` | text | Rechtliches |
| `gemeinnuetzig` | bool | Rechtliches |
| `notiz` | longtext | Eigene Notiz |

Die Software AG-Stiftung trägt sie alle als Maßstab (`profil-sagst.json` nennt die Quellen).

---

## Die Regeln

1. **Der Kopf steht fest, die Collage bewegt sich.**
2. **Eine Kachel ohne Inhalt erscheint nicht.** Feld-Präsenz statt Typ-Verzweigung.
3. **Ohne Bild ein Platzhalter, der einlädt.**
4. **Eine gespeicherte Reihenfolge ist eine Wunschliste.** Nichts geht verloren.
5. **Eigene Schlagworte vor vorgeschlagenen.**
6. **Ein Nein ist eine Antwort.** „Treuhandstiftung: nein" erspart jemandem eine Anfrage.
7. **Jedes Feld steht an genau einer Stelle.**
8. **Keine Frage steht auf dem Bildschirm.**
9. **Ein recherchierter Eintrag trägt seine Quelle**, leise am Fuß.
10. **Kein Feld wird erfunden, um die Karte zu füllen.**

---

## Das Aussehen

**Die Design-Doktrin gilt** (`memory/feedback_design_doktrin.md`, seit 12.05.2026): Jede Kachel ist eine Farbfläche, `rounded-2xl`, ohne Rahmen. Die Hausfarbe reist als CSS-Variable, damit die dunkle Ansicht lesbar bleibt.

---

## Offen

- **Bild ergänzen:** Der Platzhalter ruft einen Haken (`onBildAendern`) auf. Was der tut, ist noch nicht angebunden; dafür braucht es Antons Bild-Upload aus `profile-panel-content.tsx`.
- **Schlagworte von Hand ergänzen** und **die eigene Notiz schreiben**: Das Feld ist da, die Eingabe noch nicht. Beides gehört in den Bereich *Netzwerk* des Space-Dialogs.
- **Reihenfolge für alle:** Wer den Space verwaltet, soll die Collage für alle Besucher festlegen können. Dann wandert die Reihenfolge von `localStorage` nach `Group.data.profilOrdnung`.

---

## Verwandt

- `13-profil-uebergabe.md` — die Übergabe an Janosch mit den echten Zahlen
- `docs/03-datenmodell.md` — die Felder im Einzelnen
- Skill `/td-profil` — der Weg von der Frage zum Feld
