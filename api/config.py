import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "my_database")

# need to fix cause cant read from env file
# mid level security penetration !!!!
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "UXSApB20PPpsJ6LlEBj99HkdVTfmplN25HL0cxZoQEmGO5fG9wyv4wBRvpSCl4ha")