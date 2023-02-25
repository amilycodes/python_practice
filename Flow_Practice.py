#Sal's shipping on codecademy
weight= 41.5
cost=0.0
#Ground Shipping
if weight <= 2:
  cost = 1.50
elif weight >2 and weight <= 6:
  cost = 3.00
elif weight >6 and weight <= 10:
  cost = 4.00
elif weight > 10:
  cost = 4.75
else:
  print("Error")
print("Ground Shipping $", weight*cost+20)

premium_cost = 125.00
print("Ground Shipping Premium $",premium_cost)

#Drone Shipping
if weight <= 2:
  cost = 4.50
elif weight >2 and weight <= 6:
  cost = 9.00
elif weight >6 and weight <= 10:
  cost = 12.00
elif weight > 10:
  cost = 14.25
else:
  print("Error")
print("Drone Shipping $", weight*cost)