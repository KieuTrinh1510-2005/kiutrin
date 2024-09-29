# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:18:35 2024

@author: Student
"""

def tinh_tong_va_tich(*args, **kwargs):
    tong = 0 
    tich = 1
    for num in args:
        tong += num
        tich *= num
    if kwargs.get('mode') == 'tong':
        return tong
    elif kwargs.get('mode') == 'tich':
        return tich
    else:
        return {"tong": tong, "tich": tich}
print(tinh_tong_va_tich(1, 2, 3, 4))
print(tinh_tong_va_tich(1, 2, 3, 4, mode='tong'))
print(tinh_tong_va_tich(1, 2, 3, 4, mode='tich'))
