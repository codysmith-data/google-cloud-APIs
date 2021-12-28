import io
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = '220px-Guido-portrait-2014-drc.jpg'

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection and scoring  on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

for label in labels:
    print(label.description, label.score)