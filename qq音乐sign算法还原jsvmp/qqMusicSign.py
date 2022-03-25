from hashlib import md5

bbk = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
       "D": 13, "E": 14, "F": 15}
hhh = [212, 45, 80, 68, 195, 163, 163, 203, 157, 220, 254, 91, 204, 79, 104, 6]
ss = ''
sss = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
m = list()
dd_list = list()
m_s = list()


def ack(a, b):
    d = a * 16
    ii = d + b
    m.append(ii)


def find_the_map():
    global m
    m = list()
    aae = list(map(lambda x: bbk.get(x), ss))
    for kk in range(0, len(aae), 2):
        ack(aae[kk], aae[kk + 1])


def find_head():
    find_the_map()
    hh = ''
    for i in [21, 4, 9, 26, 16, 20, 27, 30]:
        hh += ss[i]
    return hh


def find_tail_shit():
    tt = ''
    for i in [18, 11, 3, 2, 1, 7, 6, 25]:
        tt += ss[i]
    return tt


def find_middle():
    global dd_list
    dd_list = list()
    global m_s
    m_s = list(map(lambda x, y: x ^ y, m, hhh))
    for jjj in range(0, len(m_s), 3):
        if jjj + 3 < len(m_s):
            find_the(*tuple(m_s[jjj:jjj + 3]))
        else:
            find_the(*tuple(m_s[jjj:len(m_s)]))

    middle = ''.join(dd_list).replace('/', '').replace('+', '')
    return middle


def find_the(a, b=None, c=None):
    aa = a >> 2
    aaa = a & 3
    aaa_a = aaa << 4
    if b:
        bb = b >> 4
        bbb = aaa_a | bb
        bbb_b = 5 + 10
        bbb_bb = b & bbb_b
        bbb_bbb = bbb_bb << 2
        if c:
            bbb_bbb_b = c >> 6
            cc = bbb_bbb | bbb_bbb_b
            ddd = 53 + 10
            dd = c & ddd
            dd_list.append(sss[aa])
            dd_list.append(sss[bbb])
            dd_list.append(sss[cc])
            dd_list.append(sss[dd])
        else:
            dd_list.append(sss[aa])
            dd_list.append(sss[bbb])
    else:
        算法内容在群公告的text文件里，加我微信YotaGit拉你进群


def get_the_sign(ppk):
    global ss
    ss = md5(ppk.encode()).hexdigest().upper()
    ret = 'zzb' + find_head() + find_middle() + find_tail_shit()
    return ret.lower()


if __name__ == '__main__':
    ppp = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.musichallSinger.SingerList","method":"GetSingerListIndex","param":{"area":200,"sex":1,"genre":2,"index":1,"sin":0,"cur_page":1}}}'
    result = get_the_sign(ppp)
    print(result)
