import sys
def palindroma(s):
   i=0
   j=len(s)-1
   for i in range(0,len(s)-1 ,1):
       if s[i] != s[j]:
           return False
       j=j-1
   return True                    
              
s1=sys.argv[1]
if(palindroma(s1)):
   print("la stringa è palindroma")
else:
   print("la stringa non è palindroma")