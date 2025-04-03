#for i in range(15):
  #  print(i) 
#for i in range(1, 15):
  #  print(i)

car = 4
while car < 10:
    print(car)
    car += 1

print("Blast off! 🚀")

# Traditional loop
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]