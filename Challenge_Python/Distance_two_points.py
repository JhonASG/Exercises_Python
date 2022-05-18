import math as m

punto1 = (10, 5)
punto2 = (4, 3)

difx = punto1[0] + punto2[0]
dify = punto1[1] + punto2[1]

hip = m.sqrt((m.pow(difx,2)+m.pow(dify,2)))

print(hip)