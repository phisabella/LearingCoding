if __name__ == '__main__':
    with open('C:\\Users\\hexagram\\Desktop\\dictionary\\burpPass.txt', 'r+') as file:
        with open('C:\\Users\\hexagram\\Desktop\\dictionary\\burpPass2.txt', 'r+') as file1:
            while 1:
                line = file.readline().replace('\n', '')
                if not line:
                    break
                file1.write("\"" + line + "\"" + ","+"\n")
