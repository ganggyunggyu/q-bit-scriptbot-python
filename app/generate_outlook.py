import re


def refine_sentence(text: str) -> str:
    
    text = re.sub(r"분야에서 활용되는 .*? 등급의 국가기술자격으로, (.*?) 분야", r"\1 분야", text)

    
    text = re.sub(r"\.\s+\.", ".", text)
    text = re.sub(r"\s{2,}", " ", text)

    
    text = text.replace("있으며,", "있고,")
    text = text.replace("있습니다. 또한", "있습니다. 더불어")
    text = text.replace("해당 분야", "그 분야")

    return text.strip()


def generate_outlook_by_field(field_name: str) -> str:
    domain_templates = {
        "자동차": (
            "자동차 산업의 고도화, 전동화 및 자율주행 기술 확산에 따라 정비·설계 분야의 전문 기술인력 수요가 증가하고 있습니다. "
            "자동차 정비소, 제조사 서비스센터, 검사소, 관련 공공기관 등 다양한 진출 경로가 존재합니다."
        ),
        "정보통신": (
            "IT 및 디지털 전환 시대에 따라 시스템 개발, 정보 보안, 데이터베이스 관리 등 다양한 분야에서 정보처리 인재의 수요가 증가하고 있습니다. "
            "공공기관, 금융, 제조, 스타트업 등 거의 모든 산업에서 활용도가 높습니다."
        ),
        "기계": (
            "기계 분야는 제조업의 핵심으로, 자동화·스마트팩토리 확산과 함께 다양한 산업에서 기계 설계, 유지보수, 생산관리 인력의 수요가 늘고 있습니다. "
            "기계설비 회사, 공기업, 발전소, 플랜트 등에서 진출이 가능합니다."
        ),
        "전기전자": (
            "전기 및 전자 산업은 에너지 전환과 스마트시티 구축과 맞물려 고도화되고 있으며, 관련 자격은 전기설비 설계 및 시공, 안전 관리 등에서 활용됩니다. "
            "전력회사, 공기업, 아파트 관리소, 산업 시설 등 다양한 영역으로 진출할 수 있습니다."
        ),
        "건설": (
            "국가 기반시설 확충 및 도시 재개발, 스마트건설 기술 도입에 따라 건설 기술인의 역할은 더욱 중요해지고 있습니다. "
            "시공사, 감리사, 설계사무소, 공기업 등 건설 전반에서 진로가 열려 있습니다."
        ),
        "보건복지": (
            "보건의료 및 사회복지 분야는 고령화와 복지 수요 증가에 따라 꾸준한 수요가 있는 영역입니다. "
            "병원, 복지시설, 보건소, 공공기관 등에서 근무할 수 있으며, 전문성과 자격이 곧 경쟁력으로 이어집니다."
        ),
        "해양수산": (
            "해양 산업은 수산업, 항만 물류, 해기사 및 선박 운항과 관련된 전문성을 요구하며, 국가의 전략 산업 중 하나로 꼽힙니다. "
            "선사, 해양청, 수산관련 연구소, 항만공사 등에서 진출 기회를 가질 수 있습니다."
        ),
        "항공": (
            "항공산업은 정비, 운항, 공항관리 등 다양한 기술 인력 수요가 있으며, 특히 국제화에 따라 안전 및 품질 기준도 높아지고 있습니다. "
            "항공사, 공항공사, 항공기 제조사 등에서 커리어를 쌓을 수 있습니다."
        ),
        "소방": (
            "소방 분야는 재난 대응 역량과 기술력을 갖춘 인재를 필요로 하며, 국민 안전을 위한 중요한 역할을 담당합니다. "
            "소방청, 지방자치단체, 소방안전 전문기업 등에서 진출할 수 있습니다."
        ),
        "경찰": (
            "경찰 분야는 공공질서 유지 및 치안 확보에 기여하는 핵심 인력을 양성하는 영역으로, 지속적인 채용 수요가 있습니다. "
            "경찰청, 교통경찰, 사이버범죄 수사대 등 다양한 분야에서 활동할 수 있습니다."
        ),
        "회계세무": (
            "회계 및 세무 분야는 기업의 재무 건전성과 세무 리스크 관리에서 필수적인 역량으로, 전문성과 정직성이 요구됩니다. "
            "회계법인, 세무회계 사무소, 금융기관, 대기업 재무팀 등에서 활약할 수 있습니다."
        )
    }

    return domain_templates.get(field_name, "관련 분야에서 자격을 바탕으로 다양한 기술직 또는 관리직으로 진출이 가능합니다.")


def generate_outlook(cert_data: dict) -> str:
    name = cert_data.get("jmfldnm", "이 자격증")
    series = cert_data.get("seriesnm", "")
    agency = cert_data.get("examAgency", "")
    oblig = cert_data.get("obligfldnm", "")
    mdoblig = cert_data.get("mdobligfldnm", "")

    
    field = mdoblig or oblig or "기타"
    domain = f"{oblig} 및 {mdoblig}" if oblig and mdoblig else field

    
    intro = f"{name}는 {domain} 분야에서 활용되는 {series} 등급의 국가기술자격으로,"

    
    field_outlook = generate_outlook_by_field(field)

    
    agency_info = (
        f" 이 자격은 {agency}에서 시행되며, 해당 분야 공공기관이나 민간 산업체에서도 폭넓게 활용되고 있습니다."
        if agency else ""
    )

    
    future = " 또한 기술 변화에 맞춰 상위 자격 취득이나 연계 분야로의 진출이 유리합니다."

    
    raw = f"{intro} {field_outlook} {agency_info} {future}"

    return refine_sentence(raw)

cert = {
    "jmfldnm": "자동차정비기능사",
    "seriesnm": "기능사",
    "examAgency": "국토교통부",
    "obligfldnm": "기계",
    "mdobligfldnm": "자동차"
}

print(generate_outlook(cert))