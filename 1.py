url ='https://account.xiaomi.com/oauth2/authorize?skip_confirm=false&client_id=428135909242707968&pt=1&redirect_uri=https%3A%2F%2Fapi-mifit-cn.huami.com%2Fhuami.health.loginview.do&_hideSwitch=false&_locale=zh_CN&response_type=code&scope=1+16001+16002+20000+6000&_sas=true&userId=367456618&nonce=O2EcfZqubHwBmIEk&confirmed=true&from_login=true&sign=sN1oJdOzZnq5h2cRL9Mukda32WE%3D'
header ={
    'Host': 'account.xiaomi.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Passport/OAuthMIUI/20.6.18',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'X-Requested-With': 'com.xiaomi.account',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Faccount.xiaomi.com%2Fsts%2Foauth%3Fsign%3Dq0XlyqvJVn4Wi3Bo284txf%252BLyPg%253D%26followup%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Foauth2%252Fauthorize%253Fskip_confirm%253Dfalse%2526client_id%253D428135909242707968%2526pt%253D1%2526redirect_uri%253Dhttps%25253A%25252F%25252Fapi-mifit-cn.huami.com%25252Fhuami.health.loginview.do%2526_hideSwitch%253Dfalse%2526_locale%253Dzh_CN%2526response_type%253Dcode%2526scope%253D1%25252016001%25252016002%25252020000%2525206000%2526_sas%253Dtrue%26sid%3Doauth2.0&sid=oauth2.0&lsrp_appName=%E4%BD%BF%E7%94%A8%E5%B0%8F%E7%B1%B3%E5%B8%90%E5%8F%B7%E7%99%BB%E5%BD%95%24%7B%E5%B0%8F%E7%B1%B3%E8%BF%90%E5%8A%A8%7D%24&_customDisplay=20&scope=1%206000%2016001%2016002&_locale=zh_CN&_ssign=2%26V1_oauth2.0%26Q99AnOtTELVItwUWIM3cdYrVA4k%3D',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'deviceId=_d2jPOpqqfufDrNB; uLocale=zh_CN; JSESSIONID=aaaxuOZRQ5Rq9hQVcgZxx; tick=6311711253253605730; userId=367456618; pass_ua=web; _onetrack_cid=5edb1c19df1d84c45bbf91a71b38730a; _onetrack_st=1606304895926; passToken=V1:gWkX85p93R9b9HZlDknoic611Zmnu7ZFPZwHxSy39grfQOvJLuDCSpLZwBvxYFB9pwT01tF2Cdagh8VcELtLULJcyaFKtczF80+O4g5QBA3u6izsQkfd2OqhV1wI6y1+Xrx3N9BCEb2ge8INZ2saNb+H1v7q1DNMdsYJvrUDJEqhzigYTaIR1QkgDve697DLuv45IKjdQk5XlPEw4v+IoGOYBTTGPnRkCLaXSx40cekDNdxIy6b/RrDDMF1bmZqs4IEE9GRlX/TZ4RW1LPldNoqaPUl4GeDvcQ21NMUrxvo=; cUserId=H7uCz_wC2AV0Mduqf3godSUj6a8; cUserId=H7uCz_wC2AV0Mduqf3godSUj6a8; pExpireTime=0; passInfo=login-end; userName=185***028; oauth2.0_serviceToken=2.0&V1_oauth2.0&1:0aolYNLTAIfucVSDg33dDw:J7upos65KnakzBfrVb9sJYwbuG1vLnBkaH+mboQjb6EqBgkKvbe9FHcpLN6tn4CuglPs8NgE1o/TpaQkTjucYspfWHZD1vvC1G1gZMEycOaxxpiNysL8mQ2bqrsD5uAn0D8OU02F1QNs/TULhVj+WKyMWWRv3vJNSsaSg7kSd3DXrVNvE1SUguO30jF/TtWomZ3WRTPWK0J6u77Sv2wTj61zOhQQm6zlOimrfMmPQ09huYlMIlQa1IoCrGO5kjACH1mwRAmV1abtu64OmcxxZA==&xs+VRwCyy867DXQ/MXZtgg==; userId=367456618; oauth2.0_slh=MOprrFwc6LEGZbap0KmSDBV+XF0=; oauth2.0_ph=yi6qceOMGF1MzFIuvpCaYQ=='
}
r = requests.get(url=url, headers=header, allow_redirects=False)
print(r.text)
