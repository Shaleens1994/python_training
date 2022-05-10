from classesandobjects_demo import Product
from posts import Post

product_1 = Product("iphone", "1200", "25")
product_1.get_product_info()
product_1.product_price_change(1400)
product_1.get_product_info()
product_2 = Product("s24", "1100", "55")
product_2.get_product_info()
new_post = Post("this is the first message","user1")
new_post.display_message()
