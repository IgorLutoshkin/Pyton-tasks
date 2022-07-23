def compute_payment(t, s, n, k):
    pay= s/n+(s-(t-1)* s/n)* k/(12*100)
    return pay

t=1
s=int(input("s="))
n=int(input("n="))
k=int(input("k="))
if n<=0 or s<=0 or k<=0:
    print("Ошибка ввода данных")
    
else:
    t_list= [t+i for i in range(0,n)]
    list_pay=[compute_payment(t, s, n, k) for t in t_list]
    
    for t in range(len(list_pay)):
        print("|%2d месяц - %6.2f руб|" % (t_list[t], list_pay[t]))
    a=sum(list_pay)-s
    print("Доход банка - %6.2f руб" % a)
    