
from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_answer(data,probs):

    index_of_max = probs.argmax()

    return data[index_of_max]

def classify_image_in_text(url_of_image,text_possibilities):

    image = Image.open(requests.get(url_of_image, stream=True).raw)
    inputs = processor(text=text_possibilities, images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities

    return get_answer(text_possibilities,probs)

def classify_image_in_text_file_version(file,text_possibilities):

    image = Image.open(file)
    inputs = processor(text=text_possibilities, images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities

    return get_answer(text_possibilities,probs)