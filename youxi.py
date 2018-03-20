'''
Heroes beta-0.1
Kaelin
2017-09-01
'''
hp = 100
print('welcome Heroes world!')
print("| the world is like this ##### , 'a' for left, 'd' for right |")
name = input('input you name:')

if not name:
	name = 'player1'
usermsg = [name,hp]

print("your hero's name is :",usermsg[0], 'hp is :' , usermsg[1])
print("and now you are here : *####' | 'a' for left, 'd' for right |") 


userinput = input()
if userinput == 'd':
	print("your are here #*###")
if userinput == 'a':
    print("your are here *####")

print("测试修改")
