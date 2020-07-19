import sys
from giphy_client import V1

def handler(event, context):
	version = event.pop("version").upper()
	client = globals()[version](event)
	return client.get_image()
