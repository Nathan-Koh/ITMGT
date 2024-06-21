#!/usr/bin/env python
# coding: utf-8

# In[24]:


def savings(gross_pay, tax_rate, expenses):
      
    return(((gross_pay-(gross_pay*tax_rate))//1)-expenses)
    


# In[25]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    
    return(str(total_material-(num_jobs*job_consumption))+material_units)


# In[26]:


def interest(principal, rate, periods):
  
    return((principal + principal*(rate*periods))//1)







