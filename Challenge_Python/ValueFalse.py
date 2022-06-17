val = [0, "", 'False', "0", [], False, None]

for v in val:
    print('**********************')
    print(v or False)
    print('**********************')