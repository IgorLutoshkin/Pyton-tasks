"""Известны величины потребленной электроэнергии в некотором помещении  за
каждый месяц года. Месячная норма потребления электроэнергии
n кВт·ч , стоимость 1 кВт·ч в пределах нормы  a руб, и стоимость за
каждый 1 кВт·ч потребления электроэнергии сверх нормы  b руб.  Вычислите
суммарное потребление и стоимость электроэнергии за год.

Входные данные:
строка, в которой через пробел перечислены значения потребленной энергии 
за каждый месяц (целые числа);
месячная норма потребления n кВт·ч (целое число);
стоимость  1 кВт·ч в пределах нормы  a руб (вещественное число);
стоимость  1 кВт·ч сверх нормы  b руб (вещественное число).

Выходные данные:
суммарное потребление электроэнергии за год;
стоимость потребленной электроэнергии за год."""
# ввод данных
elektro= list(map(float, input().split()))
n,a,b =int(input()), float(input()), float(input())
#создаем два списка х= сумма в пределах нормы и у= сумма сверх нормы
x= [elektro[i]*a for i in range(len(elektro)) if elektro[i]<=n]
y= [((elektro[i]- n)*b +(n*a)) for i in range(len(elektro)) if elektro[i]>n] 
#вывод результата
print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (sum(elektro),sum(x)+sum(y) ))