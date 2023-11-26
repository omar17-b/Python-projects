from PIL import Image

image_path = '/Users/omarelbanna/Desktop/Personal-project/Python-projects/lg2mekqi25x41.jpg'
img = Image.open(image_path)

name = "Heisenberg"
guess = input("Say My Name: ")

while guess != name:
    guess = input("Try again: ")
else:
    print("You are goddamn right")
    img.show()
