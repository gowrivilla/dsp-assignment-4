Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5]
>>> print(l)
[1, 2, 3, 4, 5]
>>> type(l)
<class 'list'>
>>> print(l[0])
1
>>> print(l[1:3])
[2, 3]
>>> print(l[-3])
3
>>> print(l[-3:-1])
[3, 4]
>>> print(l[3: ])
[4, 5]
>>> f=[6,9,7]
>>> print(l+f)
[1, 2, 3, 4, 5, 6, 9, 7]
>>> l.insert(1,10)
>>> print(l)
[1, 10, 2, 3, 4, 5]
>>> l.extend([9,7,88])
>>> print(l)
[1, 10, 2, 3, 4, 5, 9, 7, 88]
>>> l.append([22,44,55])
>>> print(l)
[1, 10, 2, 3, 4, 5, 9, 7, 88, [22, 44, 55]]
>>> l.remove(1)
>>> print(l)
[10, 2, 3, 4, 5, 9, 7, 88, [22, 44, 55]]
>>> del(l[0])
>>> print(l)
[2, 3, 4, 5, 9, 7, 88, [22, 44, 55]]
>>> print(l)
[2, 3, 4, 5, 9, 7, 88, [22, 44, 55]]
>>> l[0]=100
>>> print(l)
[100, 3, 4, 5, 9, 7, 88, [22, 44, 55]]
>>> l(1:5]=14,32
SyntaxError: invalid syntax
>>> l[1:3]=12
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    l[1:3]=12
TypeError: can only assign an iterable
>>> l[1]=123
>>> print(l)
[100, 123, 4, 5, 9, 7, 88, [22, 44, 55]]
>>> l[-1]=43
>>> print(l)
[100, 123, 4, 5, 9, 7, 88, 43]
>>> l[1:4]=[12]
>>> print(l)
[100, 12, 9, 7, 88, 43]
>>> l.sort()
>>> print(l)
[7, 9, 12, 43, 88, 100]
>>> l.sort(reverse=True)
>>> print(l)
[100, 88, 43, 12, 9, 7]
>>> print(l)
[100, 88, 43, 12, 9, 7]
>>> l2=l
>>> print(l2)
[100, 88, 43, 12, 9, 7]
>>> l2=l.copy()
>>> print(l2)
[100, 88, 43, 12, 9, 7]
>>> l.reverse()
>>> print(l)
[7, 9, 12, 43, 88, 100]
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l.count()
TypeError: count() takes exactly one argument (0 given)
>>> l.count(12)
1
>>> length(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    length(l)
NameError: name 'length' is not defined
>>> l.length(l)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l.length(l)
AttributeError: 'list' object has no attribute 'length'
>>> len(l)
6
>>> 