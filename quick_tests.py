def modif_dict(dic, x):
    dic[x] = 0
    return dic

dic = {}

for i in range(100):
    dic = modif_dict(dic, i)
    
for i in range(100, 201):
    dic = modif_dict(dic, i)
