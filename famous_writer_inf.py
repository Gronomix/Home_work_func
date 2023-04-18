'''Напишите функцию, принимающую сведения об авторе (в виде произвольного списка именнованых аргументов)
и выводящая их на экран в указанном формате
 И.О. Фамилия (дата рождения - дата смерти) -краткая информация'''


def famous_writer(sep='.', **kwargs):
    n = kwargs['name'][0]
    p = kwargs['patr'][0]
    surname = kwargs['surname']
    birth = kwargs['birth']
    death = kwargs['death']
    krt = kwargs['krt']
    return f'{n}{sep}{p}{sep}{surname} ({birth} - {death}) - {krt}'
print(famous_writer(name='Лев', patr='Николаевич', surname='Tолстой', birth='09.09.1828', death='20.11.1920',
                    krt='Граф, политический деятель, писатель'))

