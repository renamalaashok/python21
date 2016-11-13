
# coding: utf-8

# In[2]:

s = raw_input("Enter a string:")
print s


# In[3]:

s = raw_input("Enter a string:")
if s:
    print s
else:
    print "not entered string"


# In[4]:

s = raw_input("Enter a string:")
if s:
    print s
else:
    print "not entered string"


# In[5]:

s = raw_input("Enter a string:")
if s:
    print s
else:
    print "not entered string"


# In[6]:

"python program".capitalize()


# In[7]:

"python PROgram".capitalize()


# In[8]:

"abcd".isalpha()


# In[9]:

"abc123".isalpha()


# In[10]:

"ahcg@#".isalpha()


# In[11]:

"python".upper()


# In[12]:

"PYTHON".upper()


# In[13]:

"123".upper()


# In[14]:

"".upper()


# In[15]:

s="python program"
print s.startswith('python')


# In[16]:

s="python program"
print s.startswith('p')


# In[17]:

s="python program"
print s.startswith('program')


# In[18]:

name="Anil"
age=23
height=5.6
# name: Anil, age: 23, height: 5.6
s="name: {0}, age: {1}, height:{2}".format(name,age,height)


# In[19]:

s


# In[20]:

f=10.2345678


# In[21]:

# cost: 10.23
s="cost: {0}".format(f)
print s


# In[23]:

# cost: 10.23
f=10.23789
s="cost: {0:.2f}".format(f)
print s


# In[24]:

"abcd".isupper()


# In[25]:

"ABCD".isupper()


# In[26]:

"abcDEF".isupper()


# In[27]:

s1="abcd"
s2="abcDEF"
s3="DEFGHT"


# In[28]:

s1.islower()


# In[29]:

s2.islower()


# In[30]:

s3.islower()


# In[ ]:

s=raw_input("Enter string:")
if s.islower():
    print "Doesn't contains capital letters"


# In[31]:

"qwe123".islower()


# In[32]:

"".islower()


# In[33]:

s=raw_input("Enter string:")
if s.islower():
    print "Doesn't contains capital letters"
else:
    print "contains capital letters"


# In[34]:

s=raw_input("Enter string:")
if s.islower():
    print "Doesn't contains capital letters"
else:
    print "contains capital letters"


# In[35]:

s=raw_input("Enter string:")
if s.islower():
    print "Doesn't contains capital letters"
else:
    print "contains capital letters"


# In[36]:

s=raw_input("Enter string:")
if s:
    if s.islower():
        print "Doesn't contains capital letters"
    else:
        print "contains capital letters"
else:
    print "Please enter data"


# In[37]:

"abc123".isalnum()


# In[38]:

"abc".isalnum()


# In[39]:

"123".isalnum()


# In[40]:

"abc123#".isalnum()


# In[41]:

s=raw_input("Enter string:")
if s:
    if s.isalnum():
        print "Doesn't contains special letters"
    else:
        print "contains special letters"
else:
    print "Please enter data"


# In[42]:

s=raw_input("Enter string:")
if s:
    if s.isalnum():
        print "Doesn't contains special letters"
    else:
        print "contains special letters"
else:
    print "Please enter data"


# In[43]:

s=raw_input("Enter string:")
if s:
    if s.isalnum():
        print "Doesn't contains special letters"
    else:
        print "contains special letters"
else:
    print "Please enter data"


# In[44]:

"abc123".isdigit()


# In[45]:

"1234".isdigit()


# In[46]:

"123$%".isdigit()


# In[47]:

box_size = 25
s="python program"
s.center(box_size)


# In[48]:

box_size = 10
s="python program"
s.center(box_size)


# In[50]:

s="python is pure object oriented program"
#sub = raw_input("Enter substring:")
s.count("python")


# In[51]:

s.count('p')


# In[52]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if s.count(sub)>0:
    print "Sub string is find"
else:
    print "substring is not find"


# In[53]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if s.count(sub)>0:
    print "Sub string is find"
else:
    print "substring is not find"


# In[54]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if s.count(sub)>0:
    print "Sub string is find"
else:
    print "substring is not find"


# In[55]:

s


# In[56]:

s.count('')


# In[57]:

len(s)


# In[58]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if sub:
    if s.count(sub)>0:
        print "Sub string is find"
    else:
        print "substring is not find"
else:
    print "please enter sub string"


# In[59]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if sub:
    if s.count(sub)>0:
        print "Sub string is find"
    else:
        print "substring is not find"
else:
    print "please enter sub string"


# In[60]:

s


# In[61]:

s.count("PYTHON")


# In[62]:

s


# In[63]:

s[0]


# In[64]:

s[1]


# In[65]:

s[-1]


# In[66]:

s[-2]


# In[67]:

s[-3]


# In[69]:

print s[0]+s[1]+s[2]+s[3]+s[4]+s[5]


# In[ ]:




# In[70]:

s


# In[71]:

s[0:6]


# In[72]:

s[0:3]


# In[73]:

s[2:6]


# In[74]:

s


# In[75]:

s[4:]


# In[76]:

s[:7]


# In[77]:

s[-6:-2]


# In[78]:

s[::-1]


# In[79]:

s[-3::-1]


# In[80]:

s[::-1]


# In[81]:

s[::-2]


# In[82]:

s[::1]


# In[83]:

s[::2]


# In[84]:

s[::3]


# In[85]:

s


# In[86]:

s[::-3]


# In[87]:

s[::1]


# In[88]:

s[::-1]


# In[89]:

s[::-2]


# In[90]:

s[::-3]


# In[91]:

len(s)


# In[92]:

s[6]


# In[93]:

s[10]


# In[94]:

s[1:4]


# In[95]:

s[39]


# In[96]:

len(s)


# In[97]:

s[39]


# In[98]:

s[39:]


# In[99]:

s[20:37]


# In[100]:

s[20:2]


# In[101]:

s[39:64]


# In[102]:

s[38]


# In[103]:

s[37]


# In[104]:

s[-1]


# In[105]:

s[37:40]


# In[106]:

len(s)


# In[107]:

s


# In[108]:

s.find("pure")


# In[109]:

s.index("pure")


# In[110]:

s.index('p')


# In[111]:

s.find('p')


# In[112]:

s.index('P')


# In[113]:

s.find('P')


# In[114]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if sub:
    if s.find(sub) != -1:
        print "Sub string is find"
    else:
        print "substring is not find"
else:
    print "please enter sub string"


# In[115]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if sub:
    pos = s.find(sub)
    if pos != -1:
        print "Sub string is find at:{0}".format(pos)
    else:
        print "substring is not find"
else:
    print "please enter sub string"


# In[116]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if sub:
    pos = s.find(sub)
    if pos != -1:
        print "Sub string is find at:{0}".format(pos)
    else:
        print "substring is not find"
else:
    print "please enter sub string"


# In[117]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if sub:
    pos = s.find(sub)
    if pos != -1:
        print "Sub string is find at:{0}".format(pos)
    else:
        print "substring is not find"
else:
    print "please enter sub string"


# In[118]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
if sub:
    pos = s.find(sub)
    if pos != -1:
        print "Sub string is find at:{0}".format(pos)
    else:
        print "substring is not find"
else:
    print "please enter sub string"


# In[119]:

s


# In[120]:

s.find("PYTHON")


# In[121]:

s


# In[122]:

s.upper()


# In[123]:

sub="pyTHON"


# In[124]:

sub.upper()


# In[125]:

s="python is pure object oriented program"
sub = raw_input("Enter substring:")
s_u = s.upper()
sub_u = sub.upper()
if sub:
    pos = s_u.find(sub_u)
    if pos != -1:
        print "Sub string is find at:{0}".format(pos)
    else:
        print "substring is not find"
else:
    print "please enter sub string"


# In[126]:

s


# In[127]:

s.count("PYTHON")


# In[128]:

s


# In[129]:

sub="PyThon"
s.count(sub)


# In[130]:

sub = sub.lower()


# In[131]:

sub


# In[132]:

s.count(sub)


# In[133]:

password = "sambapython"
password.encode("base64")


# In[134]:

password = "sambapython"
p_enc = password.encode("base64")
print p_enc
p= p_enc.decode("base64")
print p


# In[135]:

password = "sambapython"
p_enc = password.encode("base64")
print p_enc
p= p_enc.decode("ASCII")
print p


# In[136]:

s


# In[137]:

s.endswith('gram')


# In[138]:

s.endswith("python")


# In[143]:

s="pyton\tprogram\tis\tpure"


# In[144]:

print s


# In[145]:

s.expandtabs(5)


# In[147]:

"python program".isspace()


# In[148]:

"     ".isspace()


# In[149]:

s="python program"


# In[150]:

s.title()


# In[151]:

"python Program".istitle()


# In[152]:

"Python Program".istitle()


# In[153]:

"pytohn PROGRAM".title()


# In[154]:

s="python program"
s.ljust(25)


# In[155]:

s.rjust(25)


# In[157]:

s.ljust(25,'@')


# In[158]:

s.rjust(25,'#')


# In[159]:

username = "  user name123   "


# In[160]:

print username
print username.strip()


# In[162]:

username = "$#@user$#@name123#@$"
print username
print username.strip('$')


# In[163]:

username = "$#@user$#@name123#@$"
print username
print username.strip('$')
print username.strip('$#')


# In[164]:

username = "$#@user$#@name123#@$"
print username
print username.strip('$')
print username.strip('#$')
print username.strip('#$@')


# In[166]:

s


# In[167]:

s.replace('python','PYTHON')


# In[168]:

s


# In[169]:

s.find('p')


# In[170]:

s.rfind('p')


# In[171]:

"PYthon PRohram".swapcase()


# In[172]:

s="1234"
s.zfill(25)


# In[173]:

s


# In[174]:

s="python program"


# In[175]:

s.replace('p','')


# In[176]:

s="python program"
s[:6].replace('o','z')


# In[177]:

get_ipython().magic(u'pinfo s.replace')


# In[179]:

s.replace('o','z',1)


# In[180]:

s.replace('o','z')


# In[ ]:



