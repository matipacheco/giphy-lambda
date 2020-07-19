import sys
from jsonschema import validate

from giphy_client import V1, v1_schema

def handler(event, context):
	try:
		validate(instance = event, schema = v1_schema)

		version = event.pop("version").upper()
		client = globals()[version](event)

		return { "url": client.get_image() }

	except ModuleNotFoundError as error:
		return { error: "Error {0}".format(error) }
