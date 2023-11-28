s = input("inserire una stringa")
i = len(s)-1
def inverti(s, i):
   s2 = ""
   while i>=0:
       s2=s2+s[i]
       i=i-1
       return s2


print(inverti(s,i))