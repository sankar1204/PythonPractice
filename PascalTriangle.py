print("I am gonna print pascal triangle of size of your choice");
print("Please enter an integer");

size = int(input());

count = 1;

for i in range(size):    
    for j in range(count):
        print("*", end =" ")
    count = count + 1;
    print(" ");