import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, key, save_name):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Add the key value to each pixel and use modulo 256 to wrap around
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    
    save_name_with_extension = save_name + '.png'
    encrypted_image.save(save_name_with_extension)
    print(f"Image encrypted and saved as '{save_name_with_extension}'")

# Function to decrypt the image
def decrypt_image(image_path, key, save_name):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Subtract the key value from each pixel and use modulo 256 to wrap around
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    
    save_name_with_extension = save_name + '.png'
    decrypted_image.save(save_name_with_extension)
    print(f"Image decrypted and saved as '{save_name_with_extension}'")

def select_file():
    file_path = filedialog.askopenfilename()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def process_image():
    image_path = entry_path.get()
    key = int(entry_key.get())
    save_name = entry_save_name.get()
    action = var_action.get()
    
    if action == 'Encrypt':
        encrypt_image(image_path, key, save_name)
    elif action == 'Decrypt':
        decrypt_image(image_path, key, save_name)
    else:
        print("Invalid action selected.")

# Set up the GUI
root = tk.Tk()
root.title("Image Encryption Tool")

frame = tk.Frame(root)
frame.pack(pady=20)

label_path = tk.Label(frame, text="Image Path:")
label_path.grid(row=0, column=0, padx=10, pady=5)

entry_path = tk.Entry(frame, width=50)
entry_path.grid(row=0, column=1, padx=10, pady=5)

button_browse = tk.Button(frame, text="Browse", command=select_file)
button_browse.grid(row=0, column=2, padx=10, pady=5)

label_key = tk.Label(frame, text="Encryption Key:")
label_key.grid(row=1, column=0, padx=10, pady=5)

entry_key = tk.Entry(frame)
entry_key.grid(row=1, column=1, padx=10, pady=5)

label_save_name = tk.Label(frame, text="Save As:")
label_save_name.grid(row=2, column=0, padx=10, pady=5)

entry_save_name = tk.Entry(frame)
entry_save_name.grid(row=2, column=1, padx=10, pady=5)

var_action = tk.StringVar(value="Encrypt")
radio_encrypt = tk.Radiobutton(frame, text="Encrypt", variable=var_action, value="Encrypt")
radio_encrypt.grid(row=3, column=0, padx=10, pady=5)

radio_decrypt = tk.Radiobutton(frame, text="Decrypt", variable=var_action, value="Decrypt")
radio_decrypt.grid(row=3, column=1, padx=10, pady=5)

button_process = tk.Button(frame, text="Process", command=process_image)
button_process.grid(row=4, columnspan=3, pady=10)

root.mainloop()
