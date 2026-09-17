# Zusammen testen

**Für das Wochenende mit Emil und Janosch.**

Der Prototyp soll keine Vorführung bleiben. Ihr sollt euch anmelden, euch gegenseitig bestätigen und gemeinsam an einem Board arbeiten. Das geht, und hier steht der Weg.

---

## Was vorher geprüft ist

Am 17.09.2026 gegen die laufende Instanz und das echte Relay:

| Schritt | Dauer |
|---|---|
| Erste Identität anlegen | 5,6 Sekunden |
| Verbindung zum Relay | sofort |
| Zweite Identität anlegen | 5,8 Sekunden |
| **Gegenseitige Verifizierung** | 5,5 Sekunden |

Der Probelauf liegt als Test bei: `apps/reference/e2e-live/zusammen.spec.ts` im Stack-Repo. Er lässt sich vor dem Treffen noch einmal fahren.

---

## Zwei Türen, ein Haus

Die App kennt zwei Wege, und das ist Absicht:

| | Wofür | Adresse |
|---|---|---|
| **App öffnen** | Stiftungen und Gäste. Beispieldaten, 234 Stiftungen auf der Karte, keine Anmeldung. | `trustdonation.org/app` |
| **Anmelden** | Ihr. Eigene Identität, eigene Gruppen, Zusammenarbeit über das Relay. | `trustdonation.org/app/?connector=wot` |

Beide stehen jetzt oben auf der Landingpage. In der App steht im angemeldeten Fall nichts, im Beispielfall der Hinweis **„Beispieldaten · Mein Konto"**.

**Die beiden Welten wissen nichts voneinander.** Wer sich anmeldet, sieht die 234 Stiftungen zunächst nicht: Sie liegen in den Beispieldaten, nicht in eurem Datenraum. Das ist kein Fehler, sondern die Trennung von Prüfstand und echtem Konto.

### Die Stiftungen in euren Space holen

Seit proto-12 geht es doch, und zwar in eine Richtung: Ihr könnt die 234 Stiftungen **in euren eigenen Space übernehmen**.

1. Anmelden und den Space wählen, in den sie sollen
2. An die Adresse in der Leiste `&import=stiftungen` anhängen und Eingabe drücken
3. **Das Passwort noch einmal eingeben.** Das Neuladen sperrt die Identität, weil der Schlüssel im Arbeitsspeicher liegt und mit der Seite verschwindet.
4. Die Rückfrage nennt den Space und die Anzahl. **Übernehmen** klicken
5. Warten, bis **Fertig** steht. Das Fenster dabei offen lassen.

Danach gehören sie dem Space: Sie laufen über das Relay, jedes Mitglied sieht sie, und wer eine ändert, ändert sie für alle. Ein zweiter Lauf verdoppelt nichts.

**Vorher überlegen, in welchen Space.** 234 Einträge nimmt man nicht mit einem Klick zurück.

---

## Der Ablauf am Wochenende

### 1. Jeder legt seine Identität an

Auf **Anmelden** gehen, dann:

1. **Identity generieren**
2. **Zwölf Wörter aufschreiben.** Auf Papier, nicht ins Telefon. Sie sind der einzige Weg zurück, wenn das Gerät verloren geht.
3. Drei der Wörter zurückgeben
4. Namen eintragen
5. Ein Passwort setzen (mindestens acht Zeichen)

Dauert unter einer Minute. Der Schlüssel entsteht auf dem Gerät und verlässt es nie.

**Stift und Papier bereitlegen**, bevor ihr anfangt. Ohne die zwölf Wörter ist ein verlorenes Konto verloren.

### 2. Ihr bestätigt euch gegenseitig

Das ist der Kern, und es ist der Grund, warum man sich dafür trifft: **Vertrauen entsteht von Angesicht zu Angesicht.**

Einer öffnet sein Nutzermenü rechts oben, dann **Verifizieren**. Der andere scannt den QR-Code. Dann umgekehrt.

Erst danach steht ihr in den Kontakten des anderen, und erst dann könnt ihr euch einladen.

### 3. Timo legt eine Gruppe an und lädt ein

1. Im Umschalter oben links auf **Neue Gruppe erstellen**
2. Name geben, zum Beispiel „Wochenende"
3. Zahnrad an der Gruppe, Bereich **Einladen**
4. Emil und Janosch auswählen, **Einladen**

Bei ihnen erscheint **Neue Einladung**, sie öffnen sie und sind drin.

### 4. Gemeinsam arbeiten

Ab jetzt sieht jeder, was die anderen tun. Zum Ausprobieren:

- **Kanban:** Aufgaben anlegen, verschieben, jemandem zuweisen
- **Feed:** Beiträge schreiben, kommentieren, reagieren
- **Kalender:** Termine anlegen
- **Karte:** Orte eintragen
- **Liste:** alles zusammen

Die Änderungen laufen über `relay.web-of-trust.de` und erscheinen beim anderen in Sekunden.

---

## Woran es hängen kann

| Was passiert | Was dahintersteckt | Was hilft |
|---|---|---|
| Nach dem Anmelden ist alles leer | Richtig so. Ein neues Konto hat keine Gruppen. | Eine Gruppe anlegen oder sich einladen lassen |
| Der andere erscheint nicht in den Kontakten | Ihr habt euch noch nicht verifiziert | Nutzermenü, Verifizieren, QR-Code scannen |
| Die Einladung kommt nicht an | Das Relay braucht einen Moment, oder der andere ist offline | Seite neu laden, warten. Beide brauchen den grünen Punkt oben rechts. |
| Kein grüner Punkt | Keine Verbindung zum Relay | Netz prüfen. Ohne Verbindung bleibt alles lokal und wird später abgeglichen. |
| Timos Konto sieht anders aus als sonst | Der Browserspeicher hängt an der Adresse. `trustdonation.org` ist eine andere als `wir.ooo`. | Mit den zwölf Wörtern wiederherstellen: **Ich habe bereits einen Seed** |

---

## Was ihr im Blick behalten solltet

Es ist ein Prototyp, und er soll zeigen, wo es klemmt. Notiert, was auffällt:

- Wo zögert die App?
- Wo ist unklar, was ein Knopf tut?
- Was habt ihr gesucht und nicht gefunden?
- Was hat sich falsch angefühlt?

Der Durchgang mit Erwartungen steht in `docs/TESTPLAN.md` des Stack-Repos. Abschnitt G ist genau dafür: was einen Menschen stört.

---

## Danach

Was ihr anlegt, bleibt in euren Konten. Es ist **nicht** Teil des Prototyps, den eine Stiftung sieht, und das ist gut: Euer Ausprobieren soll den Pitch nicht verändern.

Wenn etwas wirklich trägt, kann es später in die Beispieldaten wandern.
