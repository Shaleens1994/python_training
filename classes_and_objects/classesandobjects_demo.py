class Product:
     def __init__(self, product_name, product_price, product_quatity):
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quatity

     def product_price_change(self, new_product_price):
        self.product_price = new_product_price

     def product_quantity_change(self,new_quantity):
         self.product_quantity = new_quantity

     def get_product_info(self):
         print(f"Product: {self.product_name} currently costs {self.product_price} and we have {self.product_quantity}  units left")


'''product_1 = Product("iphone", "1200", "25")
product_1.get_product_info()
product_1.product_price_change(1400)
product_1.get_product_info()
product_2 = Product("s24", "1100", "55")
product_2.get_product_info()
'''

     
  
 