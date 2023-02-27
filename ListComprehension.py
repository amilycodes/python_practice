# Check point 1
single_digits = [0,1,2,3,4,5,6,7,8,9]
# Check point 3
squares=[]
# Check point 2
for i in single_digits:
  print(i)
  # Check point 4
  squares.append(i**2)
# Check point 5
print(squares)
# Check point 6
cubes =  [sd**3 for sd in single_digits]
# Check point 7
print(cubes)