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
searchString = "Balloon rides"
embedded = create_embedding(searchString)
labels, distances = search_index(embedded.tolist(), 3)
print(f"Label: {labels[0]}", f"Distances: {distances}")
