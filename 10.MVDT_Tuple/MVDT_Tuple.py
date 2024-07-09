Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=1,2,3,(([([('mnbvcxz',),'wonder']),'sticky note','controlling'],'nature',(10)))
t[3][0][0][0][0][1]
'n'
t[2]
3
t[3][0][0][0][0][0]
'm'
t[3][0][0][0][0][6]
'z'
t[3][0][0][1][0]
'w'
t[3][0][0][0][5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t[3][0][0][0][5]
IndexError: tuple index out of range
t[3][0][0][5]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t[3][0][0][5]
IndexError: list index out of range
t[3][0][0][1][5]
'r'
>>> t[3][0][1][0]
's'
>>> t[3][0][2][1]
'o'
>>> t[3][0][2][6]
'l'
>>> t[3][1][6]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t[3][1][6]
IndexError: string index out of range
>>> t[3][1][3]
'u'
>>> tu=('charge'),('mobile',),('question',),(('tuple is 89',90,112),([('secured')]87))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> tu=('charge'),('mobile',),('question',),(('tuple is 89',90,112),([('secured')],87))
>>> tu[0][0]
'c'
>>> tu[2][0][0]
'q'
>>> tu[3][1][0][0][3]
'u'
>>> tu[1][0][0]
'm'
>>> tu[3][0][0][2]
'p'
>>> tu[3][1][0][0][0]
's'
>>> tu[3][1][0][0][6]
'd'
>>> tu[3][0][0][0]
't'
>>> tu[3][0][0][10]
'9'
>>> tu[3][0][1]
90
>>> tu[3][1][1]
87
>>> tu[0][0][4]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tu[0][0][4]
IndexError: string index out of range
>>> tu[0][4]
'g'
>>> tu[2][0][4]
't'
>>> tu[3][0][0][5]
' '
>>> tu[3][1][0][4]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tu[3][1][0][4]
IndexError: list index out of range
>>> tu[3][1][0][0][4]
'r'
>>> tu[3][0][0][3]
'l'
