#!/usr/bin/env python
# coding: utf-8

# In[6]:


score={'gt':[20,'w','w','l','l','w'],'lsg':[18,'w','l','l','w','w'],'rr':[20,'w','w','l','l','w'],'dc':[14,'w','w','l','w','l'],'rcb':[14,'l','w','w','l','l'],'kkr':[12,'l','w','w','l','w'],'pbks':[12,'l','w','l','w','l'],'srh':[12,'w','l','l','l','l'],'csk':[8,'w','w','l','l','w'],'mi':[6,'l','w','l','w','w']}


# In[7]:


# code to find 2 consecutive losses
for each in score:
    for i in range(len(score[each])-1):
        if score[each][i] == score[each][i+1] == 'l':
            print(each,end=' ')
            break
            


# In[21]:


def find_n_consecutive(n,identifier):
    team_count=0
    point_count=0
    if identifier.lower()=='win':
        ind='w'
    else:
        ind='l'
    for each in score:
        s=score[each]
        i = 0
        while( i < len(s) - 1) :

            # Counting occurrences of s[i]
            count = 1

            while s[i] == s[i + 1] :

                i += 1
                count += 1

                if i + 1 == len(s):
                    break
            if count == n and s[i] == ind:
                print(each)
                team_count+=1
                point_count+= s[0]
                break
            i += 1
    
    print('Average = ',point_count/team_count )


# In[22]:


find_n_consecutive(2,'win')


# In[ ]:




