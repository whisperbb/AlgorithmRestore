import re
from urllib.parse import unquote
from urllib3 import disable_warnings
import execjs
from requests import Session

disable_warnings()
session = Session()
with open('env.js', encoding='utf-8')as f:
    raw_js = f.read() + '\n!'
tail_js = """
function get_token(seed, ts) {
    return encodeURIComponent((new window.ABC).z(seed, parseInt(ts) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3))
}
"""
url = "https://www.zhipin.com/c101280100-p100101/?page=3&ka=page-3"

payload = {}
headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
count = 0
success = 0
while 1:
    try:
        session.headers = headers
        response = session.request("GET", url, data=payload, verify=False, timeout=3.0)
        # response = session.request("GET", url, data=payload, verify=False)
        local = response.history[0].headers.get('location')
        seed = unquote(re.findall('seed=(.*?)&', local)[0])
        ts = re.findall('ts=(.*?)&', local)[0]
        filename = re.findall('name=(.*?)&', local)[0]
        print(seed, ts)
        ak_url = "https://www.zhipin.com/web/common/security-js/{}.js".format(filename)
        response_ak = session.request("GET", ak_url, data=payload, verify=False, timeout=3.0)
        # response_ak = session.request("GET", ak_url, data=payload, verify=False)
        final_js = raw_js + response_ak.content.decode() + tail_js
        final_js = final_js.replace('module', 'moduler')
        final_js = final_js.replace('__filename', '__filenamer')
        final_js = final_js.replace('=Buffer', '=Bufferr')
        final_js = final_js.replace('typeof process', 'typeof child_process')
        final_js = re.sub('this===(.*?),', 'true,', final_js)
        ff = execjs.compile(final_js)
        zp_token = ff.call('get_token', seed, ts)
        cookie = {'__zp_stoken__': zp_token}
        print(zp_token)
        response = session.request("GET", url, data=payload, verify=False, cookies=cookie, timeout=3.0)
        # response = session.request("GET", url, data=payload, verify=False, cookies=cookie)
        count += 1
        if response.status_code == 200:
            if "当前IP存在多次违规访问行为，已暂时被禁止访问" in response.content.decode():
                print("当前IP存在多次违规访问行为，已暂时被禁止访问。")
                continue
            if "BOSS直聘" not in response.content.decode():
                print("BOSS直聘 not in response IP")
                continue
            success += 1
        print(count, success)
    except Exception as e:
        print(e)
