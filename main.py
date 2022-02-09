"""
 - Discount Calculator
 - Malachi lang and Tequin Lake
 - Date: 10/2/2022
 - MVP:
   - https://www.programiz.com/python-programming/methods/string/lower

   - Write a program that takes an original price and calculates a discounted price,
based on a sticker colour. The red sticker items have a 20% discount, green
sticker have a 10% discount, and blue sticker have a 5% discount. If the original
price is over $50, then an additional 10% is added to the discount.

"""
#----------Variables----------

# A class that holds sticker discounts
class StickerDiscount():
  RED = 0.8
  GREEN = 0.9
  BLUE = 0.95

#----------Functions----------

# Converts string to int and restarts if it isn't a number
def to_float(string_number):
  try: # If no error convert to int and return
    return float(string_number)
  except ValueError: # If ValueError tell user and restart
    print("Ayo use number. \n")
    main() # Restart

#----------Main---------
def main():
  original_cost = to_float(input("Enter the cost of your item: ")) # Gets original cost and converts to a double
  sticker_colour = input("What colour is the sticker? Red/Green/Blue: ").lower() # Gets sticker input and converts string to lowercase

  bulk_discount_amount = 1 # Originaly no bulk discount
  if original_cost >= 50:
    bulk_discount_amount = 0.9 #Adds bulk discount if order is over $50

  if sticker_colour == "blue":
    sticker_discounted_cost = original_cost * StickerDiscount.BLUE # Multiply origional price by blue sticker discount
  elif sticker_colour == "red":
    sticker_discounted_cost = original_cost * StickerDiscount.RED # Multiply origional price by red sticker discount
  elif sticker_colour == "green":
    sticker_discounted_cost = original_cost * StickerDiscount.GREEN # Multiply origional price by green sticker discount
  else:
    print("Invalid sticker color, please enter either Red/Green/Blue\n") # Input was not a colour
    main() # Restart

  print("Discounted cost:", round(sticker_discounted_cost * bulk_discount_amount, 2), "\n") # Prints final cost of the item with discount
  main() # Restart
main() # Start