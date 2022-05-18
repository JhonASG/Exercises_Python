# Mi propuesta de solución (quedo a medias)
'''
x = [6, 7, 1, 2, 1, 3, 4, 5]
y = [7, 8, 1, 3, 2, 1, 7, 3.7, 10]
new_list = list()       

def sub_list(listx,listy):
    
    if len(listx) < len(listy):
        for i in range (len(listy)):
            for n in range (len(listx)):
                if listx[n] == listy[i]:
                    new_list.append(listx[n])
    
    return new_list

print(sub_list(x, y))
'''
#Solución del profesor
x = [6, 7, 1, 2, 1, 3, 4, 5]
y = [7, 8, 1, 3, 2, 1, 7, 3.7, 10]

def sub_list(list_x, list_y):
    new_list = []

    for element in list_x:
        if element in list_y:

            new_list.append(element)

    return new_list


print(sub_list(x, y))
