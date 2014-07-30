#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

In Python, what is the difference between bytes and string object?

En Python, ¿Cual es la diferencia entre un objeto bytes y string?
'''

# bytes objects are immutable sequences of integers, each value in the sequence
# restricted such that 0 <= x < 256, representations are based on ASCII text.
# string objects are immutable sequences of unicode characters.
s = 'hello world'
b = b'hello world'
print(s)
print(b)

# representation of characters found in unicode but not in ascii
s = 'cañon'
b = bytes('cañon', 'utf8')
print(s)
print(b)

# bytes objects provide almost all methods found on string objects, with the
# exceptions of str.isidentifier(), str.isnumeric(), str.isdecimal(),
# str.isprintable(), str.encode(), str.format(), str.format_map().
s = s.replace('ñ', 'scar')
b = b.replace(b'\xc3\xb1', b'mar')
print(s)
print(b)
