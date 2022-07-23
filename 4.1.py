"""Семья из трех человек планирует поехать отдыхать из города А в город B.
 Можно полететь самолетом, а можно – на своей машине.
Билет на самолет на одного человека стоит k рублей туда и обратно. 
Автомобиль расходует 12 литров бензина на 100 км, а цена бензина –  p рублей
 за 1 литр. Расстояние от города А до В -  s км. Сколько рублей придется 
 заплатить за самую дешевую поездку на троих туда и обратно?

Входные данные:

стоимость билета на самолет (вещественное число);
цена бензина (вещественное число);
расстояние от города А до города В (вещественное число).
Выходные данные:

сумма самой дешевой поездки (вещественное число) или '"error", если введены ошибочные данные."""






k, p, s = (float(input())for _ in range(3))
if k<=0 or p<=0 or s<=0:
    print("error")
else: 
    c = 3 * k
    m = (0.12 * s * p)*2
    if c > m: print(round(m,2))    
    else: print(round(c,2))
    