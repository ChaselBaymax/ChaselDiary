def Multiplication_table():#打印输出9*9乘法表
        for i in range (0,10) :
                for j in range (1,i+1):
                        print (j,'*',i,"=",i*j,end="\t")#print中，默认以换行符\n做结尾，end=" "是让print以“”中内容代替\n作结尾
                print('\n')
Multiplication_table()
