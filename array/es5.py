import sys
s1=''
for s in range(len(sys.argv)):
   if s != 0:
       s2=sys.argv[s]
       s1=s1+s2  
print(s1) 