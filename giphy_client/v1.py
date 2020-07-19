import requests
from .base import GiphyClient

class V1(GiphyClient):
	def __init__(self, payload):
		super(V1, self).__init__(payload)
		self.endpoint = payload["endpoint"]
		self.resource = payload["resource"]

		self.config = payload["config"]
		self.config["api_key"] = self.api_key

		self.set_images()

	def set_images(self):
		response = requests.get(
			f"{self.base_url}/v1/{self.resource}/{self.endpoint}",
			params = self.config
		)

		self.images = response.json()["data"]["images"]

	def get_image(self, size = "original"):
		return self.images[size]["url"]
