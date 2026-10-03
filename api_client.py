"""
Einfacher API-Client als Beispiel zum Testen mit Requests.
"""
import requests
from typing import Dict, Any, Optional


class APIClient:
    """Client für API-Aufrufe mit Error-Handling."""
    
    def __init__(self, base_url: str, timeout: int = 5):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        GET-Request mit Error-Handling.
        
        Args:
            endpoint: API-Endpoint
            params: Query-Parameter
            
        Returns:
            Response als Dictionary
            
        Raises:
            requests.exceptions.RequestException: Bei Netzwerkfehlern
            requests.exceptions.HTTPError: Bei HTTP-Errors
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise requests.exceptions.Timeout(f"Request timeout für {self.base_url}")
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError(f"Verbindungsfehler: {e}")
        except requests.exceptions.HTTPError as e:
            raise requests.exceptions.HTTPError(f"HTTP-Error: {e.response.status_code}")
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        POST-Request mit Error-Handling.
        
        Args:
            endpoint: API-Endpoint
            data: Request-Body
            
        Returns:
            Response als Dictionary
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"POST-Request fehlgeschlagen: {e}")
    
    def close(self):
        """Session schließen."""
        self.session.close()
