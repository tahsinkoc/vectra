# from api.services.api_key_service import create_api_key

# res = create_api_key({
#     "name": "Test API Key"
# })

# print(f"API Key Created: {res}")

from api.db.mongo import db
from embedding.create_embedding import create_embedding
from embedding.create_hnsw_index import create_index, search_index

# db_trips = db.trips.find()

# for trip in db_trips:
#     rich_text = trip["description"] + " " + trip["name"] + " " + trip["location"]
#     embedded = create_embedding(rich_text)
#     index = create_index(embedded.tolist(), trip["id"])
#     print(index)


# Finding Test
# searchString = "Balloon rides"
# embedded = create_embedding(searchString)
# labels, distances = search_index(embedded.tolist(), 3)
# print(f"Label: {labels[0]}", f"Distances: {distances}")


# 130+ TRAVELS ROW IMPLEMENTER ^^TESTED^^

# db_travels = db.travels.find({}, {"_id": 0})

# for travel in db_travels:
#     # Create rich text from available fields
#     db_travels = db.travels.find()

# for travel in db_travels:
#     # Create rich text from available fields
#     rich_text = (
#         travel["Destination"] + " " + 
#         travel["Traveler name"] + " " + 
#         travel["Traveler nationality"] + " " + 
#         travel["Traveler gender"] + " " + 
#         f"Age: {travel['Traveler age']} " + 
#         travel["Accommodation type"] + " " + 
#         f"Accommodation cost: ${travel['Accommodation cost']} " + 
#         travel["Transportation type"] + " " + 
#         f"Transportation cost: ${travel['Transportation cost']} " + 
#         f"Duration: {travel['Duration (days)']} days "
#     )
    
#     embedded = create_embedding(rich_text)
#     index = create_index(embedded.tolist(), travel["Trip ID"])
#     print(index)
#     embedded = create_embedding(rich_text)
#     index = create_index(embedded.tolist(), travel["Trip ID"])
#     print(index)


# 100K SALES RECORDS Implementer ^^TESTING^^
# db_sales = db["test-sales-records"].find({}, {"_id": 0})

# for sale in db_sales:
#     rich_text = (
#         sale["Region"] + " " + 
#         sale["Country"] + " " + 
#         sale["Item Type"] + " " + 
#         sale["Sales Channel"] + " " + 
#         f"Order Priority: {sale['Order Priority']} " + 
#         f"Order Date: {sale['Order Date']} " + 
#         f"Ship Date: {sale['Ship Date']} " + 
#         f"Units Sold: {sale['Units Sold']} " + 
#         f"Unit Price: ${sale['Unit Price']} " + 
#         f"Unit Cost: ${sale['Unit Cost']} " + 
#         f"Total Revenue: ${sale['Total Revenue']} " + 
#         f"Total Cost: ${sale['Total Cost']} " + 
#         f"Total Profit: ${sale['Total Profit']}"
#     )
    
#     embedded = create_embedding(rich_text)
#     index = create_index(embedded.tolist(), sale["Order ID"])
#     print(f"Document indexed ID: {index}")