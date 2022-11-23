#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.write a python program to convert a string into a lower case
#2. write a python program to convert only odd a indexed character to lower case 
EX:PYTHON
Out put :PyThon
#3. write a python program to convert only even indexed to lower case
Ex:PYTHON
out put:pytHon


# In[4]:


x="INNOMATICS"
x.lower()


# In[5]:


x="innomatics"
x.upper()


# In[4]:


z="python"
x=" "
for str in range(len(z)):
    if str%2==0:
        x=x+z[str].upper()
    else:
        x=x+z[str].lower()
print(x)


# In[11]:


x="python"
y=" "
for str in range(len(x)):
    if str%2==0:
        y=y+x[str].lower()
    else:
        y=y+x[str].upper()
print(y)


# In[ ]:


#4. write a python program to convert only odd indexed characters to upper case
EX:python
output:pYtHoN


# In[56]:


a="python"
b=" "
for str in range(len(a)):
    if str%2!=0:
        b=b+a[str].upper()
    else:
        b=b+a[str]
print(b)


# #5.write a python program to convert only even indexed characters to uppercase
# Ex:-python
# Output:-PyThOn

# In[76]:


i="python"
j=" "
for str in range (len(i)):
    if str%2==0:
        j=j+i[str].upper()
    else:
        j=j+i[str]
print(j)


# In[ ]:


#6.write a python program where you have different variable which contains your name,sex,age,phone no,fathers name and mothers
name and using this variable create a variable named bio-data where you will use all this variable 
Ex:-print(bio-data)
output:-My name is.....,my sex is.....,My age is....,My phone no....,My father name....,and my mothers name is....


# In[9]:


name=input("type your name:")
sex=input("type your sex:")
age=input("type your age:")
phone_number=input("type your number:")
fathers_name=input("type your fathers_name:")
mothers_name=input("type your mothers_name:")
bio_data="my name is {},my sex is {},my age is {},my phone_number is {},my father_name is {},my mothers_name is {}"
bio_data.format(name,age,sex,phone_number,fathers_name,mothers_name)


# In[ ]:


#7.write a python program to count how many times "@"occured


# In[15]:


x="aaaabbbbcccddd@@@@eeee@@@@Aaaaa"
x.count("@")


# In[3]:


l=input("enter your list")
l.count("@")


# In[ ]:


#8.write a python to get only names from the string
"name1.@gmail.com,name2.gmail.com,name3.@gmail.com"


# In[5]:


s1="name1.@gmail.com,name2.@gmail.com,name3.@gmail.com"
s1=s1.split(".")
print(s1[0],s1[2][4:],s1[4][4:])


# In[ ]:


#9.Given a string of odd length greater that 9,return a new string made of the middle three characters of a given string
Ex:-mynameissan
output:-"mei"


# In[6]:


name=input("")
b=int(len(name)/2)
name[b-1:b+2]


# In[ ]:


# write a python program to insert a 2 string in the middle of 1 string


# In[5]:


str1=input("")
str2=input("")
print(str1[:len(str1)//2:]+str2+str1[len(str1)//2:])


# In[ ]:


#11.write a program to remove vowels from the entire alphabets


# In[6]:


vowels=["a","e","i","o","u","A","E","I","O","U"]
name=input()
a=""
for k in name:
    if k not in vowels:
        a+=k
print(a)


# In[ ]:




