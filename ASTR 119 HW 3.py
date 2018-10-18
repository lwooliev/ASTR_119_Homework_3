
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


x = np.linspace(0,2*np.pi,1000)

y = (5.5)*np.cos(2*x) + 5.5
z = 0.02*np.exp(x)
w = (0.25)*(x**2) + 0.1*np.sin(10*x)


# In[ ]:


plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,w)

plt.xlabel('Time in ASTR119')
plt.ylabel('Level of Awesomeness')

