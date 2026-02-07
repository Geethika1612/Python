Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[ :4]
'code'
a[4: ]
'gnan'
a="beautiful is better than ugly"
a[25:28]
'ugl'
a[25:29]
'ugly'
>>> a[25: ]
'ugly'
>>> a[13:19]
'better'
>>> a[0:9]
'beautiful'
>>> a[ :9]
'beautiful'
>>> b="simple is better than complex"
>>> b[22: ]
'complex'
>>> b[0:6]
'simple'
>>> b[17:21]
'than'
>>> a="python is easy"
>>> a[-14:-9]
'pytho'
>>> a[-14:-8]
'python'
>>> a[-7:-5]
'is'
>>> a[-4: ]
'easy'
>>> a[ :-8]
'python'
>>> b="every day is learning"
>>> b[ :-16]
'every'
>>> b[-15:-12]
'day'
>>> b[-11:-9]
'is'
>>> b[-8:-1]
'learnin'
>>> b[-8:0]
''
>>> b[-8: ]
'learning'
