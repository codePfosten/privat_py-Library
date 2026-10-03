# privat_py-Library

Sachen nur einmal machen, dafür gut

Eine kleine, wiederverwendbare Sammlung von AI-Agent-Prompts für Softwareentwicklung, Code-Reviews, Tests, Dokumentation und Qualitätschecks. Das Repository ist bewusst einfach gehalten: Es dient als persönliches Bibliotheks- und Prompt-Repository für wiederkehrende Aufgaben, die man nicht jedes Mal neu formulieren möchte.

## Zweck

Dieses Repository sammelt kurze, aber hilfreiche Prompts für verschiedene AI-Assistenten, insbesondere für:

- Code-Review und Architektur-Analyse
- Test-Entwicklung
- Dokumentationsverbesserungen
- Performance-Analyse
- Sicherheits-Reviews
- IntelliJ / IDE-gestützte Codehilfe

Ziel ist es, Standard-Workflows konsistent und schnell nutzbar zu machen.

## Struktur

```text
privat_py-Library/
├── README.md
├── ai/
│   └── Agent/
│       ├── intellij.txt
│       ├── review.txt
│       ├── test.txt
│       ├── documentation.txt
│       ├── performance.txt
│       └── security.txt
└── .gitignore
```

## Enthaltene Agenten

- `intellij.txt` – allgemeine IntelliJ/IDE-Prompts für Dokumentation, Refactoring, Code-Erklärung und Code-Review
- `review.txt` – strukturiertes Code- und Architektur-Review
- `test.txt` – Prompt für das Schreiben und Implementieren von Tests
- `documentation.txt` – Fokus auf technische Dokumentation und Wissensmanagement
- `performance.txt` – Analyse von Performance-Engpässen und Optimierungspotenzialen
- `security.txt` – Sicherheitsreviews und Risikobewertung

## Typischer Einsatz

Die Dateien können direkt als Prompt in:

- IntelliJ IDEA AI Assistant
- GitHub Copilot Chat
- andere lokale oder Editor-basierte AI-Tools

verwendet werden. So lassen sich standardisierte Prüfungen und Review-Schritte schnell wiederholen, ohne jedes Mal dieselben Anweisungen neu zu formulieren.

## Grundprinzipien

- Keine unnötige Komplexität
- klare Aufgabenbeschreibung
- Fokus auf Wiederverwendbarkeit
- keine Codeänderungen ohne explizite Freigabe
- Prompts sollen nachvollziehbar, präzise und fokussiert sein

## Ideen für Erweiterungen

Das Repository kann später um weitere Spezialisten erweitert werden, zum Beispiel:

- `bugfinder.txt`
- `refactor.txt`
- `architecture.txt`
- `devops.txt`
- `requirements.txt`
- `dependency-review.txt`

## Hinweise

Dieses Repository ist als private Sammlung und persönliches Werkzeug gedacht. Es ist bewusst klein, aber erweiterbar und eignet sich gut als Basis für eigene Prompt-Patterns im Team oder für persönliche Workflows.

## Lizenz

Das Repository ist derzeit ohne explizite Open-Source-Lizenz. Wenn du es öffentlich teilen möchtest, solltest du vorab eine passende Lizenz wählen.

## Ziel

Das Ziel dieses Repositories ist einfach:

Wiederholbare, gute Engineering- und Review-Workflows möglichst ohne Mehrfacharbeit nutzbar machen.
