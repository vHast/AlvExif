from PIL import Image
from PIL.ExifTags import TAGS 

def get_exif(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data is not None:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            print(f"{tag_name}: {value}")
    else:
        print("No EXIF metadata found")

# Temporary, need arguments for this
get_exif('picture.jpg')