#Carly's Clippers on codecademy
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#Check point 1
total_price = 0
#Check point 2
for price in prices:
  total_price += price
#Check point 3
average_price = total_price/len(prices)
#Check point 4
print("Average Haircut Price:",average_price)
#Check point 5
new_prices = [neg_five - 5 for neg_five in prices]
#Check point 6
print(new_prices)
#Check point 7
total_revenue=0
#Check point 8 & 9
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
#Check point 10
print("Total Revenue:", total_revenue)
#Check point 11
average_daily_revenue=total_revenue/7
print ("Average daily revenue:",average_daily_revenue)
#Check point 12
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]< 30]
#Check point 13
print(cuts_under_30)