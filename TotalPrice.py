#Full Name: Kevin T Le

#Student ID: 2406054

#Chapman Email: kevle@chapman.edu

#Course Number and Section: CPSC 230-07

#Programming Assignment 2: Conditionals; Exercise #1

#Purpose: This program calculates and outputs the total price of a purchase item, given the price and the sales tax rate.

#The program does not accept negative values, but will accept 0.

print("\n\nThis program calculates and outputs the total price of a purchase item, given the price\nand the sales tax rate.\n")

#User enters the Item Price
item_price = float(input("Enter the item purchase price: \n \n"))

sales_tax_rate = 0

#Item Price Conditions
if item_price < 0:
    print("\nError: The item price cannot be a negative. Please restart the program.\n")
    exit()
elif item_price == 0:
    print("\nThe total price of the item is: $0.\n") #The Item Price is $0 when they enter "0".
    exit()
else:
    sales_tax_rate = float(input("\nEnter the sales tax rate in percentage: \n \n")) #User enters Sales Tax Rate.

#Sales Tax Rate Conditions
if sales_tax_rate < 0:
    print("\nError: The sales tax rate cannot be negative. Please restart the program.\n") #Will add "0" for Sales Tax if there is no Sales Tax.
    exit()

#Calculation and Output of Total Price
total_price = item_price + ((sales_tax_rate * 0.01) * item_price)

print("\nThe total price of the item is: \n \n$" '{:.2f}'.format(total_price))

print()
