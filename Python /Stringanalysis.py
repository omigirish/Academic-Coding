s=list(input("Enter a string:"))
sc=[' ',':',';','=',')','(']
d1={}
def addchar(d1,c):
    d1.update({c:1})
def ischar(d1,c):
    t=0
    for i in d1.keys():
        if i==c:
            t=1
            return 1
        else:
            pass
    if t==0:
        return 0

def analyse(d1):
    for i in range(0,len(s)):
        if ischar(d1,s[i])==0:
            if s[i] in sc:   # ==' ':
                pass
            else:
                addchar(d1,s[i])
        else:
            d1[s[i]]=d1[s[i]]+1
analyse(d1)
print(d1)