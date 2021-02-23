#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle


# In[ ]:


turtle.forward(100)


# In[ ]:


turtle.done()


# In[ ]:


turtle.fillcolor("yellow")
turtle.circle(50)
turtle.done()


# In[ ]:


def tri():
    turtle.begin_poly()
    while len(turtle.get_poly())<=3:
        turtle.forward(100)
        turtle.left(120)
    turtle.done()

tri()
    


# In[ ]:


def square():
    turtle.begin_poly()
    while len(turtle.get_poly())<=4:
        turtle.forward(100)
        turtle.left(90)
    turtle.done()

square()


# In[2]:


def rect():
    turtle.begin_poly()
    while len(turtle.get_poly())<=4:
        if len(turtle.get_poly())==1 or len(turtle.get_poly())==3:
            turtle.forward(100)
        else:
            turtle.forward(200)
        turtle.left(90)
    turtle.done()

rect()


# In[ ]:




