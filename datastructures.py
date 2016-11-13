
# coding: utf-8

# In[1]:

product_names = "prod1,prod2,prod3,prod4"
for i in product_names:
    print i


# In[2]:

product_names = "prod1,prod2,prod3,prod4"


# In[3]:

products = ['prod1','prod2','prod3','prod4']
for i in products:
    print i


# In[4]:

print products[0]


# In[5]:

products[1]


# In[6]:

products[2]


# In[7]:

l=['a','b','c','d','e','f']


# In[8]:

l[1:5]


# In[9]:

l[3]


# In[10]:

l[8]


# In[11]:

l[8:]


# In[12]:

l=[1,1.2,1+2j,[10,20,30,40,50],'python']


# In[13]:

l


# In[14]:

l[1]


# In[15]:

l[2]


# In[16]:

l[3]


# In[17]:

l[3][1]


# In[18]:

l=[10,20,30,40]
sum(l)


# In[19]:

l=[10,20,"python",1.2,"wert"]
sum(l)


# In[20]:

isinstance(123,int)


# In[21]:

isinstance(1.2,float)


# In[22]:

isinstance('pythoin',str)


# In[23]:

l


# In[25]:

l2=[10,20,30,40]
s =0
for i in l2:
    s=s+i
print s


# In[26]:

l = [10, 20, 'python', 1.2, 'wert']
s=0
for i in l:
    if isinstance(i,int) or isinstance(i,float):
        s=s+i
print s
        


# In[27]:

type(i)


# In[28]:

t=type(i)


# In[29]:

type(t)


# In[30]:

s="prod1,prod2,prod3,prod4"
s.split(',')


# In[31]:

s=raw_input("Enter numbers:")
print s


# In[33]:

l=s.split(',')


# In[34]:

l


# In[35]:

sum(l)


# In[36]:

l


# In[37]:

l.append('50')


# In[38]:

l


# In[39]:

tmp = []
for i in l:
    print i,type(i)


# In[40]:

tmp = []
for i in l:
    i=int(i)
    tmp.append(i)
print tmp


# In[41]:

sum(tmp)


# In[42]:

s=raw_input("Enter numbers separated by coma:")
print s
l = s.split(',')
tmp = []
for i in l:
    tmp.append(int(i))
print tmp
print sum(tmp)


# In[43]:

s=raw_input("Enter numbers separated by coma:")
print s
l = s.split(',')
tmp = []
for i in l:
    tmp.append(int(i))
print tmp
print sum(tmp)


# In[44]:

int("12.34")


# In[45]:

int(12.34)


# In[46]:

float("12.34")


# In[48]:

s=raw_input("Enter numbers separated by coma:")
print s
l = s.split(',')
tmp = []
for i in l:
    tmp.append(float(i))
print tmp
print sum(tmp)


# In[49]:

s=raw_input("Enter numbers separated by coma:")
print s
l = s.split(',')
tmp = []
for i in l:
    tmp.append(float(i))
print tmp
print sum(tmp)


# In[50]:

s=raw_input("Enter numbers separated by coma:")
print s
l = s.split(',')
print l


# In[51]:

l


# In[52]:

for i in l:
    print type(i)


# In[53]:

s=raw_input("Enter numbers separated by coma:")
print s
l = s.split(',')
tmp = []
for i in l:
    if i.isdigit():
        tmp.append(float(i))
print tmp
print sum(tmp)


# In[54]:

"python".isdigit()


# In[55]:

"pu123".isdigit()


# In[56]:

"12.34".isdigit()


# In[57]:

s=raw_input("Enter numbers separated by coma:")
print s
l = s.split(',')
tmp = []
for i in l:
    if i.isdigit():
        tmp.append(float(i))
print tmp
print sum(tmp)


# In[58]:

l=[1,2,3,4]
l1=[5,6,7,8]
print l+l1


# In[59]:

# write a prdgram to add tow lists
zip(l,l1)


# In[60]:

for i in zip(l,l1):
    print i


# In[61]:

for i in zip(l,l1):
    print i[0]+i[1]


# In[62]:

tmp = []
for i in zip(l,l1):
    tmp.append(i[0]+i[1])


# In[63]:

tmp


# In[64]:

l+l1


# In[65]:

l-l1


# In[66]:

l*l1


# In[67]:

l+12


# In[68]:

l-12


# In[69]:

l*2


# In[70]:

l*4


# In[ ]:

l=['p1','p3','p4']
p = raw_input("Enter product:")
print l+p


# In[71]:

['p1','p2','p3']+"p4"


# In[72]:

['p1','p2','p3']+["p4"]


# In[73]:

l=['p1','p3','p4']
p = raw_input("Enter product:")
print l+[p]


# In[74]:

l=[10,20,30,40,50]
l[1]=200


# In[75]:

l


# In[76]:

s="pytho program"
s[2]="s"


# In[77]:

s.replace('t','s')


# In[78]:

s


# In[79]:

s1 = s.replace('t','s')


# In[80]:

s1


# In[81]:

s


# In[82]:

l=[10,20,30,4]
l1=l.append(50)
print l1


# In[83]:

l


# In[84]:

s="python"
l=['p','y','t','h','o','n']
s1=s.replace('t','s')
l1 = l.append("python")
print s,s1
print l,l1


# In[ ]:



