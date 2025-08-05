def right_side_pyramid(size):
    n = size

    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print() #here u can give "\n" in print statement it provide a space in each line.....!   

size = int(input("Enter the size of pyramid that u Want to genrate--> "))
right_side_pyramid(size)