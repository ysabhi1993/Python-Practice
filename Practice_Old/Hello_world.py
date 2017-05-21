from math import *

def compute_radians(a):
    radians = a * 2 * pi/360
    return radians

def compute_sin(b,a):
    text = input('print the expected result:\n')
    c = b(a)
    d = sin(c)
    if (d > 0):
        print(text)
        print('sin of the angle is = ',round(d,4))
    else:
        print('the computed angle is negative')

compute_sin(compute_radians,90)

#def conv_BtoD(a):
 #   d = len(a)

def count_down(n,count):
    if (n <= 0):
        print('blast off!')
    else:
        print(n)
        count = count + n
        print(count)
        count_down(n-1,0)

count_down(3,0)