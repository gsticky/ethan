seoul = ['kim', 'jane', 'jin']
print(seoul)

#print(seoul[0])

def findKim():
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

a = findKim()

print(a)

