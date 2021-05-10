
if __name__ == '__main__':
    # 不换行
    print('123123',end="")
    print('213')

    '''
    翻转
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    '''
    st = '1234'
    st = st[-1::-1]
    print(st)

    print(f'{1+2}')
    name = "ao"
    print(f'hello {name}')
    print(f'{1+1=}')

    list=['213','ao','mira']
    del list[1]
    print(list)
    for i in list:
        print(i)
    for i in range(5):
        print(i)
    for i in range(5,9):
        print(i)
    for i in range(0,10,3):
        print(i)
    list=range(11,5)
    print("================")
    print(list)
    for i in [1, 0]:
        print(i + 1)
    print('===================')
    list = ['213', 'ao', 'mira']
    it=iter(list)
    for x in it:
        print(it)
    print('==============')
    def f(ab,*,c):
        return ab+c
    b = f(1,c=1)
    print(b)
    print(dir())
    s = 'awewq'
    print('==============')
    print(str(s))
    print(repr(s))