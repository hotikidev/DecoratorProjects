#================Decorator Project=================#
def decorator1(func):
    def wrapper():
        print('hello1')
        func()
        print('hello2')
    return wrapper


def decorator2(func):
    def wrapper():
        print('hello3')
        func()
        print('hello4')
    return wrapper


def decorator3(func):
    def wrapper():
        print('hello5')
        func()
        print('hello6')
    return wrapper


def decorator4(func):
    def wrapper():
        print('hello7')
        func()
        print('hello8')
    return wrapper


@decorator1
@decorator2
@decorator3
@decorator4
def play():
    print('hello9')


play()

#================OK now another model !! lets have it.

def printoneto50(func):
    def startit():
        for i in range(1, 51):
            print(i)
        func()

    return startit


@printoneto50
def play():
    pass


play()

#=================OK another one!!============

def welcome(func):
    def startit():
        name = input('Enter your name: ')
        print('Welcome dear', name)
        func()

    return startit


@welcome
def play():
    pass


play()


#=================OK another one!!============

def decorator(func):
    def wrapper():
        print('I ate chocolate number 1!')
        func()
        print('I ate chocolate number 2!')

    return wrapper

def decorator2(func):
    def wrapper2():
        print('I ate chocolate number 3!')
        func()
        print('I ate chocolate number 4!')

    return wrapper2
def decorator3(func):
    def wrapper3():
        print('I ate chocolate number 5!')
        func()
        print('I ate chocolate number 6!')

    return wrapper3
def decorator4(func):
    def wrapper4():
        print('I ate chocolate number 7!')
        func()
        print('I ate chocolate number 8!')

    return wrapper4
def decorator5(func):
    def wrapper5():
        print('I ate chocolate number 9!')
        func()
        print('I ate chocolate number 10!')

    return wrapper5
@decorator
@decorator2
@decorator3
@decorator4
@decorator5

def play():
    print('DONE!!')
play()

