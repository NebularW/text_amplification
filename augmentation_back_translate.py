# coding=utf8
import codecs
import requests
import hashlib
import random

appid = '20220505001204017'  # 你的appid
secretKey = 'VZFGzRLyTh2QofgKJEAI'  # 你的密钥


def fetch_data(input_file):
    """ Store each reference and candidate sentences as a list """
    input_string = ''
    reference_file = codecs.open(input_file, 'r', 'utf-8')
    for line in reference_file.readlines():
        input_string += line

    return input_string


def baidu_fanyi(query, from_lan='auto', to_lan='zh'):
    salt = random.randint(1, 10)  # 随机数
    code = appid + query + str(salt) + secretKey
    sign = hashlib.md5(code.encode()).hexdigest()  # 签名

    api = "https://api.fanyi.baidu.com/api/trans/vip/translate"

    data = {
        "q": query,
        "from": from_lan,
        "to": to_lan,
        "appid": appid,
        "salt": salt,
        "sign": sign
    }

    response = requests.post(api, data)

    try:
        result = response.json()
        dst = ''
        for trans_res in result.get("trans_result"):
            dst += trans_res.get("dst")
    except Exception as e:
        dst = query

    finally:
        return dst


if __name__ == '__main__':
    ini_file = '.\\text\\input.txt'
    ini = fetch_data(ini_file)
    en = baidu_fanyi(ini, from_lan='zh', to_lan='en')
    res = baidu_fanyi(en, from_lan='auto', to_lan='zh')
    print("这是原文件：\n")
    print(ini)
    out = open('.\\output\\back_translate.txt', 'w', encoding='utf-8')
    out.write(res)
    out.close()

