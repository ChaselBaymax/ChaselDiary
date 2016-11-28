import time
def main():#主函数
    try:
        n =int(input("please input a natural number for Hanoi："))
        a="A"
        b="B"
        c="C"
        speed = 0.5#单位：秒
        calculate(n,a,b,c)
    except:
        print("ValueError, please check your input")
        main()
def calculate(n,a,b,c):#算法函数，计算n阶(A是初始柱，B是过渡柱，C是目标柱)
    if n > 1:#递归调用
        calculate(n-1,a,c,b)
        delay_print(a,c)
        calculate(n-1,b,a,c)
    elif n == 1:
        delay_print(a,c)
def delay_print(m,n):#用以控制输出速度
    time.sleep(speed)
    print(m,"-->",n)
main()#开始
