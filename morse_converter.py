from tkinter import *
from tkinter import ttk

conversion = {
    'a' : '.-',     'b' : '-...',   'c' : '-.-.',   'd' : '-..',    'e' : '.',
    'f' : '..-.',   'g' : '--.',    'h' : '....',   'i' : '..',     'j' : '.---',
    'k' : '-.-',    'l' : '.-..',   'm' : '--',     'n' : '-.',     'o' : '---',
    'p' : '.--.',   'q' : '--.-',   'r' : '.-.',    's' : '...',    't' : '-',
    'u' : '..-',    'v' : '...-',   'w' : '.--',    'x' : '-..-',   'y' : '-.--',
    'z' : '--..'    }

def ascii2morse(*args):
    # get string of input ascii text and lower case it
    ascii_str = str(ascii_text.get())
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
    morse_text.set(morse_str)


# set main window 
root = Tk()
root.title("Morse code converter")

# give main window a frame to encapsulate subsequent widgets
mf = ttk.Frame(root, padding="3 3 12 12")
mf.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# establish input entry
ascii_text = StringVar()
ascii_text_entry = ttk.Entry(mf, width=25, textvariable=ascii_text)
ascii_text_entry.grid(column=2, row=1)

# establish output display
morse_text = StringVar()
ttk.Label(mf, textvariable=morse_text, wraplength=250, justify=LEFT).grid(column=2, row=3)

# create button to convert
ttk.Button(mf, text="Convert", command=ascii2morse).grid(column=2, row=2)

# add labels in input and output fields
ttk.Label(mf, text="ASCII text: ").grid(column=1, row=1)
ttk.Label(mf, text="Morse text: ").grid(column=1, row=3)

# give some padding to the widgets in the main frame
for child in mf.winfo_children():
    child.grid_configure(padx=5, pady=5)

# start with cursor in input box and assign Enter key to start conversion
ascii_text_entry.focus()
root.bind("<Return>", ascii2morse)

# start main event monitoring loop
root.mainloop()
    
