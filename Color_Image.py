import requests
import urllib.request
import tkinter as tk
from tkinter import filedialog


def choose_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename()
    root.destroy()
    return file


def save_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file = filedialog.asksaveasfilename(filetypes=[('JPG', '*.jpg')])
    root.destroy()
    return file


def take_image_input(path):
    try:
        image = open(path, 'rb')
    except FileNotFoundError:
        print('No Image Path Chosen...')
        return
    return image


def send_request(image):
    req = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            'image': image,
        },
        headers={'api-key': '30ab770e-fd7f-4914-b0bd-8f095a6a8303'},
    )
    return req


def save_file(req):
    print('Done Coloring!')
    user_save_location = save_file_dialog()
    file_path = user_save_location + '.jpg' if not user_save_location.endswith('.jpg') else user_save_location
    urllib.request.urlretrieve(req.json()['output_url'], file_path)
    open_image(file_path)


def open_image(path):
    open_it = str(input('Would you like to open the image? (y / n): ')).lower()

    if open_it == 'y':
        from PIL import Image
        img = Image.open(path)
        img.show()


def main():
    path = choose_file_dialog()
    image = take_image_input(path)
    if image is not None:
        print('Coloring... its may take a little time.')
        req = send_request(image)
    else:
        return

    save_file(req)


if __name__ == '__main__':
    main()
