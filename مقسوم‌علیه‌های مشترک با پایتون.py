x = int (input("x : "))
y = int (input("y : "))
m = min (x , y)

for i in range(1 ,m+1 ) :
    if x % i ==0 and y % i == 0:
        print(i)
