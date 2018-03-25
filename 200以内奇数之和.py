def JishuTotal():
    s=0
    for i in range (1,200):
        if(i%2==1):
            s=s+i
    return s
if __name__ == '__main__':
    print("两百以内的奇数之和为:{}".format(JishuTotal()))
