import random

list = []

#for i in range(1):
#    list.append(random.randint(1,12))
'''
while len(list)<24:
    n = random.randint(14,320)
    if n not in list:
       list.append(n)
'''
'''
while len(list) < 22:
    n = random.randint(321, 608)
    if n not in list:
        list.append(n)
'''
'''
while len(list) < 12:
    n = random.randint(609, 768)
    if n not in list:
        list.append(n)
'''

while len(list) < 61:
    n = random.randint(769, 1566)
    if n not in list:
        list.append(n)


print(list)