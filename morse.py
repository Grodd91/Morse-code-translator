import re
#library 
ENG_TO_MORSE = {1
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.'
}
MORSE_TO_ENG = {value: key for key, value in ENG_TO_MORSE.items()}
#translation functions
def eng_to_morse(text):
    text = re.sub('[^A-Za-z0-9]', ' ', text.upper())
    return ' '.join([ENG_TO_MORSE.get(char, '') for char in text])
def morse_to_eng(morse):
    letters = [MORSE_TO_ENG.get(letter, '') for letter in morse.split()]
    return ''.join(letters)
choice = input("Enter '1' to translate English text to Morse code, or '2' to translate Morse code to English text: ")
if choice == '1':
    text = input("Enter the English text to translate: ")
    result = eng_to_morse(text)
    print(f"Morse code: {result}")
elif choice == '2':
    morse = input("Enter the Morse code to translate: ")
    result = morse_to_eng(morse)
    print(f"English text: {result}")
else:
    print("Invalid choice, please enter '1' or '2'")
