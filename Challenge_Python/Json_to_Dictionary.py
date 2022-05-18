import json

json_object = input()

dictionary = json.loads(json_object)

#Con load pasamos un objeto Json a un dictionario y con dump pasamos de un diccionario a un objeto Json
#Fuente para trabajar Json-Python: https://pywombat.com/articles/json-python

print(dictionary)