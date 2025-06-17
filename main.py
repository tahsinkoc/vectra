from api.services.api_key_service import create_api_key

res = create_api_key({
    "name": "Test API Key"
})

print(f"API Key Created: {res}")
