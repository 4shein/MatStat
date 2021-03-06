#!/usr/bin/env python
# coding: utf-8

# # Task_1

# Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# в колоде из 52 карт 13 крестей. Значит вероятность выпадения первой карты крестовой масти равна 13/52, во второй раз 12/51, в третий раз 11/50 и в четвертый раз 10/49. Так как события зависимые - 
# вероятности перемножаются

# In[9]:


c = 13/52 * 12/51 *11/50 * 10/49
c


# В колоде из 52 карт 4 туза, значит вероятность выпадения одного туза = 4/52

# In[11]:


a = 4/52
a


# # Task_2

# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

# Так как в коде нет повторяющихся цифр, из общего количества комбинаций кода следует исключить цифры 000, 111, 010, 020, 100 и т. п. Общее количество комибнаций равно

# In[14]:


n = 10*9*8
n


# Следовательно, вероятность с первой попытки угадать код равна

# In[16]:


с = 1/720
с


# # Task_3

# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

# Вероятность извлечения первой окрашенной детали 9/15, второй 8/14, третьей - 7/13. Так как события зависимые, вероятности перемножаются

# In[22]:


c = 9/15 * 8/14 * 7/13
c


# # Task_4

# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

# Вероятность купить выигрышный билет 2/100 = 1/50.

# In[29]:


c = (1/100)*2
c


# In[ ]:




