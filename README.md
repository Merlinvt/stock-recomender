# Probetag: Python Data Science Engineering Projekt

## Projektübersicht

Das Projekt enthält eine minimale Flask-Applikation, eine `users.csv`-Datei
mit Daten und eine PDF-Datei mit weiteren Erklärungen zur Berechnung. Die
App enthält bereits einen Endpunkt zum Hinzufügen eines Users.

## Aufgabe

### Problembeschreibung

Gegeben sind 100 User in einem System, die Aktien von Unternehmen gekauft
haben. Insgesamt gibt es 20 Unternehmen. Jeder Nutzer hat zwischen 0 und 5
Aktien eines Unternehmens. Anhand dieser Informationen sollen Empfehlungen
für die User berechnet werden: Hat ein anderer User nämlich ähnliche
Aktienpräferenzen wie ich, aber zusätzlich Aktien eines weiteren Unternehmens,
bin ich vielleicht auch am Kauf dieser Aktie interessiert. Insofern fassen
wir die Anzahl der Aktien als eine Bewertung auf, die der User dem Unternehmen
gibt.

### Ziel

Das Ziel ist, eine API / Schnittstelle zu entwickeln, die über die folgenden
Routen verfügt:

1. Es gibt eine `POST`-Route `rate/<user_id>/<company_id>` zum Abgeben einer Bewertung. Dies kann im Format `{"score": 4}` geschehen, d.h. der User hält 4 Aktien vom Unternehmen.
2. Es gibt eine `GET`-Route `neighbors/<user_id>/<company_id>?number=k`  mit Query-Parameter `number`, die die `k`
nächsten Nachbarn für einen User zurückgibt, die Anteile an `<company_id>` besitzen.
3. Es gibt eine `GET`-Route `recommendations/<user_id>?number=k` mit Query-Parameter `number`, die auf Grundlage der
`k` nächsten Nachbarn prognostiziert, wie viele Anteile der User kaufen soll. Zur Berechnung siehe den nächsten Abschnitt. Ausgabeformat kann beispielsweise so sein

```
{
    "Nunez-Ramirez": 0,
    "Scott PLC": 1.02,
     # ...
    "Perez and Sons": 4.21
}
```

Darüber hinaus ist die API immer initialisiert mit den Daten aus `users.csv`, d.h. die 100 Beispieldaten sind immer vorhanden.

### Berechnung der Empfehlungen

Die Ähnlichkeit zwischen `User1` und `User2` kann durch Pearson-Korrelation
festgestellt werden (z.b. über `scipy.stats.pearsonr` oder `numpy.corrcoef`).
Dabei wird die Korrelation zwischen den Bewertungsvektoren berechnet, hier also die
Korrelation zwischen Aktienanteilen.

Schließlich können Bewertungen vorausgesagt werden. Eine Möglichkeit dies zu tun ist
sogennantes [Collaborative Filtering](https://en.wikipedia.org/wiki/Collaborative_filtering#Memory-based).
Eine kleine Anleitung zur Berechnung stelle ich per PDF in diesem Repository bereit.

## Tipps

Wenn keine Erfahrungen in der API-Programmierung vorhanden sind, ist der Flask Quickstart
ein guter Anlaufpunkt. Ist etwas unverständlich, gibt es Probleme oder möchtest du deine Ideen diskutieren, kannst du mich jederzeit anschreiben.
Du kannst auch zunächst in einem Jupyter Notebook prototypen und hinterher deine API bauen.
# stock-recomender
