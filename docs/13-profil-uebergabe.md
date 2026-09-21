# Profile: Übergabe an Janosch

**Stand:** 21.09.2026 · Zusammengestellt von Eli für Janosch

Janosch übernimmt die Definition der Profile. Dieses Blatt sagt in einer Sitzung, was fest liegt, was frei ist, und womit wir tatsächlich arbeiten.

Eli hat dreimal gebaut und dreimal danebengelegen. Die Sackgassen stehen unten, damit sie niemand zweimal geht.

---

## 1. Die wichtigste Zahl zuerst

Der Bestand sind **234 recherchierte Stiftungen**. So viel tragen sie wirklich:

| Feld | gefüllt | Anteil |
|---|---:|---:|
| Name, Anschrift, Ort auf der Karte, Quelle | 234 | 100 % |
| Art (Stiftung, GmbH, Verein) | 234 | 100 % |
| fördernd oder operativ | 234 | 100 % |
| Sitz | 233 | 100 % |
| Förderbereiche | 201 | 86 % |
| Antragsweg | 162 | 69 % |
| Website | 56 | 24 % |
| Zustiftung möglich | 55 | 24 % |
| Förderrahmen (Obergrenze) | 32 | 14 % |
| Förderrahmen (Untergrenze) | 26 | 11 % |

**Ein Eintrag trägt im Schnitt zehn Felder.** Der dünnste acht, der dickste vierzehn.

Und drei Zahlen, die alles verändern:

| | |
|---|---|
| Einträge mit **Bild** | **0** von 234 |
| Einträge mit **Bio** (eigener Text) | **0** von 234 |
| Einträge mit **Werk** (was sie gefördert haben) | **0** von 234 |

Die einzige Ausnahme ist die **Software AG-Stiftung**. Sie ist von Hand gepflegt, trägt 20 Angaben und dient als Maßstab für ein Profil, das seine Einrichtung übernommen hat.

**Das heißt für einen Entwurf:** Was für Bild, Bio und Werk gedacht ist, ist bei 234 von 235 Einträgen leer. Ein Profil muss mit **zehn kurzen Angaben** gut aussehen, und mit zwanzig auch.

---

## 2. Was fest liegt (Antons Protokoll)

Anton hat in `docs/spec/12-profile.md` das **Profil eines Menschen** definiert. Das ist Protokoll, keine Gestaltung, und wir fassen es nicht an:

- Ein Mensch hat **ein** Profil. Seine Kennung ist seine DID, es lebt in seinem persönlichen Space.
- In jeden Space, dem er beitritt, wandert eine **signierte Kopie**. Er gibt sie mit der Annahme der Einladung frei und kann sie jederzeit zurückziehen.
- Die Felder eines Menschen-Profils sind: `displayName`, `bio`, `avatarUrl`, optional ein Ort.

**Was daraus folgt:** Antons Spec sagt nichts darüber, wie ein Profil aussieht, und nichts über Organisationen. Beides ist offen.

Die Fläche für ein Menschen-Profil liegt in `packages/toolkit/src/components/profile/profile-panel-content.tsx`. Sie zeigt Avatar, Name, Bio und die Zahl der Kontakte.

---

## 3. Was frei ist

| Frage | Stand |
|---|---|
| Wie ein Profil **aussieht** | ganz offen, deine Entscheidung |
| Welche Felder eine **Organisation** trägt | offen, Vorschlag steht in `13-profil.md` |
| Wie ein **recherchierter Eintrag** sich von einem **gepflegten** unterscheidet | offen |
| Ob Mensch und Organisation **dieselbe** Fläche teilen | offen |

---

## 4. Die Rahmen, in die gezeichnet wird

Dasselbe Profil erscheint an drei Orten mit sehr verschiedenem Platz:

| Ort | Breite | Was drumherum steht |
|---|---|---|
| **Panel rechts** | 480 px, Spalte am Rand | eigener Schließen-Knopf oben rechts |
| **Item-Detail** auf der Karte | rund 400 px | der Titel steht schon darüber, Kommentarfeld darunter |
| **Landingpage** (später) | volle Seite | nichts |

Dazu das Telefon: Das Panel wird dort zum Schlitten von unten.

**Live ansehen:** <https://trustdonation.org/app>
Ein Klick auf eine Nadel auf der Karte zeigt ein recherchiertes Profil. Die Taste rechts oben in der Kopfzeile zeigt das Profil des offenen Space.

---

## 5. Die drei Sackgassen

**Erster Versuch: der Fragebogen.** Sechs Abschnitte untereinander, jeder mit seiner Frage als Überschrift: *"Wer ist das · Mit wem habe ich es zu tun?"*. Timo: *"Das ist ja jetzt wirklich dumm Design."*

Gelernt: Die Fragen helfen beim Bauen. Auf dem Bildschirm haben sie nichts verloren.

**Zweiter Versuch: das Datenblatt.** Kopf, Kennzahlen, Reiter. Besser gegliedert, und trotzdem Beschriftung links, Wert rechts, bis nach unten.

Gelernt: Gliederung allein macht noch kein Profil.

**Dritter Versuch: Profil nach Instagram-Vorbild.** Cover, Logo, Bio, Zahlen, runde Themen-Kacheln, Reiter, Werk als Karten.

Gelernt: Gebaut für eine Datenlage, die es nicht gibt. Bio, Bild und Werk sind bei 234 von 235 Einträgen leer, also fällt genau das weg, was die Fläche tragen sollte.

---

## 6. Die Frage, die wirklich offen ist

Ein recherchierter Eintrag ist **kein Auftritt**. Er ist eine Visitenkarte, die jemand anders geschrieben hat, und er wartet darauf, dass die Stiftung ihn übernimmt.

Das sind zwei verschiedene Dinge, und vielleicht brauchen sie zwei verschiedene Flächen:

| | Recherchierter Eintrag | Übernommenes Profil |
|---|---|---|
| Wer hat es geschrieben | wir | die Einrichtung |
| Wie viel steht drin | zehn Angaben | zwanzig und mehr |
| Bild, Bio, Werk | nichts davon | alles |
| Wozu ist es da | jemanden finden und einschätzen | sich zeigen |

**Die Fragen an dich:** Ist das eine Fläche in zwei Zuständen, oder sind es zwei? Und was macht den Unterschied sichtbar, ohne den dünnen Eintrag schlecht aussehen zu lassen?

---

## 7. Wo was liegt

| Was | Wo |
|---|---|
| Unser Vorschlag zur Definition | `docs/13-profil.md` (dieses Repo) |
| Antons Protokoll-Spec | `20-repos/rls-uebersicht/docs/spec/12-profile.md` |
| Die Regel (welche Felder, welche Reiter) | `packages/td-core/src/profil.ts` |
| Die Fläche | `packages/td-ui/src/profil-flaeche.tsx` |
| Die Musterdaten | `packages/td-core/daten/items.json`, `profil-sagst.json` |

Die Trennung ist Absicht: **Die Regel weiß nichts von der Oberfläche.** Wer die Darstellung ändert, fasst eine einzige Datei an.

---

## 8. Design-Vorgaben, die gelten

Aus `memory/feedback_design_doktrin.md` (seit 12.05.2026), Timos Linie:

- **Farbflächen statt weißer Karten mit Rahmen.** Keine Borders, keine Trennstriche.
- `rounded-2xl`, Atemraum durch Polster statt durch Linien.
- Hell und dunkel müssen beide tragen.

Und aus `/klare-sprache`: echte Umlaute, keine Gedankenstriche, keine Verneinungen.

---

## 9. Was Eli beitragen kann

Zeichne, und Eli baut. Eine Skizze, ein Foto einer Skizze, eine Referenzseite: daraus wird die Fläche.

Nützlich wäre außerdem eine Antwort auf Abschnitt 6, denn davon hängt alles Weitere ab.
