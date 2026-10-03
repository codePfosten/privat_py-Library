# privat_py-Library

Sachen nur einmal machen, dafür gut.

Eine kleine, wiederverwendbare Sammlung von Prompts und Codevorlagen für Softwareentwicklung. Die Vorlagen liegen nach ihrem Einsatzbereich sortiert in `ai/Agent/`.

## Vorlagen finden

| Bereich | Inhalt |
| --- | --- |
| [`ai/Agent/review/`](ai/Agent/review/) | Code-, Sicherheits-, Performance- und Architektur-Reviews |
| [`ai/Agent/testing/`](ai/Agent/testing/) | Testplanung und OAuth-Tests |
| [`ai/Agent/automation/`](ai/Agent/automation/) | Zuverlässigkeit für unbeaufsichtigte Abläufe |
| [`ai/Agent/documentation/`](ai/Agent/documentation/) | Technische Dokumentation |
| [`ai/Agent/ide/`](ai/Agent/ide/) | Kurze Prompts für IntelliJ und IDE-Assistenten |
| [`ai/Agent/implementation/`](ai/Agent/implementation/) | Fehlerbehebung, Refactoring und neue Anforderungen |
| [`ai/Agent/templates/`](ai/Agent/templates/) | Wiederverwendbare Python-Codebausteine |

### Reviews

- [`review.txt`](ai/Agent/review/review.txt) – Codequalität, Architektur und Wartbarkeit
- [`architecture.txt`](ai/Agent/review/architecture.txt) – Architekturgrenzen, Abhängigkeiten und Änderbarkeit
- [`security.txt`](ai/Agent/review/security.txt) – Sicherheits- und Datenschutzprüfung
- [`performance.txt`](ai/Agent/review/performance.txt) – Engpässe und Optimierungsvorschläge

### Tests und Automatisierung

- [`test.txt`](ai/Agent/testing/test.txt) – Tests für vorhandenes Verhalten
- [`OAuth_test.txt`](ai/Agent/testing/OAuth_test.txt) – Offline-Tests für OAuth- und Tokenlogik
- [`clean_für_automatisch.txt`](ai/Agent/automation/clean_für_automatisch.txt) – Zuverlässigkeit und Sicherheit bei automatisierten Abläufen

### Umsetzung und IDE

- [`bugfix.txt`](ai/Agent/implementation/bugfix.txt) – Fehler nachvollziehbar beheben
- [`refactoring.txt`](ai/Agent/implementation/refactoring.txt) – Verhaltenserhaltendes Refactoring
- [`requirements.txt`](ai/Agent/implementation/requirements.txt) – Anforderungen vor der Umsetzung klären
- [`documentation.txt`](ai/Agent/documentation/documentation.txt) – Dokumentationsprüfung und -planung
- [`intellij.txt`](ai/Agent/ide/intellij.txt) – Kurze IntelliJ-Prompts

### Codevorlagen

- [`python_logging.py`](ai/Agent/templates/python_logging.py) – kleines, konfigurierbares Logging-Grundgerüst
- [`Request_test_vorlange.py`](ai/Agent/templates/Request_test_vorlange.py) – Offline-Mocks für einfache GET- und POST-Aufrufe

## Verwendung

Öffne die passende Textdatei und kopiere den Prompt in deinen AI-Assistenten. Passe Platzhalter und Projektkontext an. Prüfe vor dem Einsatz, ob die Vorlage zu den Konventionen des jeweiligen Projekts passt.

Die Vorlagen unterscheiden klar zwischen Analyse und Umsetzung. Review-Vorlagen verändern keinen Code; Umsetzungsvorlagen verlangen eine Prüfung des vorhandenen Projekts und begrenzen Änderungen auf den jeweiligen Auftrag.

## Grundsätze

- kurz, verständlich und wiederverwendbar
- keine Funktionen oder Anforderungen erfinden
- bestehende Projektkonventionen beachten
- Änderungen nachvollziehbar halten
- sensible Daten schützen

## Lizenz

Das Repository hat derzeit keine explizite Open-Source-Lizenz.
