import requests
from PIL import Image
import io


response = requests.get("https://randomfox.ca/images/116.jpg")
image_bytes = io.BytesIO(response.content)

img = Image.open(image_bytes)
img.show()
