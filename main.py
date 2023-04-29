import tkinter as tk
import random
from tkinter import Text
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import padding
global TextBox,TextBox2
global AESkey

root = tk.Tk()
root.geometry("860x640")
root.title("TextEncrypt")
optionsA = ["Encrypt", "Decrypt"]
optionsT = ["AES 265", "Ceaser", "ASCII"]
selected_optionA = tk.StringVar()
selected_optionA.set("select action")
dropdownA = tk.OptionMenu(root, selected_optionA, *optionsA)
dropdownA.place(x=2, y=5)
selected_optionT = tk.StringVar()
selected_optionT.set("select type")
dropdown = tk.OptionMenu(root, selected_optionT, *optionsT)
dropdown.place(x=2, y=45)
ptl = tk.Label(root, text="Plain text:",  font=("Arial", 25))
ptl.place(x=2, y=90)
TextBox = tk.Text(root, height=12, width=40, font=("Arial", 12))
TextBox.place(x = 2, y = 130)

ctl = tk.Label(root, text="Cipher text:",  font=("Arial", 25))
ctl.place(x=400, y=90)
TextBox2 = tk.Text(root, height=12, width=40, font=("Arial", 12))
TextBox2.place(x = 400, y = 130)

keyhole: Text = tk.Text(root, height=2, width=60, font = ("Arial", 15))
keyhole.place(x=100, y= 400)

def aesEn():
    f = Fernet(keyhole.get(0.0, "end").encode())
    entry = TextBox.get(0.0, "end-1c").encode()
    padder = padding.PKCS7(128).padder()
    plaintext = padder.update(entry) + padder.finalize()
    encrypted_message = f.encrypt(plaintext)
    TextBox2.delete(0.0, "end")
    TextBox2.insert(0.0, encrypted_message.decode())
def aesDe():
    AESkey = keyhole.get(0.0, "end").encode()
    ciphertext = TextBox2.get(0.0, "end").encode()
    f = Fernet(AESkey)
    decrypted_message = f.decrypt(ciphertext)
    TextBox.delete(0.0, "end")
    TextBox.insert(0.0, decrypted_message.decode())

def ceaserEn():
    message = TextBox.get(0.0, "end-1c")
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    Ceaserkey = int(keyhole.get(0.0, "end-1c"))
    encrypt = ''

    for i in message:
        position = alphabet.find(i)
        newposition = (position + int(Ceaserkey)) % 94
        encrypt += alphabet[newposition]
    TextBox2.delete(0.0, "end")
    TextBox2.insert(0.0, encrypt)

def ceaserDe():
    message = TextBox2.get(0.0, "end-1c")
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    Ceaserkey = int(keyhole.get(0.0, "end-1c"))
    decrypt = ''

    for i in message:
        position = alphabet.find(i)
        newposition = (position - int(Ceaserkey)) % 94
        decrypt += alphabet[newposition]
    TextBox.delete(0.0, "end-1c")
    TextBox.insert(0.0, decrypt)

def asciiEn():
    message = TextBox.get(0.0, "end-1c")
    ascii_list = []

    for char in message:
        ascii_value = ord(char)
        ascii_list.append(ascii_value)
    TextBox2.delete(0.0, "end")
    TextBox2.insert(0.0, str(ascii_list))

def asciiDe():
    message = TextBox.get(0.0, "end-1c")
    num_list = [int(num) for num in message.split(",")]
    decoded_string = ""
    for ascii_code in num_list:
        decoded_string += chr(ascii_code)
    TextBox.delete(0.0, "end")
    TextBox.insert(0.0, decoded_string)


def router():
    if selected_optionA.get() == "Encrypt" and selected_optionT.get() == "AES 265":
        aesEn()
    elif selected_optionA.get() == "Decrypt" and selected_optionT.get() == "AES 265":
        aesDe()

    if selected_optionA.get() == "Encrypt" and selected_optionT.get() == "Ceaser":
        ceaserEn()
    elif selected_optionA.get() == "Decrypt" and selected_optionT.get() == "Ceaser":
        ceaserDe()

    if selected_optionA.get() == "Encrypt" and selected_optionT.get() == "ASCII":
        asciiEn()
    elif selected_optionA.get() == "Decrypt" and selected_optionT.get() == "ASCII":
        asciiDe()



keylabel = tk.Label(root, text = "KEY:", font=("Arial", 18))
keylabel.place(x=6, y = 410)
gobutton = tk.Button(root, text="Go!", font=("Arial", 30), bg="#00ff99", command= router)
gobutton.pack(side="bottom")


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    temp = random.randint(range_start, range_end)
    return temp
def genKey():
    if selected_optionA.get() == "Encrypt" and selected_optionT.get() == "AES 265":
        AESkey = Fernet.generate_key()
        keyhole.delete(0.0,"end")
        keyhole.insert(0.1, AESkey.decode())
    if selected_optionA.get() == "Encrypt" and selected_optionT.get() == "Ceaser":
        key = random_with_N_digits(int(keylen.get()))
        keyhole.delete(0.0,"end")
        keyhole.insert(0.1, str(key))

genk = tk.Button(root, text="Generate\nKey", font=("Arial", 10), bg="white", command= genKey)
genk.place(x=8, y = 490)

keylenl = tk.Label(root, text = "Length of key for Auto-gen (Ceaser only):")
keylenl.place(x = 85, y = 480)

keylen = tk.Entry(root, width=42)
keylen.place(x = 85, y = 510)
root.mainloop()
