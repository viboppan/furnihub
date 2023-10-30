# import pymongo
# import mongoengine
#
# # MongoDB connection details
# mongo_host = 'localhost'  # Your MongoDB server host
# mongo_port = 27017  # Your MongoDB server port
# mongo_client = pymongo.MongoClient(mongo_host, mongo_port)
#
# # Create a new database named "CustomerDB"
# customer_db = mongo_client["CustomerDB"]
#
# # Create a collection named "Customer" in the "CustomerDB" database
# customer_collection = customer_db["Customer"]
#
# # Define the fields for a customer document
# customer_data = {
#     "name": "John Doe",
#     "email": "john@example.com",
#     "password": "password123",
#     "mobile_number": "1234567890"
# }
#
# # Insert a sample customer document into the collection
# customer_collection.insert_one(customer_data)
#
# # Verify the database and collection creation
# print("Database 'CustomerDB' and collection 'Customer' created.")
#
# # Close the MongoDB connection
# mongo_client.close()
