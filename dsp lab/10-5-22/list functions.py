Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5,6]
>>> print[l]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(l)
[1, 2, 3, 4, 5, 6]
>>> print(type(l))
<class 'list'>
>>> help(l)

>>> 
>>> l1=[4,5,6]
>>> l2=l1+[7,8,9]
>>> print(l2)
[4, 5, 6, 7, 8, 9]
>>> len(l2)
6
>>> l2.insert[1,3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l2.insert[1,3]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l2.extend(11,22,33)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l2.extend(11,22,33)
TypeError: extend() takes exactly one argument (3 given)
>>>  l2.extend([11,22,33])
 
SyntaxError: unexpected indent
>>> l2.extend([11,12,13])
>>> print(l2)
[4, 5, 6, 7, 8, 9, 11, 12, 13]
>>> len(l2)
9
>>> l2.append([16,17])
>>> print(l2)
[4, 5, 6, 7, 8, 9, 11, 12, 13, [16, 17]]
>>> l2.insert([1,2,3])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l2.insert([1,2,3])
TypeError: insert expected 2 arguments, got 1
>>> l2.insert(1,88888)
>>> print(l2)
[4, 88888, 5, 6, 7, 8, 9, 11, 12, 13, [16, 17]]
>>> l2.pop(2)
5
>>> print(l2)
[4, 88888, 6, 7, 8, 9, 11, 12, 13, [16, 17]]
>>> l2.push(0,10)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l2.push(0,10)
AttributeError: 'list' object has no attribute 'push'
>>> l2.push([0,10])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    l2.push([0,10])
AttributeError: 'list' object has no attribute 'push'
>>> l2.reverse()
>>> print(l2)
[[16, 17], 13, 12, 11, 9, 8, 7, 6, 88888, 4]
>>> l2.remove()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    l2.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> l2.remove(0)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l2.remove(0)
ValueError: list.remove(x): x not in list
>>> l2.remove([0])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l2.remove([0])
ValueError: list.remove(x): x not in list
>>> l2.remove[0]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l2.remove[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l2.remove(88888)
>>> print(l2)
[[16, 17], 13, 12, 11, 9, 8, 7, 6, 4]
>>> l2[0]=1
>>> print(l2)
[1, 13, 12, 11, 9, 8, 7, 6, 4]
>>> l2[1:3]=[70,30]
>>> print(l2)
[1, 70, 30, 11, 9, 8, 7, 6, 4]
>>> l2.sort()
>>> print(l2)
[1, 4, 6, 7, 8, 9, 11, 30, 70]
>>> l2.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    l2.sort(reverse=true)
NameError: name 'true' is not defined
>>> l2.sort[reverse=true]
SyntaxError: invalid syntax
>>> l2.sort[reverse]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    l2.sort[reverse]
NameError: name 'reverse' is not defined
>>> l2.reverse()
>>> print(l2)
[70, 30, 11, 9, 8, 7, 6, 4, 1]
>>> l2.count()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    l2.count()
TypeError: count() takes exactly one argument (0 given)
>>> l2.count([0,3])
0
>>> l2.count([0:3])
SyntaxError: invalid syntax
>>> l2.count([1,4])
0
