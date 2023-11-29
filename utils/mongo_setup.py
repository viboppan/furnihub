# import random
#
# from mongoengine import Document, StringField, FloatField, ListField, IntField, connect
# from utils.MongoDBUtils import Product
#
# connect(host="mongodb://localhost:27017/furnihub")
#
#
# # MongoDB connection setup
#
#
# # Sample data for 100 products
# def insert_sample_data():
#     print("hello")
#     for i in range(1, 101):
#         product = Product(
#             name=f'Product {i}',
#             cost=50.99 + i,
#             dimensions=[10.0, 5.0, 3.0],
#             color='Red',
#             brand='Brand A',
#             material_type='Plastic',
#             weight=0.5 + (i / 10),
#             seller_id=f'seller{i}',
#             rating=4.5
#         )
#         product.save()
#     update_product_images()
#
#
# # Generate random image URLs
# def generate_random_image_url():
#     return f"https://via.placeholder.com/{random.randint(200, 400)}x{random.randint(200, 400)}"
#
#
# # Update product documents with random image URLs
# def update_product_images():
#     products = Product.objects()
#
#     for product in products:
#         product.image_url = generate_random_image_url()
#         product.save()
#
#
# if __name__ == "__main__":
#     update_product_images()
