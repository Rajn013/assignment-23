#!/usr/bin/env python
# coding: utf-8

# 1. What is the result of the code, and why?
# >>> def func(a, b=6, c=8):
# print(a, b, c)
# >>> func(1, 2)

# In[ ]:


The output of the code will be "1 2 8".


# In[ ]:


get_ipython().set_next_input('2. What is the result of this code, and why');get_ipython().run_line_magic('pinfo', 'why')
def func(a, b, c=5):
print(a, b, c)
func(1, c=3, b=2)


# In[ ]:


The output of the code will be "1 2 3".


# In[ ]:


get_ipython().set_next_input('3. How about this code: what is its result, and why');get_ipython().run_line_magic('pinfo', 'why')
def func(a, *pargs):
print(a, pargs)
func(1, 2, 3)


# In[ ]:


1 (2, 3)


# In[ ]:


get_ipython().set_next_input('4. What does this code print, and why');get_ipython().run_line_magic('pinfo', 'why')
def func(a, **kargs):
print(a, kargs)
func(a=1, c=3, b=2)


# In[ ]:


The output of the code will be "1" followed by a dictionary containing the keyword arguments passed to the function: {'c': 3, 'b': 2}.


# In[ ]:


get_ipython().set_next_input('5. What gets printed by this, and explain');get_ipython().run_line_magic('pinfo', 'explain')
def func(a, b, c=8, d=5): print(a, b, c, d)
func(1, *(5, 6))


# In[ ]:


The output of the code will be:

1 5 6 5


# In[ ]:


get_ipython().set_next_input('6. what is the result of this, and explain');get_ipython().run_line_magic('pinfo', 'explain')
def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'
l=1; m=[1]; n={'a':0}
func(l, m, n)
l, m, n


# In[ ]:


1, ['x'], {'a': 'y'}

