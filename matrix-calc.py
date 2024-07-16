#The purpose of this code is to perform calculations on given 2 matricesd depending on the user request.
#date n time :- 16-07-2024 21:36 Hrs   By- Ananda


def Add_matrix(a,b):
    mat1=[[0 for j in range(b)] for i in range(a)]
    mat2=[[0 for j in range(b)] for i in range(a)]
    res=[[0 for j in range(b)] for i in range(a)]
    print("Enter the elements of First Matrix: ")
    for i in range(a):
        for j in range(b):
            el=int(input("enter element:- "))
            mat1[i][j]=el
    print("Enter the elements of Second Matrix: ")
    for i in range(a):
        for j in range(b):
            el=int(input("enter element:- "))
            mat2[i][j]=el
    for i in range(a):
        for j in range(b):
            res[i][j]=mat1[i][j]+mat2[i][j]

    print("\n================================")
    print("Resulatant Matrix: ")
    for i in range(a): 
        for j in range(b):
            print(res[i][j], end=" ")  
        print("\n")
    print("\n================================================================")     
            

def Sub_matriix(a,b):
    mat1=[[0 for j in range(b)] for i in range(a)]
    mat2=[[0 for j in range(b)] for i in range(a)]
    res=[[0 for j in range(b)] for i in range(a)]
    print("Enter the elements of First Matrix: ")
    for i in range(a):
        for j in range(b):
            el=int(input("enter element:- "))
            mat1[i][j]=el
    print("Enter the elements of Second Matrix: ")
    for i in range(a):
        for j in range(b):
            el=int(input("enter element:- "))
            mat2[i][j]=el
    for i in range(a):
        for j in range(b):
            res[i][j]=mat1[i][j]-mat2[i][j]
    print("\n================================")
    print("Resulatant Matrix: ")
    for i in range(a):
        for j in range(b):
            print(res[i][j], end=" ")  
        print("\n")
    print("\n================================================================")

def multiply_matriix(a,b,c,d):
    mat1=[[0 for j in range(b)] for i in range(a)]
    mat2=[[0 for j in range(d)] for i in range(c)]
    res=[[0 for j in range(b)] for i in range(c)]
    print("Enter the elements of First Matrix: ")
    for i in range(a):
        for j in range(b):
            el=int(input("enter element:- "))
            mat1[i][j]=el
    for i in range(c):
        for j in range(d):
            el=int(input("enter element:- "))
            mat2[i][j]=el
    for i in range(c):
        for j in range(b):
            for k in range(d):
                res[i][j]+=mat1[i][k]*mat2[k][j]
    print("\n================================")
    print("Resulatant Matrix: ")
    for i in range(c):
        for j in range(b):
            print(res[i][j], end=" ")  
        print("\n")
    print("\n================================================================")


def transpose_matriix(a,b):
    mat1=[[0 for j in range(b)] for i in range(a)]
    res=[[0 for j in range(b)] for i in range(a)]
    for i in range(a):
        for j in range(b):
            el=int(input("enter element:- "))
            mat1[i][j]=el
    for i in range(a):
        for j in range(b):
            res[j][i]=mat1[i][j]
    print("\n================================")
    for i in range(a):
        for j in range(b):
            print(res[i][j], end=" ")  
        print("\n")
    print("\n================================================================")

    
print("Hello Human, Welcome to the MATRIX MANIACCESS...\n in this session you'll be making me do mathematical \nequations on  matrix just because you, as human, \ngot fedup of it.")
print("\n \n")
print("ALrihty, lets start..")
while True:
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Transpose\n5.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("youve chosen Addition:")
        r=int(input("Enter number of rows:  "))
        c=int(input("Enter number of columns:  "))
        Add_matrix(r,c)
    elif choice==2:
        print("You've chosen Subtraction:")
        r=int(input("Enter number of rows:  "))
        c=int(input("Enter number of columns:  "))
        Sub_matriix(r,c)
    elif choice==3:
        print("You've chosen Multiplication:")
        r1=int(input("Enter number of rows of first matrix:  "))
        c1=int(input("Enter number of columns of first matrix:  "))
        r2=int(input("Enter number of rows of second matrix:  "))
        c2=int(input("Enter number of columns of second matrix:  "))
        if c1!=r2:
            print("Matrices can't be multiplied as column of first matrix is not equal to row of second matrix.")
        else:
            multiply_matriix(r1,c1,r2,c2)
    elif choice == 4:
        print("You've chosen Transpose:")
        r=int(input("Enter number of rows:  "))
        c=int(input("Enter number of columns:  "))
        transpose_matriix(r,c)
    elif choice==5:
        print("Goodbye, Have a nice day!")
        break

print("==================================================")
print("==================================================")
print("==================================================")
print("==================================================")
