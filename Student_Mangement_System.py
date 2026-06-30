print("***** Student Management System *****")
print("--------------------------------------")
student = {}

try:
    with open("student.txt","r") as file:
        for line in file:
            name,marks = line.strip().split(",")
            student[name] =float(marks)

except FileNotFoundError:
    pass


while True:
    print("1.Add Student")
    print("2.Search Student") 
    print("3.View All Students")
    print("4.Delete Student")
    print("5.Calculate Average Marks")
    print("6.Assign Grades")
    print("7.Exit")

    try:
        choice = int(input("Enter your Choice :"))
    except ValueError:
        print("Invalid Choice")
        continue    

    match choice:
        case 1:
            name = input("Enter Name : ")
            try:
                marks = float(input("Enter Marks : "))
            except ValueError:
                continue

            student[name] = marks
            with open("student.txt","a") as file:
                file.write(f"{name},{marks}\n")
            print("Student Added Successfully\n")
        
        case 2:
            search = input("Enter name to Search : ")

            if search in student:
                print(f"{search} : {student[search]}\n")
            else:
                print("Name Not Found!\n")    

        case 3:
            print("---------STUDENTS---------")
            if len(student)==0:
                print("No Student Available\n")
            else:
                    for name,marks in student.items():
                        print(f"{name}:{marks}")
            print()  

        case 4:
            delete = input("Enter name to delete : ")
            if delete in student:
                del student[delete]

                with open("student.txt","w") as file:
                    for name,marks in student.items():
                        file.write(f"{name},{marks}\n")

            else:
                print("Name Not Found!") 

        case 5:
            if len(student)==0:
                print("No Data Available")
            else:    
                average = sum(student.values())/len(student)
                print(f"The Average sum of marks is {average}\n")

        case 6:
            if len(student) == 0:
                print("Data Unavailable!")

            else:
                for name,marks in student.items():

                    if marks>=90:
                        grade = 'A'  
                    elif marks>=80:
                        grade = 'B'
                    elif marks>=70:
                        grade = 'C'
                    else:
                        grade = 'D'

                    print(f"NAME : {name} , Mark : {marks} , Grade : {grade}")
  
        case 7:
            print("Fully Updated!!")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-")
            break

        case _:
            print("Invalid choice!")    

