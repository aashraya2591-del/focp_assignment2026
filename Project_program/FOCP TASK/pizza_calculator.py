

def get_pizza_price(pizza_number):
    """
    Gets a valid pizza price from the user.
    Keeps asking until a valid positive number is entered.
    """
    while True:
        try:
           
            price = float(input(f"Enter Price of Pizza #{pizza_number}: "))
            
          
            if price <= 0:
                print("Please enter a valid price!")
                continue
            
           
            return price
            
        except ValueError:
 
            print("Please enter a valid price!")

def calculate_order():
    """
    Main function that calculates the pizza order total and discount.
    """
   
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================")
    
 
    prices = []
    for i in range(1, 5): 
        price = get_pizza_price(i)
        prices.append(price)
    
 
    total_before_discount = sum(prices)
  
    cheapest_pizza = min(prices)
    
   
    order_total = total_before_discount - cheapest_pizza
    

    discount_percentage = (cheapest_pizza / total_before_discount) * 100
    
 
    print(f"Order Total is £{order_total:.2f}, a fabulous discount of {discount_percentage:.0f}%!")

if __name__ == "__main__":
    calculate_order()