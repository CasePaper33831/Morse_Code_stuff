'''
TODO: debugging and stuff

DONE: User input for English/morse translate

VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''
import tkinter as tk

# mmorse code and English stuff
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + '/'
        else:
            cipher += ' '
    return cipher

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

def translate():
    if translation_option.get() == "English to Morse Code":
        message = entry.get()
        result = encrypt(message.upper())
        output_label.config(text="Morse Code: " + result)
    elif translation_option.get() == "Morse Code to English":
        message = entry.get()
        result = decrypt(message)
        output_label.config(text="English: " + result)

popup = tk.Tk()
popup.title("Translation")

label = tk.Label(popup, text="Select translation type:")
label.pack()

translation_option = tk.StringVar()
translation_option.set("English to Morse Code")
translation_menu = tk.OptionMenu(popup, translation_option, "English to Morse Code", "Morse Code to English")
translation_menu.pack()

label = tk.Label(popup, text="Enter a message:")
label.pack()

entry = tk.Entry(popup)
entry.pack()

translate_button = tk.Button(popup, text="Translate", command=translate)
translate_button.pack()

output_label = tk.Label(popup, text="click above button to translate")
output_label.pack()

popup.mainloop()
