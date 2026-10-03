"""Kleine Logging-Vorlage für Python-Anwendungen.

Anwendung: logging.getLogger(__name__) in Modulen verwenden und die
Konfiguration einmal am Programmeinstieg aufrufen.
"""

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Richtet eine einfache Ausgabe mit Zeitstempel und Level ein."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


logger = logging.getLogger(__name__)


def perform_operation() -> bool:
    """Beispiel: Fehler mit Traceback erfassen, ohne sensible Werte zu loggen."""
    try:
        # Hier die eigentliche Operation einsetzen.
        return True
    except (OSError, ValueError) as exc:
        # Nur unkritische technische Angaben protokollieren.
        logger.warning("Operation fehlgeschlagen (%s)", type(exc).__name__)
        return False
    except Exception:
        # logger.exception ergänzt den Traceback. Keine Tokens, Passwörter,
        # Request-Bodies oder andere vertrauliche Eingaben an den Logger geben.
        logger.exception("Unerwarteter Fehler bei der Operation")
        return False


if __name__ == "__main__":
    configure_logging()
    success = perform_operation()
    raise SystemExit(0 if success else 1)
