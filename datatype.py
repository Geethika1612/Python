Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype
a=10
type(a)
<class 'int'>
>>> b=6.7
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e='python'
>>> type(e)
<class 'str'>
>>> y=5j+3
>>> type(y)
<class 'complex'>
>>> z=7j
>>> type(z)
<class 'complex'>
>>> b=j
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b=j
NameError: name 'j' is not defined
>>> c="j"
>>> type(c)
<class 'str'>
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> x=6+9j
>>> type(x)
<class 'complex'>
>>> x=true
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
