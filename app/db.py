from pymongo import MongoClient
from typing import List, Dict
from .config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def insert_items(items: List[Dict]) -> None:
    """자격증 리스트를 MongoDB에 삽입"""
    if not items:
        print("⚠️ 삽입할 자격증이 없습니다.")
        return

    try:
        result = collection.insert_many(items)
        print(f"✅ {len(result.inserted_ids)}개 문서 삽입 완료.")
    except Exception as e:
        print(f"❌ 삽입 중 오류 발생: {e}")
