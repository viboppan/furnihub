import os

from bson import ObjectId
from mongoengine import connect, Document, StringField, FloatField, ListField, FloatField, ObjectIdField
from faker import Faker
import random

fake = Faker()


# Define MongoDB model
class Product(Document):
    product_id = ObjectIdField(default=ObjectId, primary_key=True)
    name = StringField()
    cost = FloatField()
    dimensions = ListField(FloatField())
    color = StringField()
    brand = StringField()
    material_type = StringField()
    weight = FloatField()
    seller_id = StringField()
    rating = FloatField()
    image_url = StringField()
    category = StringField()


# MongoDB Connection
connect(host="mongodb://localhost:27017/furniture")


# Function to insert products from images in folders with random data
def insert_products_from_images(folder_path):
    for category_folder in os.listdir(folder_path):
        category_path = os.path.join(folder_path, category_folder)
        if os.path.isdir(category_path):
            for idx, image_file in enumerate(os.listdir(category_path)):
                image_path = os.path.join(category_path, image_file)
                # Create a new Product document with random data
                product = Product(
                    name=f"{category_folder}{idx + 1}",
                    cost=random.uniform(50, 500),
                    dimensions=[random.uniform(1, 10) for _ in range(3)],
                    color=fake.color_name(),
                    brand=fake.company(),
                    material_type=fake.word(),
                    weight=random.uniform(1, 50),
                    seller_id=fake.uuid4(),
                    rating=random.uniform(1, 5),
                    image_url=image_path,  # Store local path as image_url
                    category=category_folder
                )
                product.save()
                # Rename the image file with the generated product ID
                new_image_name = f"{product.id}{os.path.splitext(image_file)[1]}"
                new_image_path = os.path.join(category_path, new_image_name)
                os.rename(image_path, new_image_path)
                # Update the image_url field with the new path
                product.image_url = new_image_path
                product.save()


# Driver code
if __name__ == "__main__":
    images_folder_path = "C:\\Users\\vikra\\Pictures"  # Replace with your actual path
    insert_products_from_images(images_folder_path)
