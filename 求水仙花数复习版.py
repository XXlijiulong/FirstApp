def qiushuixianhua():
    a=eval(input("请输入一个数:"))
    b=a%10
    c=(a//10)%10
    d=a//100
    if(b*b*b+c*c*c+d*d*d==a):
        print("YES")
    else:
        print("NO")
def qiushuixianhua():
    a = []
    for i in range(100, 1000):
        b = i % 10
        c = (i // 10) % 10
        d = i // 100
        if (b ** 3 + c ** 3 + d ** 3 == i):
            a.append(i)
    return a


if __name__ == '__main__':
    print(qiushuixianhua())
    print(qiushuixianhua())


