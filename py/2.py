import mk

if __name__ == '__main__':
    def a():
        pass


    print(a.__globals__['__builtins__'].eval('1+1'))
    print(id(a))
    print(dir, ' ')
    print(globals())
    # print(a.__globals__['__builtins__']['__import__']['os'].pope('whoami').read())
    # print('class->__init__:', mk.cl.__init__.__globals__[ '__builtins__' ][ '__import__' ]( os ).popen('whoami').read())
    print(''.__class__.__bases__)
    print(''.__class__.__base__)
    print(''.__class__.__mro__)
    print('=======================')
    print(''.__class__.__base__.__subclasses__())
    print('=======================')
    '''
    下面我们就可以来依次判断这些类中是否定义__init__（或其他魔术方法）方法，
    如果定义，那么就可以拿到__init__（或其他魔术方法）下的__globals__[“__builtins__”]从而执行任意函数，编写脚本进行测试：
    '''
    # for i in ''.__class__.__base__.__subclasses__():
    #     try:
    #         # i.__sizeof__().__init__.__globals__['__builtins__']['__import__']('os').popen('whoami').read()
    #     except:
    #         pass
    '''
    我们可以通过普通数据类型的__class__成员属性得到所属类，
    再通过__bases__/__base__/__mro__可以得到object类，
    再次通过__subclasses__()来得到object下的所有基类，
    遍历所有基类检查是否存在指定的魔术方法，如果存在，
    那么即可获取__globals__[__builtins__]，就可以调用任意函数了。
    '''
    print('=====================')
    print(r'123\r/r')
    print('121231233\r/r')
