import sys
from giphy_client import V1

payload = {
	"version": "v1",
	"resource": "gifs",
	"endpoint": "random",
	"config": {
		"endpoint": "random",
		"tag": "soccer goal",
		"rating": "r"
	}
}

version = payload.pop("version").upper()
client = globals()[version](payload)
print(client.get_image())