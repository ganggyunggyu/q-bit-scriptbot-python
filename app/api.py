import os
import requests

from dotenv import load_dotenv

from xml_to_json import xml_to_json
import json


load_dotenv()
SERVICE_KEY = os.getenv("SERVICE_KEY")


def get_ntq_schedule(jmcd: str):
    url = 'http://apis.data.go.kr/B490007/qualExamSchd/getQualExamSchdList'
    params = {
        'serviceKey': SERVICE_KEY,
        'numOfRows': '10',
        'pageNo': '1',
        'dataFormat': 'json',
        'implYy': '2025',
        'qualgbCd': 'T',
        'jmCd': jmcd
    }

    response = requests.get(url, params=params)
    decoded = response.content.decode('utf-8')
    parsed = json.loads(decoded)

    items = parsed.get('body', {}).get('items', [])
    for item in items:
        print(item.get('description'))

    return items
    

def get_ntq_info(jmCd: str):
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryInformationTradeNTQSVC/getList'
    params = {'serviceKey': SERVICE_KEY, 'jmCd': jmCd}
    res = requests.get(url, params=params)

    if res.status_code == 200:
        return xml_to_json(res.content)
    else:
        raise Exception(f"❌ API 오류: {res.status_code} - {res.text}")
    

def get_professional_qual_list():
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryListNationalQualifcationSVC/getList'
    params = {'serviceKey': SERVICE_KEY}
    result = requests.get(url, params=params).content

    return xml_to_json(result)

def get_professional_test_dates(seriesCd: str):
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestDatesNationalProfessionalQualificationSVC/getList'
    params = {'serviceKey': SERVICE_KEY, 'seriesCd': seriesCd}
    return xml_to_json(requests.get(url, params=params).content)

# info = get_ntq_info('9737')
# schedule = get_ntq_schedule('9737')

# print("🔍 자격 정보:", info)
# print("🗓️ 시험 일정:", schedule)

# print(get_professional_qual_list())

print(get_professional_test_dates('04'))
