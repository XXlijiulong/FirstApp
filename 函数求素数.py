num = []
def qiusushu(a,b):
    for i in range(a,b):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            num.append(i)
    return num
if __name__ == '__main__':
    print(qiusushu(100,200))

