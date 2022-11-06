triangle = int(input("Enter the size of the triangle of the stars to print: "))
print("Displaying", triangle, "row(s) of stars of the Triangle")
    
for line in range(triangle,0,-1):
    for j in range(triangle-line):
        print(" ", end="")
    for j in range(2*line-1):
        print("*", end="")
    print()    