from math import atan


def compute_population(t_1):
   # вычислить численность населения для года t по формуле
    N = (172/45) * arcctg
    arcctg = (3.14/2) - atan((2000-t_1)/45)
    return N


# ввести строку с перечисленными через пробел годами
line = input()

# преобразовать строку в список из строковых значений годов
years_str_list = line.split()


# вычислить количество элементов в списке
n = len(years_str_list)


# сформировать список years_list на основе years_str_list,
# преобразовав строковые значения в целые
years_list = [int(t) for t in years_str_list]

# создать список population_list, каждый элемент которого вычисляется
# функцией compute_population от соответсвующего года из списка years_list



# в цикле для каждого года вывести численность населения, для вывода использовать
# формат "%5d - %6.3f миллиард(ов)"
print("%5d - %6.3f миллиард(ов)" % (t, c))