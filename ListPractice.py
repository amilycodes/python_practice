# Len's Slice on codecademy
# Check point 1
toppings = [ "pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies","mushrooms"]
# Check point 2
prices = [2,6,1,3,2,7,2]
# Check point 3
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# Check point 4
num_pizzas = len(toppings)
# Check point 5
print("We sell", num_pizzas, "different kinds of pizza!")
# Check point 6 & 7
pizza_and_prices = [[2,"pepperoni"], [6,"pineapple"], [1,"cheese"],[3,"sausage"],[2,"olives"], [7,"anchovies"], [2,"mushrooms"]]
print(pizza_and_prices)
# Check point 8
pizza_and_prices.sort()
# Check point 9
cheapest_pizza = pizza_and_prices[0]
# Check point 10
priciest_pizza = pizza_and_prices[-1]
# Check point 11
pizza_and_prices.pop()
# Check point 12
pizza_and_prices.insert(-1, [2.5, "peppers"])
pizza_and_prices.sort()
# Check point 13
three_cheapest= pizza_and_prices[-3:]
# Check point 14
print(three_cheapest)