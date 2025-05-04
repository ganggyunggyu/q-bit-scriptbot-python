import xmltodict
from typing import List, Dict

def parse_items(xml_data: bytes) -> List[Dict]:
    """XML 데이터를 파싱해서 item 리스트로 변환"""
    parsed = xmltodict.parse(xml_data)

    try:
        items = parsed['response']['body']['items'].get('item')
    except (KeyError, AttributeError):
        print("❌ 파싱 오류: item 경로가 존재하지 않음")
        return []

    # item이 하나만 있으면 dict로 들어오므로 리스트로 변환
    if isinstance(items, dict):
        return [items]
    elif isinstance(items, list):
        return items
    else:
        return []
