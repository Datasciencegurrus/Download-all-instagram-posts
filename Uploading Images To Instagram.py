import os
from instabot import Bot

bot = Bot()

bot.login(username="", password="") # your username and password

# Provide the path to the folder containing the images
image_folder = r''

# Loop through all files in the folder
for filename in os.listdir(image_folder):
    # Check if the file is an image (assuming .jpg, .jpeg, and .png formats)
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".mp4"):
        # Create the full file path by joining the folder path and the filename
        file_path = os.path.join(image_folder, filename)

        # Upload the image with a caption
        bot.upload_photo(file_path, caption="Technical Scripter Event 2019")
