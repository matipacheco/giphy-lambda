from jsonschema import validate

schema = {
	"type": "object",
	"required": ["version", "config"],
	"properties": {
		"version": {"type": "string"},
		"config": {
			"type": "object",
			"properties": {
				"resource": {"type": "string", "enum": ["gifs", "stickers"]},
				"tag": {"type": "string"},
				"rating": {"type": "string", "enum": ["g", "pg", "pg-13", "r"]}
			}
		}
	}
}

class GiphyClient:
	def __init__(self, payload):
		validate(instance = payload, schema = schema)
