import os
from jsonschema import validate

schema = {
	"type": "object",
	"required": ["endpoint", "config"],
	"properties": {
		"version": {"type": "string"},
		"endpoint": {"type": "string", "enum": ["random"]},
		"resource": {"type": "string", "enum": ["gifs", "stickers"]},
		"config": {
			"type": "object",
			"properties": {
				"tag": {"type": "string"},
				"rating": {"type": "string", "enum": ["g", "pg", "pg-13", "r"]}
			}
		}
	}
}

class GiphyClient:
	base_url = "https://api.giphy.com"
	api_key = os.getenv("GIPHY_API_KEY")

	def __init__(self, payload):
		validate(instance = payload, schema = schema)
