import os
import re

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
    description = StringField()


# MongoDB Connection
connect(host="mongodb://localhost:27017/furnihub")


# Function to insert products from images in folders with random data and color detection
def insert_products_from_images(folder_path):
    for category_folder in os.listdir(folder_path):
        category_path = os.path.join(folder_path, category_folder)
        if os.path.isdir(category_path):
            for idx, image_file in enumerate(os.listdir(category_path)):
                image_path = os.path.join(category_path, image_file)

                # Use a regular expression to match the initial part of the file name as the color name
                match = re.match(r'^[^\d.]+', image_file)
                color_name = match.group() if match else "Unknown"

                # Create a new Product document with random data and detected color
                product = Product(
                    name=f"{category_folder}{idx + 1}",
                    cost=random.uniform(50, 500),
                    dimensions=[random.uniform(1, 10) for _ in range(3)],
                    color="brown",
                    brand=fake.company(),
                    material_type="wood",
                    weight=random.uniform(1, 50),
                    seller_id=fake.uuid4(),
                    rating=random.uniform(1, 5),
                    image_url=image_path,  # Store local path as image_url
                    category=category_folder,
                    description="This awesome product provides you fabulous comfort",
                    available_quantity=4
                )
                product.save()
                # Rename the image file with the generated product ID
                new_image_name = f"{product.id}{os.path.splitext(image_file)[1]}"
                new_image_path = os.path.join(category_path, new_image_name)
                os.rename(image_path, new_image_path)
                # Update the image_url field with the new path
                product.image_url = new_image_path
                product.save()


import os


def rename_images_to_brown(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Set the new name as 'brown'
            new_name = 'brown' + os.path.splitext(filename)[1]
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)

            # Check if the new name already exists, and if so, append a number
            count = 1
            while os.path.exists(new_path):
                new_name = f'brown_{count}' + os.path.splitext(filename)[1]
                new_path = os.path.join(folder_path, new_name)
                count += 1

            # Rename the file
            os.rename(old_path, new_path)


# Driver code
if __name__ == "__main__":
    # folder_path = "../static/images/coffee_table"
    # rename_images_to_brown(folder_path)
    images_folder_path = "../static/images/"  # Replace with your actual path
    insert_products_from_images(images_folder_path)
