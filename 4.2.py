"""Во многих странах очень популярным транспортом для передвижения по городу 
 является велосипед. А пользуются им так. Скачиваешь приложение на телефон, 
 видишь на улице велосипед, подходишь,  с помощью приложения открываешь замок,
 едешь, куда тебе нужно. Там оставляешь велосипед, закрываешь замок. 
 За поездку с тебя списываются деньги. Все просто и удобно.
  Но проблема "недобросовестных" пользователей, то есть тех, кто решил
  присвоить велосипед, была, есть и будет. Выявляют таких пользователей
  следующим образом: если замок на велосипеде открыт 
  более 12 часов – велосипед нужно срочно искать.

Написать программу, которая выводит номера всех велосипедов, 
которые открыты более 12 часов.

Входные данные:

строка, состоящая из значений, разделенных пробелами. Каждое значение
 либо 0, если велосипедом не пользуются, либо количество минут, 
 прошедших с момента открытия замка. Номер значения времени в списке 
 соответствует номеру велосипеда, нумерация начинается с 0.
Выходные данные:

номера велосипедов, которые открыты больше 12 часов, каждый номер 
вывести на отдельной строке."""

a= list(map(int, input().split()))
for i in range(len(a)) :
    if a[i] > 720:
        print(i)



























