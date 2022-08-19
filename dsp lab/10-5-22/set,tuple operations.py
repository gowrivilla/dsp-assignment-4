Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=(3,4,5)
>>> print(s)
(3, 4, 5)
>>> type(s)
<class 'tuple'>
>>> s1=[1,2,3]
>>> print(S)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(S)
NameError: name 'S' is not defined
>>> print[s]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print[s]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(s1)
[1, 2, 3]
>>> type(s1)
<class 'list'>
>>> s2={3,6,5}
>>> print(s2)
{3, 5, 6}
>>> type(s2)
<class 'set'>
>>> help(s)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> print(s)
(3, 4, 5)
>>> type(s)
<class 'tuple'>
>>> x=list(t)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x=list(t)
NameError: name 't' is not defined
>>> x=list(s)
>>> type(s)
<class 'tuple'>
>>> tuple(s)
(3, 4, 5)
>>> tuple(x)
(3, 4, 5)
>>> type(x)
<class 'list'>
>>> x[0]=888
>>> print(x)
[888, 4, 5]
>>> print(s)
(3, 4, 5)
>>> t=tuple(x)
>>> print(t)
(888, 4, 5)
>>> s1={2,4,6}
>>> print(s1)
{2, 4, 6}
>>> type(s2)
<class 'set'>
>>> help(s)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> print(s1)
{2, 4, 6}
>>> s2={3,7,8}
>>> print{s2}
SyntaxError: invalid syntax
>>> print(s2)
{8, 3, 7}
>>> s1.union(s2)
{2, 3, 4, 6, 7, 8}
>>> s2.union(s1)
{2, 3, 4, 6, 7, 8}
>>> s1.intersection(s2)
set()
>>> s1.difference(s2)
{2, 4, 6}
>>> s2.difference(s1)
{8, 3, 7}
>>> s1.update((5,6,7))
>>> print(s1)
{2, 4, 5, 6, 7}
>>> s1.difference_update(s2)
>>> print(s1)
{2, 4, 5, 6}
>>> s1.issubset(s2)
False
>>> s2.subset(s1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s2.subset(s1)
AttributeError: 'set' object has no attribute 'subset'
>>> s2.issubset(s1)
False
>>> 