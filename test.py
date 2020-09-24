a = {'a':0.1,'b':0.3,'c':0.4,'d':0.5,'e':0.6}
res = []
for k,v in a.items():
    if v >= 0.4:
        print(k,v)
        res.append(k)
print(res)



