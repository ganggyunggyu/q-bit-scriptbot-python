from app.fetcher import fetch_raw_xml
from app.parser import parse_items
from app.db import insert_items


def main():
    print("🚀 데이터 수집 시작")

    try:
        print("📡 XML 데이터 요청 중...")
        xml = fetch_raw_xml()

        print("📦 파싱 중...")
        items = parse_items(xml)
        print(f"🔍 {len(items)}개의 item 발견")

        print("🗂️ MongoDB에 삽입 중...")
        insert_items(items)

        print("✅ 작업 완료")
    except Exception as e:
        print(f"❌ 작업 실패: {e}")


if __name__ == "__main__":
    main()
