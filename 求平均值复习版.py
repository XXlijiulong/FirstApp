def avg():
    a=eval(input("请输入一个数:"))
    b=eval(input("请输入另一个数:"))
    savg=(a+b)/2
    return savg
def avg1():
    a=eval(input("请输入一个数:"))
    s=0
    for i in range(a):
        score = eval(input("请输入分数:"))
        s=s+score
    return s/a


if __name__ == '__main__':
    #print(avg())
    print(avg1())