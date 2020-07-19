import os

class GiphyClient:
	base_url = "https://api.giphy.com"
	api_key = os.getenv("GIPHY_API_KEY")
