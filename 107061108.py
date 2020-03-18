#!/usr/bin/env python
# coding: utf-8

# In[174]:


# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061108.csv'
data = []
header = []
targeta = ['0']
counta=0
targetb = ['0']
countb=0
targetc = ['0']
countc=0
targetd = ['0']
countd=0
targete = ['0']
counte=0
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
#   for row in mycsv:
    #  data.append(row)
   temp = [row['TEMP'] for row in mycsv]    
with open(cwb_filename) as csfile:
   mcsv = csv.DictReader(csfile)
   header = mcsv.fieldnames 
   name = [row['station_id'] for row in mcsv]
   
#print (temp)
#print (name)
need_data = list (filter( lambda item:(item['TEMP'] != -99) and (item['TEMP'] != -990) and (item['station_id'] == 'C0A880')  , data))

for i in range(len(name)):
    if (name[i] == 'C0A880') :
        counta=counta+1
        targeta.append (temp[i])
a = max(targeta)
#print(targeta)
if(a == '0'):
    print("['C0A880', 'None']")
else:          
    print("['C0A880',",a,']')
#============================================
for i in range(len(name)):
    if (name[i] == 'C0F9A0') :
        countb=countb+1
        targetb.append (temp[i])
b = max(targetb)
if(b == '0'):
    print("['C0F9A0', 'None']")
else:          
    print("['C0F9A0',",b,']')   
#=======================================
for i in range(len(name)):
    if (name[i] == 'C0G640') :
        countc=countc+1
        targetc.append (temp[i])
c = max(targetc)
if(c == '0'):
    print("['C0G640', 'None']")
else:          
    print("['C0G640',",c,']')   
#=======================================
for i in range(len(name)):
    if (name[i] == 'C0R190') :
        countd=countd+1
        targetd.append (temp[i])
d = max(targetd)
if(d == '0'):
    print("['C0R190', 'None']")
else:          
    print("['C0R190',",d,']')   
#=======================================
for i in range(len(name)):
    if (name[i] == 'C0X260') :
        counte=counte+1
        targete.append (temp[i])
e = max(targete)
if(e == '0'):
    print("['C0X260', 'None']")
else:          
    print("['C0X260',",e,']')   
#=======================================
# Part. 3 C0F9A0, C0G640, C0R190, C0X260
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


    
#target_data = list (need_data)                 
# Retrive ten data points from the beginning.
#target_data = data[:10]  

#=======================================

# Part. 4
#=======================================
# Print result
#print(target_data)   
#========================================


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




