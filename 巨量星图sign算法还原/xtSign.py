    def get_sign_params(oai):
        """核心算法还原"""
        salt = 'e39539b8836fb99e1538974d3ac1fe98'
        #这里举例两种params，其实已经够用了，使用前请替换达人或者主播的o_author_id为对应字符串
        params = [('o_author_id',oai), ('platform_source', '1'), ('platform_channel', '10'),
                    ('limit', '15'),
                    ('service_name', 'author.AdStarAuthorService'),
                    ('service_method', 'GetAuthorLatestItems'), ('sign_strict', '1')]
        params2 = [('o_author_id', oai), ('platform_source', '1'), ('platform_channel', '10'),
                      ('limit', '15'), ('only_ecom_live', 'only_ecom_live'),
                      ('service_name', 'author.AdStarAuthorService'),
                      ('service_method', 'GetAuthorLatestItems'), ('sign_strict', '1')]
        params.sort()
        sss = ''
        for i in params:
            sss += ''.join(list(i))
        sss += salt
        sign = 核心算法内容在群公告的text文件里，加我微信YotaGit拉你进群
        params.append(('sign', sign))
        params_data_dict = dict()
        for item in params:
            k = item[0]
            v = item[1]
            if k == v:
                if k == "recommend":
                    v = "true"
                else:
                    v = "false"
            params_data_dict[k] = v
        return params_data_dict

if __name__ == '__main__':
    author_id="某个达人或者主播的o_author_id"
    result = get_sign_params(author_id)
    print(result)