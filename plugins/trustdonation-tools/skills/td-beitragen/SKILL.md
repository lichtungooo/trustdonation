---
name: td-beitragen
description: "Etwas von uns in Antons Stand zurueckbringen. Aus einer Naht einen sauberen Pull Request an real-life-org/real-life-stack machen: Anwendungsfall zuerst, Spec-Aenderung dazu, Tests, und was danach mit der Naht passiert."
---

# Etwas zu Anton zurueckbringen

Die Gegenrichtung zu `td-anton`. Wir geben etwas vor, gleichen es mit seinem Stand ab und bringen es hinein.

**Der Gewinn ist doppelt:** Was er uebernimmt, ist danach keine Naht mehr, und alle anderen Instanzen bekommen es mit.

## Wann ein Beitrag lohnt

| Lage | Beitragen? |
|---|---|
| Eine Naht mit **hohem Risiko** (A1, A2) | ja, das ist der wichtigste Fall |
| Eine Naht, die **jede Instanz** braucht (Zuhause-Space, Arten) | ja |
| Ein **Haken**, den wir uns wuenschen | ja, und das ist der beste Beitrag: er hilft auch anderen, die erweitern wollen |
| Etwas, das **nur trustdonation** braucht | nein, das bleibt bei uns |
| Unsere **Musterdaten** | nie |
| Unsere **Definition** | nein, die gehoert in `docs/DEFINITION.md` |

Faustregel: **Was Anton definieren wuerde, wenn er daran gedacht haette, gehoert zu ihm. Was unsere Sache ist, bleibt bei uns.**

Er hat gesagt, dass er die Funktionalitaet selbst definieren will. Das spricht nicht gegen Beitraege, es spricht dafuer, sie als **Angebot** zu formulieren: der Anwendungsfall und eine Skizze, nicht ein fertiger Umbau, den er nur noch abnicken soll.

## Vorbereiten

```bash
cd /d/Workspace/20-repos/rls-uebersicht
python td-tools/anton-stand.py            # steht er still? dann ist jetzt gut
git fetch origin master
```

Ein Beitrag setzt auf **seinem aktuellen Stand** auf, nie auf unserem Prototyp-Branch:

```bash
git checkout -b beitrag/<kurzer-name> origin/master
```

Dann die Aenderung **neu** aufbauen, nicht aus dem Prototyp kopieren. Der Prototyp traegt Dinge, die nur uns angehen (Musterdaten, unsere Bereiche), und die gehoeren nicht in seinen PR.

## Was in einen Beitrag gehoert

1. **Die Aenderung selbst**, so klein wie sie sein kann. Ein Thema, ein PR.
2. **Die Spec-Aenderung dazu.** Bei ihm gewinnt die Spec: Eine neue Regel, die nur im Code steht, ist bei ihm ein Fehler. Also `docs/spec/` mitschreiben.
3. **Tests.** Fuer jede Regel, die eine Liste betrifft.
4. **Keine Spuren von uns.** Kein `trustdonation` in Bezeichnern, keine Musterdaten, keine Verweise auf unsere Dateien.

## Der Text

Er beginnt mit dem **Anwendungsfall**. Das ist Antons ausdruecklicher Wunsch, siehe `memory/feedback_pr_mit_use_case.md`.

```markdown
## Warum

<Der Anwendungsfall in zwei bis vier Saetzen. Was ein Mensch tun will,
und was ihn heute daran hindert. Konkret, mit Namen: "Eine Stiftung
traegt ihre Foerderschwerpunkte" ist besser als "Spaces brauchen Felder".>

## Was fehlt

<Der Haken, knapp. Am besten mit Verweis auf ein Muster, das er selbst
schon benutzt: "wie beim Modul-Register" wiegt mehr als jede Begruendung.>

## Vorschlag

<Signatur oder Skizze. Kurz. Es ist ein Angebot, keine Vorlage.>

## Spec

<Welche Datei in docs/spec/ mitgeaendert ist und welche Regel dazukommt.>

## Was damit moeglich wird

<Ein bis zwei Saetze, was andere Instanzen davon haben. Nicht nur wir.>
```

Deutsch, echte Umlaute, keine Gedankenstriche, siehe Skill `klare-sprache`.

## Absenden

```bash
git push fork beitrag/<kurzer-name>
gh pr create --repo real-life-org/real-life-stack \
  --base master --head lichtungooo:beitrag/<kurzer-name> \
  --title "<knapp, was es tut>" --body-file <text.md>
```

Den Text vorher in eine Datei im Scratchpad schreiben. Lange Texte ueber `--body` scheitern an der Zeilenlaenge.

## Danach

1. **In `docs/NAEHTE.md` eintragen**, dass ein Wunsch unterwegs ist, mit PR-Nummer. Die Zeile „Naehte mit offenem Wunsch" oben nachziehen.
2. **Im Stand vermerken** (`memory/stand_trustdonation.md`).
3. **Warten.** Der Prototyp bleibt, wie er ist. Wir bauen nicht auf einem PR auf, der noch offen ist.

## Wenn er uebernimmt

Das ist das Ziel, und es hat einen eigenen Ablauf:

1. `td-anton` meldet die Commits.
2. `td-update` spielt sie ein.
3. **Unsere Fassung weicht seiner.** Nicht umgekehrt, auch wenn seine anders aussieht als unsere. Zwei Fassungen derselben Sache sind der Fehler, gegen den alles hier gebaut ist.
4. Die Naht aus `docs/NAEHTE.md` **entfernen** und die Zahlen nachziehen.
5. Unsere Bereiche auf seinen Haken umbauen.

## Wenn er nicht uebernimmt

Auch das ist ein Ergebnis, und es kostet nichts.

1. Die Naht bleibt, mit einem Satz im Eintrag, warum sie bleibt.
2. Bei einer Naht mit hohem Risiko den **Zwischenschritt** gehen: den Inhalt nach `td-ui` oder `td-core` ziehen, sodass bei ihm ein Aufruf stehenbleibt.
3. Kein Nachhaken. Er hat gute Gruende, seinen Stack zu schuetzen, und das ist auch in unserem Interesse.

## Offene Beitraege

| PR | Was | Stand |
|---|---|---|
| [#379](https://github.com/real-life-org/real-life-stack/pull/379) | Netzwerke, Arten, Zuhause-Space, Gliederung im Umschalter | offen, bleibt als Vorlage |
| [#6](https://github.com/real-life-org/claude-plugins/pull/6) | Sprach-Skills in `claude-plugins` | offen |

## Verwandt

- `memory/feedback_pr_mit_use_case.md` der Anwendungsfall zuerst
- `docs/NAEHTE.md` die Wuensche, die PRs werden wollen
- Skills `td-anton`, `td-naht`, `klare-sprache`
