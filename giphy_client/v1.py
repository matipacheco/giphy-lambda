from .base import GiphyClient

class V1(GiphyClient):
	def __init__(self, payload):
		super(V1, self).__init__(payload)

