#emoty list store name 
students = []
#gettig the number of tudents 
num=int(input("enter the name of student that will enroll "))
# filling in with students names 
for i in range (num):
    name = input(f"enter name{i+1} ")
    students.append(name)
#printing the originl list 
print("list of students is")
print(students)
#printing the sorted list using sorted function 
print(" sorted list is ")
print(sorted(name ))
#finding the number of students using len 
print(f"totle number of student is {len(students)}")
#removing a giving name 
remove=input("enter a name to remove" )
if remove in name:
    students.remove(remove)
# printing the list after remove 
    print(f"the list after removing{remove}is ")
    print(students)
else :
    print("the giving name was not found ")
