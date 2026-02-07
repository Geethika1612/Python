Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DATA TYPE CONVERSIONS
#INT
int(6)
6
int(7.8)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#float
float(2)
2.0
float(3.6)
3.6
float("hi")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(6+9j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(TRUE)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(TRUE)
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
>>> float("TRUE")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("TRUE")
ValueError: could not convert string to float: 'TRUE'
>>> 
>>> 
>>> #string
>>> str(3)
'3'
>>> str(3.5)
'3.5'
>>> str("abc")
'abc'
>>> str(abcd)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    str(abcd)
NameError: name 'abcd' is not defined
>>> str(1i+3j)
SyntaxError: invalid decimal literal
>>> str("TRUE")
'TRUE'
>>> str("FALSE")
'FALSE'
>>> 
>>> #COMPLEX
>>> complex(2)
(2+0j)
>>> complex(6.23)
(6.23+0j)
>>> complex("abcde")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex("abcde")
ValueError: complex() arg is a malformed string
>>> complex(2i+3j)
SyntaxError: invalid decimal literal
>>> complex(99i)
SyntaxError: invalid decimal literal
