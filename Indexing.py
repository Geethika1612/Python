Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[4]
' '
a[7]
' '
a[1]+a[4]+a[7]
'   '
a="Vijayawada is a royal city"
a[22]+a[23]+a[24]+a[25]
'city'
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
>>> b="Vizag is a city of Destiny"
>>> b[19]+b[20]+b[21]+b[22]+b[23]+b[24]+b[25]+b[26]+b[27]+b[28]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b[19]+b[20]+b[21]+b[22]+b[23]+b[24]+b[25]+b[26]+b[27]+b[28]
IndexError: string index out of range
>>> a="Vizag is a city of Destiny"
>>> a[0]+a[1]+a[2]+a[3]+a[4]
'Vizag'
>>> a[19]+a[20]+a[21]+a[22]+a[23]+a[24]+a[25]
'Destiny'
>>> a[11]+a[12]+a[13]+a[14]
'city'
>>> a[16]+a[17]
'of'
>>> b="Andhra Pradesh"
>>> b[7]+b[8]+b[9]+b[10]+b[11]+b[12]+b[13]
'Pradesh'
>>> b[0]+b[1]+b[2]+b[3]+b[4]+b[5]
'Andhra'
>>> a="I am learning python"
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
>>> a[-15]+a[-14]+a[-13]+a[-12]+a[-11]+a[-10]+a[-9]+a[-8]
'learning'
>>> a[-18]+a[-17]
'am'
>>> a[-20]
'I'
>>> a="we are pretty"
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'pretty'
>>> a[-10]a[-9]+a[-8]
SyntaxError: invalid syntax
>>> a[-10]+a[-9]+a[-8]
'are'
>>> a[-13]+a[-12]
'we'
