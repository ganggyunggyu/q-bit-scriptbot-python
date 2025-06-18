from pymongo import MongoClient
from typing import List, Dict
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION
from generate_outlook import generate_outlook  
from guess_exam_agency import guess_exam_agency
from api import get_기술사, get_기능장, get_기사_산업기사, get_기능사
from tqdm import tqdm
import time

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def insert_items(items: List[Dict]) -> None:
    """item 리스트를 MongoDB에 삽입 (중복 방지용 upsert 처리)"""
    if not items:
        print("⚠️ 삽입할 item이 없습니다.")
        return

    inserted_count = 0
    print("⏳ 기술사 일정 요청 중...")
    기술사_일정 = get_기술사() or []
    print("✅ 기술사 일정 완료. 10초 대기...")
    time.sleep(10)

    print("⏳ 기능장 일정 요청 중...")
    기능장_일정 = get_기능장() or []
    print("✅ 기능장 일정 완료. 10초 대기...")
    time.sleep(10)

    print("⏳ 기사/산업기사 일정 요청 중...")
    기사_일정 = get_기사_산업기사() or []
    print("✅ 기사/산업기사 일정 완료. 10초 대기...")
    time.sleep(10)

    print("⏳ 기능사 일정 요청 중...")
    기능사_일정 = get_기능사() or []
    print("✅ 기능사 일정 완료. 모든 요청 완료!")

    for item in tqdm(items, desc="🚚 MongoDB 저장 중", unit="item"):
        # ✅ outlook 생성
        item["outlook"] = generate_outlook(item)

        # ✅ agency 추정
        item["agency"] = guess_exam_agency(item['jmfldnm'])

     # ✅ 안전하게 schedule 생성
        seriesnm = item.get("seriesnm") or ""
        schedule = []
        if "기술사" in seriesnm:
            schedule = 기술사_일정
        elif "기능장" in seriesnm:
            schedule = 기능장_일정
        elif "기사" in seriesnm or "산업기사" in seriesnm:
            schedule = 기사_일정
        elif "기능사" in seriesnm:
            schedule = 기능사_일정

        item["schedule"] = schedule     

        # ✅ upsert
        filter_query = {"jmcd": item.get("jmcd")}  # 고유키: jmcd
        update_doc = {"$set": item}

        result = collection.update_one(filter_query, update_doc, upsert=True)
        if result.upserted_id:
            inserted_count += 1

    print(f"✅ {inserted_count}개 문서 새로 삽입됨 (upsert 처리됨)")