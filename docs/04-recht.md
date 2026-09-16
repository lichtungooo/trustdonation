# 04 Rechtliche Leitplanken

**Status:** Arbeitsstand, vor Welle 1 anwaltlich zu prüfen

> Dieses Dokument fasst die Leitplanken zusammen, nach denen wir bauen. Es ersetzt keine Rechtsberatung.

## Die Grundregel

Wir dürfen Informationen über Stiftungen sammeln und nutzbar machen. Wir dürfen keine fremden Inhalte, Datenbanken oder persönlichen Kontaktdaten beliebig kopieren.

> **Fakten extrahieren → selbst strukturieren → Quelle angeben → auf das Original verlinken.**
>
> Nicht: eine Website spiegeln.

Wenn eine Stiftung schreibt „Wir fördern Bildung, Jugend und Naturschutz“, dürfen wir diese Tatsache in unserer eigenen Struktur wiedergeben. So arbeiten bestehende Verzeichnisse auch, etwa die Stiftungssuche des Bundesverbands Deutscher Stiftungen mit Themen, Fördertätigkeit, Antragsmöglichkeit und Deutschlandkarte. Wir bauen darüber eine bessere Interaktionsschicht.

## Vier Dinge, die wir sauber auseinanderhalten

| | Umgang |
|---|---|
| **Fakten** | Frei strukturierbar. Zweck, Region, Summen, Fristen, Antragsweg. |
| **Fremde Texte** | Nicht übernehmen. Kein Fließtext von der Website, keine kompletten Förderbedingungen, keine Fotos, keine Logos ohne Erlaubnis. Datenbanken genießen eigenen Schutz. |
| **Personenbezogene Daten** | Nur mit Rechtsgrundlage. Siehe unten. |
| **Bewertungen** | Gar nicht. Keine Sterne, keine Ampeln, keine Note an einer Organisation. |

## Kontaktdaten

`info@stiftung-xyz.de` ist etwas anderes als `max.mustermann@stiftung-xyz.de`.

Eine persönliche Adresse ist ein personenbezogenes Datum. Für die Verarbeitung brauchen wir eine Rechtsgrundlage nach Art. 6 DSGVO. Selbst der Bundesverband veröffentlicht Ansprechpartner mit persönlichen Kontaktdaten nur mit ausdrücklicher Genehmigung.

**Unser Standard:**

1. Allgemeine Kontaktadresse der Stiftung
2. Offizielle Website
3. Offizielles Antragsportal

Eine namentliche Ansprache steht nur dort, wo die Stiftung sie selbst öffentlich als Ansprechpartner ausweist, oder wo sie ihr Profil übernommen hat.

## Werbung per Mail

Eine öffentlich angegebene Adresse auf der Karte zu zeigen, ist etwas anderes, als sie für eine Kampagne zu nutzen. Für elektronische Werbung gilt § 7 UWG, der Mails ohne vorherige Einwilligung streng behandelt.

Für die Ansprache heißt das: persönlicher Erstkontakt mit konkretem Anlass, keine Massenaussendung. Siehe [06-ansprache.md](06-ansprache.md).

## Der Herkunftsblock

Jeder recherchierte Datensatz trägt ihn. Er löst die Frage „stimmt das noch?“, indem er sie offen beantwortet.

| Feld | Beispiel |
|---|---|
| `source` | Stiftung XY |
| `sourceUrl` | Link auf die Seite, von der die Fakten stammen |
| `collectedAt` | 2026-09-16 |
| `checkedAt` | 2026-09-16 |
| `verifiedBy` | `redaktion`, `stiftung` oder `automatisch` |
| `status` | `aktuell` oder `pruefung-noetig` |

Die Karte sagt dann ehrlich: „Diese Angabe wurde vor acht Monaten zuletzt geprüft.“ Das ist wertvoller als eine stille Behauptung.

## Die Stiftung übernimmt ihr Profil

Der sauberste Weg, und langfristig der wichtigste Baustein.

1. Wir legen den Datensatz aus öffentlichen Fakten an, `verifiedBy: redaktion`.
2. Der Eintrag zeigt: **„Ist das Ihr Eintrag? Profil übernehmen.“**
3. Nach der Übernahme pflegt die Stiftung selbst: Förderbereiche, Ansprache, Fristen, Projekte, Förderaufrufe, Zustiftungsmöglichkeiten, Korrekturen. `verifiedBy: stiftung`.

Damit wird aus einer statischen Datenbank ein lebendes Netzwerk, und die Stiftung hat einen direkten Vorteil davon. Rechtlich verschiebt sich der Eintrag von „unsere Recherche“ zu „ihre eigene Angabe“.

## Checkliste vor Veröffentlichung eines Eintrags

- [ ] Alle Texte sind unsere eigene Zusammenfassung, kein Zitat
- [ ] Kein Logo, kein Foto von der fremden Seite
- [ ] Kontakt ist eine allgemeine Adresse, keine persönliche
- [ ] Herkunftsblock vollständig, `checkedAt` gesetzt
- [ ] Keine Bewertung, keine Note, kein Ranking im Eintrag
- [ ] Link auf das Original steht sichtbar

## Verwandt

- [03-datenmodell.md](03-datenmodell.md) die Felder
- [05-matching.md](05-matching.md) warum Vorschläge begründet und nicht benotet werden
