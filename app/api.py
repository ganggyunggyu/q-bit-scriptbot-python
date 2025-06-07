import os
import requests

from dotenv import load_dotenv

from xml_to_json import xml_to_json

load_dotenv()
SERVICE_KEY = os.getenv("SERVICE_KEY")

def get_ntq_schedule(jmcd: str):
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getJMList'
    params = {'serviceKey': SERVICE_KEY, 'jmcd': jmcd}
    res = requests.get(url, params=params)
    
    if res.status_code == 200:
        return xml_to_json(res.content)
    else:
        raise Exception(f"❌ API 오류: {res.status_code} - {res.text}")

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
    return xml_to_json(requests.get(url, params=params).content)

# info = get_ntq_info('0080')
# schedule = get_ntq_schedule('0510')

# print("🔍 자격 정보:", info)
# print("🗓️ 시험 일정:", schedule)

print(get_professional_qual_list())