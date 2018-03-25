from random import*
def Bigbaicai():
    quan=(eval)(input("请输入0(石头)1(剪刀)2(布):"))
    computer=randint(0,3)
    print("你输入的值是:{}".format(quan))
    print("电脑输入的值是:{}".format(computer))
    if (quan==computer):
        print("you are equals")
    elif((quan==1 and computer==2)or(quan==2 and computer==0) or(quan==0 and computer==1)):
        print("you are winner")
    else:
        print("you are loser")
def Isprime(b):
    a=[]
    for i in range(2,b):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            a.append(i)
    return a
def shuixianhua(a,b):
    l=[]
    for i in range(a,b):
        z=i%10
        x=(i//10)%10
        y=i//100
        if(z**3+x**3+y**3==i):
            l.append(i)
    return l
def Steal():
    day=9
    n=1
    for i in range(9):
        n=(n+1)*2
    return n
if __name__=='__main__':
    print(Steal())
    print(Isprime(100))
    print(shuixianhua(100,1000))
    Bigbaicai()