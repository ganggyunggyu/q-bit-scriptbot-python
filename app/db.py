from pymongo import MongoClient
from typing import List, Dict
from .config import MONGO_URI, MONGO_DB, MONGO_COLLECTION
from .generate_outlook import generate_outlook  
from .guess_exam_agency import guess_exam_agency
from tqdm import tqdm

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def insert_items(items: List[Dict]) -> None:
    """item 리스트를 MongoDB에 삽입 (중복 방지용 upsert 처리)"""
    if not items:
        print("⚠️ 삽입할 item이 없습니다.")
        return

    inserted_count = 0
    for item in tqdm(items, desc="🚚 MongoDB 저장 중", unit="item"):
        
        item["outlook"] = generate_outlook(item)  
        item["agency"] = guess_exam_agency(item['jmfldnm'])  

        filter_query = {"jmcd": item.get("jmcd")}  
        update_doc = {"$set": item}

        result = collection.update_one(filter_query, update_doc, upsert=True)
        if result.upserted_id:
            inserted_count += 1

    print(f"✅ {inserted_count}개 문서 새로 삽입됨 (upsert 처리됨)")