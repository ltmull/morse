from tkinter import *
from tkinter import ttk

conversion = {
    'a' : '.-',     'b' : '-...',   'c' : '-.-.',   'd' : '-..',    'e' : '.',
    'f' : '..-.',   'g' : '--.',    'h' : '....',   'i' : '..',     'j' : '.---',
    'k' : '-.-',    'l' : '.-..',   'm' : '--',     'n' : '-.',     'o' : '---',
    'p' : '.--.',   'q' : '--.-',   'r' : '.-.',    's' : '...',    't' : '-',
    'u' : '..-',    'v' : '...-',   'w' : '.--',    'x' : '-..-',   'y' : '-.--',
    'z' : '--..',   '1' : '.----',  '2' : '..---',  '3' : '...--',  '4' : '....-',
    '5' : '.....',  '6' : '-....',  '7' : '--...',  '8' : '---..',  '9' : '----.',
    '0': '-----'    }

def ascii2morse(*args):
    # get string of input ascii text and lower case it
    ascii_str = str(input_text.get())
    ascii_str = ascii_str.lower()
    morse_str = ''

    # iterate through ascii string, convert each letter,
    # and place encoded letter in morse string
    length = len(ascii_str)
    i = 0
    while i < length:
        if ascii_str[i] == ' ':
            # add 3 spaces between words
            morse_str += '   '
            i += 1
        else:
            morse_str += conversion[ ascii_str[i] ]
            # add 1 space between letters of a word
            morse_str += ' '
            i += 1    

    # assign the converted string to be displayed
    output_text.set(morse_str)

def morse2ascii(*args):
    # get input string
    morse_str = str(input_text.get())
    ascii_str = ''

    # replace spaces ('    ') with ' xxx '
    morse_str = morse_str.replace('    ', ' xxx ')

    # swap keys and values in conversion dict
    m2a_conversion = {v : k for k, v in conversion.items()}
    # add entry to 
    m2a_conversion['xxx'] = ' '

    # separate into list of strings, each containing 1 Morse character
    morse_list = morse_str.split()

    for char in morse_list:
        ascii_str += m2a_conversion[char]

    # assign the converted string to be displayed
    output_text.set(ascii_str)


# set main window 
root = Tk()
root.title("Morse code converter")

# give main window a frame to encapsulate subsequent widgets
mf = ttk.Frame(root, padding="3 3 12 12")
mf.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# establish input entry
input_text = StringVar()
input_text_entry = ttk.Entry(mf, width=50, textvariable=input_text)
input_text_entry.grid(column=2, row=2, columnspan=2)

# establish output display
output_text = StringVar()
ttk.Label(mf, textvariable=output_text, wraplength=250, justify=LEFT).grid(column=2, row=4)

# create buttons to convert
ttk.Button(mf, text="Convert ASCII to Morse", command=ascii2morse).grid(column=2, row=3)
ttk.Button(mf, text="Convert Morse to ASCII", command=morse2ascii).grid(column=3, row=3)

# add labels for input and output fields and instructions
ttk.Label(mf, text="Type here: ").grid(column=1, row=2)
ttk.Label(mf, text="Translation: ").grid(column=1, row=4)
ttk.Label(mf, text="When inputting Morse code, place 1 space between each letter in a word and 4 spaces to indicate a space between words", wraplength=400, justify=LEFT).grid(column=1, row=1, columnspan=4)

# give some padding to the widgets in the main frame
for child in mf.winfo_children():
    child.grid_configure(padx=5, pady=5)

# start with cursor in input box and assign Enter key to start conversion
input_text_entry.focus()
root.bind("<Return>", ascii2morse)

# start main event monitoring loop
root.mainloop()
    
