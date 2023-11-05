import os
def get_api_key():
    """Get the API key from the environment variable."""
    api_key = os.getenv("api_key")
    print(api_key)
    if api_key is None:
        raise ValueError("API_KEY is not set in the environment.")
    return api_key
get_api_key()