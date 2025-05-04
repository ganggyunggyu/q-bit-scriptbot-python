import requests
from .config import API_URL, SERVICE_KEY


def fetch_raw_xml() -> bytes:
    """공공데이터 API로부터 XML 데이터 가져오기"""
    try:
        response = requests.get(
            API_URL,
            params={'serviceKey': SERVICE_KEY},
            headers={'Accept': 'application/xml'}
        )
        response.raise_for_status()
        return response.content  
    except requests.RequestException as e:
        raise RuntimeError(f"API 요청 실패: {e}")
