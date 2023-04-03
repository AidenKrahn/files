#not failing
#aiden krahn

file = open('requiem.txt', 'r+')#open file

print(file.read())#read file

add = input("What do you have to comment on this?  ")#get input

file.write(add)#add input

file.close()#close

filepart2 = open('requiem.txt', 'r')#open the edited file

print(filepart2.read())#read it out

print("\nYour thoughts are noted.")
