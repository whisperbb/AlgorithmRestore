
var crypto=require('crypto');
var md5=crypto.createHash("md5");

bbk = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
    "D": 13, "E": 14, "F": 15
}
hhh = [212, 45, 80, 68, 195, 163, 163, 203, 157, 220, 254, 91, 204, 79, 104, 6]
m = []
m_shit = []
dd_list = []
ss = ''
sss = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
function ack(a, b) {
    d = a * 16
    ii = d + b
    this.m.push(ii)
}
function find_the_map() {
    aae = []
    for (var i = 0; i < this.ss.length; i++) {
        aae.push(bbk[this.ss[i]])
    }
    for (var kk = 0; kk < aae.length; kk += 2) {
        ack(aae[kk], aae[kk + 1])
    }

}
function find_head() {
    find_the_map()
    hh = ''
    var hea=[21, 4, 9, 26, 16, 20, 27, 30]
    for (i in hea) {
        hh += this.ss[hea[i]]
    }
    return hh
}
function find_tail() {
    tt = ''
    tai=[18, 11, 3, 2, 1, 7, 6, 25]
    for (j in tai) {
        tt += this.ss[tai[j]]
    }
    return tt
}
function find_middle() {
    this.m_shit = []
    this.dd_list=[]
    for (var i = 0; i < this.hhh.length; i++) {
        var x = this.m[i];
        var y = this.hhh[i];
        this.m_shit.push(x ^ y)
    }
    for (var jjj = 0; jjj < this.m_shit.length; jjj += 3) {
        if (jjj + 3 < this.m_shit.length) {
            find_the_shit(this.m_shit[jjj], this.m_shit[jjj + 1], this.m_shit[jjj + 2])
        }
        else {
            var lll = this.m_shit.length - jjj
            if (lll == 2) {
                find_the_shit(this.m_shit[jjj], this.m_shit[jjj + 1])
            } else {
                find_the_shit(this.m_shit[jjj])
            }
        }
        
    }
    var middle=this.dd_list.join('').replace('/','')
    return middle
}
function find_the_shit(a, b, c){
    var aa = a >> 2
    var aaa = a & 3
    var aaa_a = aaa << 4
    if(b){
        var bb = b >> 4
        var bbb = aaa_a | bb
        var bbb_b = 5 + 10
        var bbb_bb = b & bbb_b
        var bbb_bbb = bbb_bb << 2
        if (c){
            var bbb_bbb_b = c >> 6
            var cc = bbb_bbb | bbb_bbb_b
            var ddd = 53 + 10
            var dd = c & ddd
            this.dd_list.push(this.sss[aa])
            this.dd_list.push(this.sss[bbb])
            this.dd_list.push(this.sss[cc])
            this.dd_list.push(this.sss[dd])}
        else{
            this.dd_list.push(this.sss[aa])
            this.dd_list.push(this.sss[bbb])}}
    else{
        算法内容在群公告的text文件里，加我微信YotaGit拉你进群
    }
}

function get_the_sign(ppk){
    this.ss = md5.update(ppk).digest('hex').toUpperCase();
    var head=find_head()
    var mid=find_middle()
    var tail=find_tail()
    ret = 'zzb' + head + mid+ tail
    return ret.toLowerCase()
}
ppp = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.musichallSinger.SingerList","method":"GetSingerListIndex","param":{"area":200,"sex":1,"genre":2,"index":1,"sin":0,"cur_page":1}}}'
result = get_the_sign(ppp)
console.log(result)