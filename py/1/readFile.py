from base64 import *
if __name__ == '__main__':
    flag = ''
    with open(r'F:\study\CTF\access\access1.log','r') as f:
       lines = f.readlines()
       for line in lines:
           if "select%20flag%20from%20flllag" in line:
               if(line.find('377')!=-1):
                   target = line[line.find('))=')+3:line.find(',sleep')]
                   print(target)
                   flag+=chr(int(target))
               else:
                    pass
           else:
               pass

    print(b64decode(flag).decode('utf-8'))