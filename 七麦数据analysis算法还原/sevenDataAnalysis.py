def ack(a):
    e = 算法内容在群公告的text文件里，加我微信YotaGit拉你进群
    t = len(e)
    n = len(a)
    a = list(a)
    for sa in range(n):
        a[sa] = chr(ord(a[sa]) ^ ord(e[(sa + 10) % t]))
    return "".join(a).encode()

def get_analysis(url, params):
    i = int(time.time() * 1000) - 1865 - 1515125653845
    s = [str(value) for value in params.values()]
    s = ''.join(sorted(s))
    s = base64.encodebytes(s.encode("utf8"))
    s = s.decode("utf8").strip()
    s += "@#" + url.replace("https://api.qimai.cn", '')
    s += "@#" + str(i)
    s += "@#1"
    abc = ack(s)
    s = base64.encodebytes(abc)
    s = s.decode("utf8").strip()
    return quote(s)

if __name__ == '__main__':
    uuu='your target url'
    ppp = 'your params'
    result = get_analysis(uuu,ppp)
    print(result)