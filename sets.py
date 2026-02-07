Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sets
#sets()
a = {3,5.6,"python",5+9j,True,False}
print(a)
{False, True, (5+9j), 3, 'python', 5.6}
type(a)
<class 'set'>
a={4,8,9,2,3,9,4}
print(a)
{2, 3, 4, 8, 9}
#issubset{}
a = {1,2,3,7,8,9}
b = {7,8,9}
b.issubset(a)
True
a.issubset(b)
False
#issuperset()
a={4,5,6,7,8,9}
b={6,7,8,9}
a.issuperset(a)
True
b.issuperset(b)
True
b.issuperset(a)
False
#setunion{}
#merging of 2 sets
a={5,6,7,8,9}
b={1,2,3,4,5,6,7}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#intersection
#common elements
a = {2,3,4,5}
b = {3,4,5,6}
b = {3,4,5,6}
a.intersection(b)
{3, 4, 5}
b.intersection(a)
{3, 4, 5}
a={2,3,4,5,6,7,8}
b={1,2,3,4,5,6,7}
a.difference(b)
{8}
b.difference(a)
{1}
#setupdate
a={3,4,5,6,7,8}
b={1,2,3,5,7,9,11,13}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13}
#symmetric_difference
#deletes common elements from sets
a = {45,18,7}
b = {33,8,01,45,18,7}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a = {23,33,44,55,66,77,88}
b = {77,88,99,22}
a.symmetric_difference(b)
{33, 66, 99, 44, 23, 22, 55}
b.symmetric_difference(a)
{33, 66, 99, 44, 23, 22, 55}
b
{88, 99, 77, 22}
a={4,5,6,,8,9,10}
SyntaxError: invalid syntax
#difference_update
#returns only different values from both the sets
a = {2,4,6,8,10,12}
b = {1,2,4,6,8}
a.difference_update(b)
a
{10, 12}
b.difference_update(a)
b
{1, 2, 4, 6, 8}
#intersection_update
#returns common elements from both sets
a={5,6,7,8,9}
b={2,3,4,5,6,7}
a.intersection_update(b)
a
{5, 6, 7}
b.intersection_update(a)
b
{5, 6, 7}
a
{5, 6, 7}
b
{5, 6, 7}
#symmetric_difference_update
#deletes duplicate values and returns remmaining values
a={2,3,4,5,6,7}
b={1,2,3,4,5,6,7,8}
a.symmetric_difference_update(b)
a
{1, 8}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7}
a
{1, 8}
b
{2, 3, 4, 5, 6, 7}
#pop
#deletes 1st element
#pop should be empty
a={2,3,4,5}
a.pop()
2
aa
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    aa
NameError: name 'aa' is not defined. Did you mean: 'a'?
a
{3, 4, 5}
#remove
#to delete a specific index val from list
a=
SyntaxError: invalid syntax
a={2,3,4,5,6}
a.remove(3)
a
{2, 4, 5, 6}
#copy
>>> #to copy values from one set to other
>>> a={2,3,4,5,6}
>>> a.copy()
{2, 3, 4, 5, 6}
>>> b=a.copy()
>>> b
{2, 3, 4, 5, 6}
>>> #clear
>>> #deletes all the values
>>> #deletes all the values
>>> a.clear()
>>> 
>>> a = {2,3,4}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(50)
>>> b
{50}
>>> #count,index will not work on sets
>>> a={2,3,4,5}
>>> len(a)
4
>>> #disjoints
>>> #2 sets should have opposite values
>>> a={1,2,3,4,5,6}
>>> b={7,6,10,11,2}
>>> a.isdisjoint(b)
False
>>> a={1,2,3}
>>> b={4,5,6}
>>> b.isdisjoint(a)
True
>>> 
>>> b
{4, 5, 6}
