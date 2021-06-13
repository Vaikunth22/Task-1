Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #print string
>>> print('30 days 30 hours')
30 days 30 hours
>>> v='Taj Mahal'
>>> print(v)
Taj Mahal
>>> 
>>> #indexing string
>>> x='Eiffel Tower'
>>> print(x{2})
SyntaxError: invalid syntax
>>> print(x[2])
f
>>> print(x[4])
e
>>> #To print characters from string
>>> a='Vaikunth'
>>> print(a[3:7])
kunt
>>> 
>>> #converting uppercase and lowercase
>>> b='imagination'
>>> print(b.upper())
IMAGINATION
>>> print(b.lower())
imagination
>>> 
>>> #string concat
>>> c='Maruthi'
>>> d='Suzuki'
>>> print(a+b)
Vaikunthimagination
>>> 
>>> 
>>> print(f+g)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(f+g)
NameError: name 'f' is not defined
>>> print(c+d)
MaruthiSuzuki
>>> 
>>> #casefold() use
>>> w='The beSt SUpER CaR'
>>> w=text.casefold()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    w=text.casefold()
NameError: name 'text' is not defined
>>> y=w.textfold()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    y=w.textfold()
AttributeError: 'str' object has no attribute 'textfold'
>>> y=w.casefold()
>>> 
>>> g='SHE SELLS SEA SHELLS ON THE SEA SHORE'
>>> print(g.capitalize())
She sells sea shells on the sea shore
>>> print(g.title())
She Sells Sea Shells On The Sea Shore
>>> print(g.swapcase())
she sells sea shells on the sea shore
>>> 