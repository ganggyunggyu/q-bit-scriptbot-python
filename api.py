import os
import requests

from dotenv import load_dotenv

from xml_to_json import xml_to_json
import json

from parser import parse_items


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



# 국가 기술자격 시험 일정 조회
def get_기술사():
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getPEList'
    params ={'serviceKey' : SERVICE_KEY }

    response = parse_items(requests.get(url, params=params).content)
    return response

def get_기능장():
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getMCList'
    params ={'serviceKey' : SERVICE_KEY }

    response = parse_items(requests.get(url, params=params).content)
    return response

def get_기사_산업기사():
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getEList'
    params ={'serviceKey' : SERVICE_KEY }

    response = parse_items(requests.get(url, params=params).content)
    return response

def get_기능사():
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getCList'
    params ={'serviceKey' : SERVICE_KEY }

    response = parse_items(requests.get(url, params=params).content)
    return response

def get_종목별_응시_수수료(jmcd):
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getFeeList'
    params ={'serviceKey' : SERVICE_KEY, 'jmcd' : jmcd }

    response = parse_items(requests.get(url, params=params).content)
    return response

