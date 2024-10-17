import lec_3_my_module  # импортирует информацию из lec_3_my_module

print(lec_3_my_module.a) # .a выписывает информацию из lec_3_my_module а (.a) говорит что именно нужно вывести 

b = lec_3_my_module.b * 3
print(b)

import lec_3_my_module as mm # as изменяет название (mm) само название (можно назвать как угодно)

print(mm.a)

from lec_3_my_module import a, b

print(a * b)
from lec_3_my_module import * # * копирует все атрибуты модуля 

print(c[2] * c[1])