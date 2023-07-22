import tkinter as tk
import random

# Dictionary containing NATO phonetic alphabet translations
nato_phonetic_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'Xray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

def convert_to_cases():
    text = input_box.get()
    upper_output_box.delete(0, tk.END)
    upper_output_box.insert(0, text.upper())
    title_output_box.delete(0, tk.END)
    title_output_box.insert(0, text.title())
    random_output_box.delete(0, tk.END)
    random_text = "".join(
        char.upper() if random.choice([True, False]) else char.lower()
        for char in text
    )
    random_output_box.insert(0, random_text)
    reverse_output_box.delete(0, tk.END)
    reverse_output_box.insert(0, text[::-1])
    backwards_output_box.delete(0, tk.END)
    backwards_output_box.insert(0, " ".join(text.split()[::-1]))
    phonetic_output_box.delete(0, tk.END)
    phonetic_text = "".join(
        f"{nato_phonetic_alphabet[char.upper()]} "
        if char.upper() in nato_phonetic_alphabet
        else f"{char} "
        for char in text
    )
    phonetic_output_box.insert(0, phonetic_text.strip())

    # Convert to 1337 (Leet Speak)
    leet_output_box.delete(0, tk.END)
    leet_dict = {
        'A': '4',
        'B': '8',
        'E': '3',
        'G': '6',
        'L': '1',
        'O': '0',
        'S': '5',
        'T': '7',
        'Z': '2'
    }
    leet_text = "".join(leet_dict.get(char.upper(), char) for char in text)
    leet_output_box.insert(0, leet_text)

# Create the main window
window = tk.Tk()
window.title("Text Case Converter")
window.geometry('650x515')

# Create the input label and box
input_label = tk.Label(window, text="Enter text to convert:", font=("Arial", 16))
input_label.pack()
input_box = tk.Entry(window, font=("Arial", 16), width=50)
input_box.pack()

# Create the output labels and boxes
upper_output_label = tk.Label(window, text="Uppercase:", font=("Arial", 16), bg="#FEE715", fg="#101820")
upper_output_label.pack()
upper_output_box = tk.Entry(window, font=("Arial", 16), width=50)
upper_output_box.pack()

title_output_label = tk.Label(window, text="Title Case:", font=("Arial", 16), bg="#FEE715", fg="#101820")
title_output_label.pack()
title_output_box = tk.Entry(window, font=("Arial", 16), width=50)
title_output_box.pack()

random_output_label = tk.Label(window, text="Random Case:", font=("Arial", 16), bg="#FEE715", fg="#101820")
random_output_label.pack()
random_output_box = tk.Entry(window, font=("Arial", 16), width=50)
random_output_box.pack()

reverse_output_label = tk.Label(window, text="Reverse Text:", font=("Arial", 16), bg="#FEE715", fg="#101820")
reverse_output_label.pack()
reverse_output_box = tk.Entry(window, font=("Arial", 16), width=50)
reverse_output_box.pack()

backwards_output_label = tk.Label(window, text="Backwards Text:", font=("Arial", 16), bg="#FEE715", fg="#101820")
backwards_output_label.pack()
backwards_output_box = tk.Entry(window, font=("Arial", 16), width=50)
backwards_output_box.pack()

phonetic_output_label = tk.Label(window, text="Phonetic Alphabet:", font=("Arial", 16), bg="#FEE715", fg="#101820")
phonetic_output_label.pack()
phonetic_output_box = tk.Entry(window, font=("Arial", 16), width=50)
phonetic_output_box.pack()

leet_output_label = tk.Label(window, text="1337 (Leet Speak):", font=("Arial", 16), bg="#FEE715", fg="#101820")
leet_output_label.pack()
leet_output_box = tk.Entry(window, font=("Arial", 16), width=50)
leet_output_box.pack()

# Create the convert button
convert_button = tk.Button(window, text="Convert", font=("Arial", 16), bg="#101820", fg="#99F443", command=convert_to_cases)
convert_button.pack()

# Start the main event loop
window.mainloop()
