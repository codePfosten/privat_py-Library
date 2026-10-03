# ============================================================
# Mock-Requests für Offline-Tests
# ============================================================

from typing import Any


# ============================================================
# 1. GET-Request prüfen
#
# Prüft, ob URL und Header genau dem erwarteten Request
# entsprechen und gibt anschließend eine definierte Antwort zurück.
# ============================================================

def mock_get(
    url: str,
    headers: dict[str, Any] | None = None
):
    # <<< EINGABE: erwartete URL >>>
    expected_url = "https://example.com/test"

    # <<< EINGABE: erwartete Header oder None >>>
    expected_headers = {
        "Authorization": "Bearer test_token"
    }

    # Request überprüfen
    assert url == expected_url
    assert headers == expected_headers

    # <<< EINGABE: Antwort, die dein GET erhalten soll >>>
    return {
        "status_code": 200,
        "json": {
            "success": True
        }
    }


# ============================================================
# 2. GET-Request abfangen und immer dieselbe Antwort liefern
#
# Hier wird der Request NICHT überprüft.
# Alles, was an mock_get() geschickt wird, bekommt dieselbe
# definierte Antwort.
# ============================================================

def mock_get_response(
    url: str,
    headers: dict[str, Any] | None = None
):
    # <<< EINGABE: gewünschter Statuscode >>>
    status_code = 200

    # <<< EINGABE: gewünschte JSON-Antwort >>>
    response_json = {
        "success": True
    }

    return {
        "status_code": status_code,
        "json": response_json
    }


# ============================================================
# 3. GET-Request abhängig von der URL auswerten
#
# Die URL entscheidet, welche Antwort zurückgegeben wird.
# Header werden hier bewusst nicht berücksichtigt.
# ============================================================

def mock_get_by_url(
    url: str,
    headers: dict[str, Any] | None = None
):

    # <<< EINGABE: erster Endpunkt + dessen Antwort >>>
    if url == "https://example.com/token":
        return {
            "status_code": 200,
            "json": {
                "access_token": "new_access_token",
                "expires_in": 3600
            }
        }

    # <<< EINGABE: zweiter Endpunkt + dessen Antwort >>>
    if url == "https://example.com/user":
        return {
            "status_code": 200,
            "json": {
                "name": "Test User"
            }
        }

    # Antwort für unbekannte Endpunkte
    return {
        "status_code": 404,
        "json": {
            "error": "unknown_endpoint"
        }
    }


# ============================================================
# 4. POST-Request prüfen
#
# URL + Header + Body werden überprüft.
#
# Der Body wird nur bei POST berücksichtigt.
# ============================================================

def mock_post(
    url: str,
    headers: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None
):
    # <<< EINGABE: erwartete URL >>>
    expected_url = "https://example.com/token"

    # <<< EINGABE: erwartete Header oder None >>>
    expected_headers = {
        "Authorization": "Bearer client_token"
    }

    # <<< EINGABE: erwarteter Body oder None >>>
    expected_body = {
        "grant_type": "refresh_token",
        "refresh_token": "valid_refresh_token"
    }

    # Request überprüfen
    assert url == expected_url
    assert headers == expected_headers
    assert body == expected_body

    # <<< EINGABE: Antwort, die POST zurückgeben soll >>>
    return {
        "status_code": 200,
        "json": {
            "access_token": "new_access_token",
            "expires_in": 3600,
            "refresh_token": "new_refresh_token"
        }
    }


# ============================================================
# 5. POST-Request nur anhand der URL auswerten
#
# URL entscheidet über die Antwort.
# Header und Body werden NICHT überprüft.
# ============================================================

def mock_post_by_url(
    url: str,
    headers: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None
):

    # <<< EINGABE: erster Endpunkt + Antwort >>>
    if url == "https://example.com/token":
        return {
            "status_code": 200,
            "json": {
                "access_token": "new_access_token",
                "expires_in": 3600,
                "refresh_token": "new_refresh_token"
            }
        }

    # <<< EINGABE: weiterer Endpunkt + Antwort >>>
    if url == "https://example.com/other":
        return {
            "status_code": 200,
            "json": {
                "success": True
            }
        }

    # Unbekannter Endpunkt
    return {
        "status_code": 404,
        "json": {
            "error": "unknown_endpoint"
        }
    }
