#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""Даны 2 строки long_phrase и short_phrase. Напишите код, который проверяет действительно ли длинная фраза 
long_phrase длиннее короткой short_phrase. 
И выводит True или False в зависимости от результата сравнения."""

long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
if len(long_phrase) > len(short_phrase):
    test_result=True
else: 
    test_result=False
print(test_result)


# In[47]:


""""Дана строка text. Определите какая из двух букв встречается в нем чаще - 'а' или 'и'.
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'"""

a_count = 0
i_count = 0
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
for very_letter in text:
    if very_letter == 'а':
        a_count += 1
    elif very_letter == 'и':
        i_count += 1 
if a_count > i_count:
    print ('буква "а" встречается чаще')
elif a_count < i_count:
    print ('буква "и" встречается чаще')
else:
    print ('буква "а" и буква "и" встречаются в тексте с одинаковой частотой')


# In[25]:


""""Дано значение объема файла в байтах. Напишите перевод этого значения в мегабайты в формате:
'Объем файла равен 213.68Mb'"""

byte_size = int(input('Введите размер файла в битах: '))
print ('Объем файла равен ', round(byte_size/1050578, 2),'Mb')


# In[48]:


""""Выведите на экран значение синуса 30 градусов с помощью метода math.sin."""

print(math.sin((30/180)*math.pi))


# In[49]:


""""В прошлом задании у вас скорее всего не получилось точного значения 0.5 из-за конечной точности вычисления синуса. 
Но почему некоторые простые операции также могут давать неточный результат? 
Попробуйте вывести на экран результат операции 0.1 + 0.2"""
   
print(0.1+0.2)


# In[98]:


""""В переменных a и b записаны 2 различных числа. 
Вам необходимо написать код, который меняет значения a и b местами 
без использования третьей переменной."""

a = int(input('Введите число а = '))
b = int(input('Введите число b = '))
print('Сперва число a =',a,'и число b =',b, end="\n")
print('Теперь число a =',b,'и число b =',a, end="\n")
print('Решение:', end="\n")
a = a + b
print('a = a + b =',a, end="\n")
b = a - b
print('b = b - a =',b, end="\n")
a = a - b
print ('a = a - b =',a)


# In[97]:


"""Дано число в двоичной системе счисления: num=10011. 
Напишите алгоритм перевода этого числа в привычную нам десятичную систему счисления."""

num = 10011
num_ch = str(num)
num_degree = 0
ten_num = 0
for n in num_ch[::-1]:
    ten_num += ((int(n) * 2) ** num_degree)
    num_degree +=1
print (ten_num)

