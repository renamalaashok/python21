
# coding: utf-8

# In[1]:

10>20


# In[2]:

"10"<"20"


# In[3]:

"10"<"2"


# In[4]:

"sub" in "substring"


# In[5]:

a=10
b=10.0


# In[6]:

id(a)


# In[7]:

id(b)


# In[8]:

a is b


# In[9]:

a==b


# In[10]:

bool(a==b)


# In[11]:

bool(a is b)


# In[12]:

bool(0)


# In[13]:

bool(-10)


# In[14]:

bool(10)


# In[15]:

bool(1)


# In[16]:

bool("")


# In[17]:

bool("'sdfsdf")


# In[18]:

bool("0")


# In[19]:

bool([])


# In[20]:

bool([""])


# In[21]:

a=10
b=20
c=30


# In[22]:

a<b and b<c


# In[23]:

a<b or b>c


# In[24]:

name="Anil"
age=23
height = 5.6
print name,age,height


# In[25]:

# name: Anil, age: 23, height: 5.6
print "name:"


# In[28]:

print "name:"+name


# In[29]:

print "name: "+name


# In[30]:

# name: Anil, age: 23, height: 5.6
print "'name: "+name,"age:"+age,"hheight:"+height


# In[32]:

# name: Anil, age: 23, height: 5.6
print "name: "+name,"age:"+str(age),"hheight:"+str(height)


# In[33]:

# name: Anil, age: 23, height: 5.6
print "name: "+name,", age:"+str(age),", height:"+str(height)


# In[34]:

# name: Anil, age: 23, height: 5.6
print "name: "+name+", age:"+str(age)+", height:"+str(height)


# In[35]:

# format specifiers
# %s %d %f %r
print "%s%d%f"


# In[36]:

print "line1, line2"


# In[37]:

print "line1"
print "line2"


# In[38]:

print "line1\nline2"


# In[39]:

print "%s%d%f",(name,age,height)


# In[40]:

print "%s%d%f"%(name,age,height)


# In[41]:

print "%d%s%f"%(name,age,height)


# In[45]:

# name: Anil, age: 23, height: 5.6
print "name: "+name+", age: "+str(age)+", height: "+str(height)
print "name: %s, age: %d, height: %f"%(name,age,height)


# In[46]:

print "name: %r, age: %r, height: %r"%(name,age,height)


# In[47]:

# let's go for ride today
print 'let's go for ride today'


# In[48]:

# let's go for ride today
print 'let\'s go for ride today'


# In[49]:

print "let's go for ride today"


# In[50]:

print 'let"s go for ride today'


# In[51]:

print 'let"s go for\' ride" today'


# In[52]:

print "line1\nline2"


# In[53]:

print "line1\\nline2"


# In[54]:

s="line1\nline2\ttab\ndsfsdfs\tsdfsdf\ndsfsdf\t"
print s


# In[55]:

s="line1\\nline2\\ttab\\ndsfsdfs\\tsdfsdf\\ndsfsdf\\t"
print s


# In[56]:

s=r"line1\nline2\ttab\ndsfsdfs\tsdfsdf\ndsfsdf\t"
print s


# In[57]:

a=raw_input("Enter a value:")
b=raw_input("Enter b value:")
print a+b


# In[59]:

a=raw_input("Enter a value:")
print "a>10:",a>10
if a>10:
    print "value is greaterthan 10"
else:
    print "value is lessthan 10"
    


# In[60]:

a=raw_input("Enter a value:")
print "a>10:",a>10
if a>10:
    print "value is greaterthan 10"
else:
    print "value is lessthan 10"
    


# In[62]:

a=raw_input("Enter a value:")
print "%s<10:"%(a),a<10
if a<10:
    print "value is lessthan 10"
else:
    print "value is greaterthan 10"


# In[63]:

a=raw_input("Enter a value:")
print "%s<10:"%(a),a<10
if a<10:
    print "value is lessthan 10"
else:
    print "value is greaterthan 10"


# In[64]:

"5"<10


# In[67]:

a=raw_input("Enter a value:")
a=int(a)
print "%d<10:"%(a),a<10
if a<10:
    print "value is lessthan 10"
else:
    print "value is greaterthan 10"


# In[68]:

print "program started"
a=raw_input("Enter a value:")
a=int(a)
print "%d<10:"%(a),a<10
if a<10:
    print "if block started"
    print "value is lessthan 10"
    print "if block ended"
else:
    print "else block started"
    print "value is greaterthan 10"
    print "else block ended"
print "other stsements in program"
print "program ended"


# In[69]:

print "program started"
a=raw_input("Enter a value:")
a=int(a)
print "%d<10:"%(a),a<10
if a<10:
 print "if block started"
 print "value is lessthan 10"
 print "if block ended"
else:
  print "else block started"
  print "value is greaterthan 10"
print "else block ended"
print "other stsements in program"
print "program ended"


# In[70]:

print "program started"
a=raw_input("Enter a value:")
a=int(a)
print "%d<10:"%(a),a<10
if a<10:
 print "if block started"
  print "value is lessthan 10"
 print "if block ended"
else:
  print "else block started"
  print "value is greaterthan 10"
print "else block ended"
print "other stsements in program"
print "program ended"


# In[71]:

print "program started"
a=raw_input("Enter a value:")
a=int(a)
print "%d<10:"%(a),a<10
if a<10:
    print "if block started"
    print "value is lessthan 10"
    print "if block ended"
else:
    print "else block started"
    print "value is greaterthan 10"
print "else block ended"
print "other stsements in program"
print "program ended"


# In[72]:

"""
1.windwos
2.linux
3.mac
"""
print "1.windows\n2.linux\n3.mac"


# In[73]:

"""
1.windwos
2.linux
3.mac
"""
print "1.windows\n2.linux\n3.mac"
opt = raw_input("Enter an option:")
if opt == '1':
    print "selected windows"
if opt =="2":
    print "selected linux"
if opt == "3":
    print "selected mac"


# In[74]:

"""
1.windwos
2.linux
3.mac
"""
print "1.windows\n2.linux\n3.mac"
opt = raw_input("Enter an option:")
if opt == '1':
    print "selected windows"
if opt =="2":
    print "selected linux"
if opt == "3":
    print "selected mac"


# In[75]:

"""
1.windwos
2.linux
3.mac
"""
print "1.windows\n2.linux\n3.mac"
opt = raw_input("Enter an option:")
if opt == '1':
    print "selected windows"
if opt =="2":
    print "selected linux"
if opt == "3":
    print "selected mac"


# In[76]:

"""
1.windwos
2.linux
3.mac
"""
print "1.windows\n2.linux\n3.mac"
opt = raw_input("Enter an option:")
if opt == '1':
    print "selected windows"
if opt =="2":
    print "selected linux"
if opt == "3":
    print "selected mac"
else:
    print "wrong option"


# In[80]:

"""
1.windwos
2.linux
3.mac
"""
print "program started"
print "1.windows\n2.linux\n3.mac"
opt = raw_input("Enter an option:")
if opt == '1':
    print "selected windows"
if opt =="2":
    print "selected linux"
if opt == "3":
    print "selected mac"
else:
    print "wrong option"
print "other statements in python program"
print "program ended"


# In[81]:

"""
1.windwos
2.linux
3.mac
"""
print "program started"
print "1.windows\n2.linux\n3.mac"
opt = raw_input("Enter an option:")
if opt == '1':
    print "selected windows"
elif opt =="2":
    print "selected linux"
elif opt == "3":
    print "selected mac"
else:
    print "wrong option"
print "other statements in python program"
print "program ended"


# In[82]:

"""
1.windwos
2.linux
3.mac
"""
print "program started"
print "1.windows\n2.linux\n3.mac"
opt = raw_input("Enter an option:")
if opt == '1':
    print "selected windows"
elif opt =="2":
    print "selected linux"
elif opt == "3":
    print "selected mac"
else:
    print "wrong option"
print "other statements in python program"
print "program ended"


# In[83]:

# check whether user given data or not
a=raw_input("Enter:")


# In[ ]:

print "program started"
c=0
while c<10:
    print c
print "other statement in program"
print "program ended"


# In[84]:

print "program started"
c=0
while c<10:
    print c
    c=c+1
    
print "other statement in program"
print "program ended"


# In[85]:

print "program started"
c=0
while c<10:
    c=c+1
print c
print "other statement in program"
print "program ended"


# In[87]:

print "program started"
c=0
for c in "python program":
    print c
print "other statement in program"
print "program ended"


# In[88]:

print "program started"
c=0
for c in "python program":
    print "iteration started"
    print c
    print "iteration ended"
print "other statement in program"
print "program ended"


# In[89]:

print "program started"
for c in "python program":
    print "iteration started"
    print c
    print "iteration ended"
print "other statement in program"
print "program ended"


# In[90]:

print "program started"
for c in "python program":
   print ""
print c
print "other statement in program"
print "program ended"


# In[91]:

print "program started"
c=0
while c<10:
    print "iter started"
    if c>5:
        break
    print c
    c=c+1
    print "iter ended"
print "other statement in program"
print "program ended"


# In[92]:

print "program started"
c=0
while c<10:
    break
    print "iter ended"
print c
print "other statement in program"
print "program ended"


# In[93]:

print "program started"
c=0
while c<10:
    print c
    c=c+1
    continue
print "other statement in program"
print "program ended"


# In[94]:

print "program started"
c=0
while c<10:
    print "iteration started"
    c=c+1
    if c==5:
        continue
    print c
    print "iteration ended"

print "other statement in program"
print "program ended"


# In[95]:

print "program started"
for i in "python program":
    continue
    print i
print "other statement in program"
print "program ended"


# In[96]:

print "program started"
for i in "python program":
    continue
print i
print "other statement in program"
print "program ended"


# In[97]:

print "program started"
for i in "python program":
    break
print i
print "other statement in program"
print "program ended"


# In[98]:

def fun():
    print "this is function"


# In[99]:

fun()


# In[102]:

print "program started"
def fun1(a,b):
    print "a=%d,b=%d"%(a,b)
    print a+b
print "function calling"
fun1(100,200)
print "function call completed"
print "other statements in program"
print "program ended"


# In[103]:

def fun(a,b,c):
    print a,b,c
fun(100,200,300)


# In[104]:

def fun(a,b,c):
    print a,b,c
d=fun(100,200,300)
print d


# In[105]:

def fun(a,b,c):
    print a,b,c
    a=a+100
    b=b+100
    c=c+100
    print a,b,c
    return 1000
d=fun(100,200,300)


# In[106]:

def fun(a,b):
    print 10000
    print 20000
    return a+b
c=fun(100,200)
print c


# In[107]:

def fun(a,b):
    print 10000
    print 20000
c=fun(100,200)
print c


# In[ ]:



