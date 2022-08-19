Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d=()
>>> type(d)
<class 'tuple'>
>>> d={ }
>>> type(d)
<class 'dict'>
>>> d[name]="pallavi"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d[name]="pallavi"
NameError: name 'name' is not defined
>>> d["name"]="pallavi"
>>> print(d)
{'name': 'pallavi'}
>>> d['r.no']='16'
>>> print(d)
{'name': 'pallavi', 'r.no': '16'}
>>> len(d)
2
>>> d['r.no']="64"
>>> print(d)
{'name': 'pallavi', 'r.no': '64'}
>>> d["class"]="d"
>>> print(d)
{'name': 'pallavi', 'r.no': '64', 'class': 'd'}
>>> del(d["name"])
>>> print(d)
{'r.no': '64', 'class': 'd'}
>>> d.popitem()
('class', 'd')
>>> d.pop("r.no")
'64'
>>> print(d)
{}
>>> d=dict9([(1,2),(3,4)])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d=dict9([(1,2),(3,4)])
NameError: name 'dict9' is not defined
>>> d=dict([(1,2),(3,4)])
>>> print(d)
{1: 2, 3: 4}
>>> d.keys()
dict_keys([1, 3])
>>> d.values()
dict_values([2, 4])
>>> d.get(1)
2
>>> d.clear()
>>> print(d)
{}
>>> 