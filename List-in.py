#!/usr/bin/env python
# coding: utf-8

# In[5]:


#week 01 task
numbers = [1,2,3,4]
print("List:", numbers)


# In[6]:


new_number = int(input("Enter a value to add in list: "))
numbers.append(user_input)
print("List after appending the user input value:", my_list)


# In[7]:


value_to_check = int(input("Enter a value to check if it is in the list: "))
if value_to_check in numbers:
    print(f"{value_to_check} is in the list.")
else:
    print(f"{value_to_check} is not in the list.")


# In[9]:


old_num = int(input("Enter the value to be updated: "))
new_num = int(input("Enter the new value: "))

if old_num in numbers:
    index = numbers.index(old_num)
    numbers[index] = new_num
    print(f"{old_num} has been updated to {new_num} in the list. Now the list is {numbers}")
else:
    print(f"{old_num} is not in the list.")


# In[10]:


value_to_remove = int(input("Enter a value to remove from the list: "))
if value_to_remove in numbers:
    numbers.remove(value_to_remove)
    print(f"{value_to_remove} has been removed from the list. Now the list is {numbers}")
else:
    print(f"{value_to_remove} is not in the list.")


# In[ ]:




