import sys
from giphy_client import V1

payload = {
	"version": 'v1',
	"config": {
		"resource": "gifs",
		"tag": "soccer goal",
		"rating": "r"
	}
}

version = payload["version"].upper()
client = globals()[version](payload)
