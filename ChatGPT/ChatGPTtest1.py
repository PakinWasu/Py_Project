def encode_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': ' ',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '!': '-.-.--'
    }

    # Convert the input text to uppercase for consistency
    text = text.upper()

    # Encode each character into Morse code
    morse_code = [morse_code_dict[char] for char in text if char in morse_code_dict]

    # Join the Morse code representations and return as a string
    return ' '.join(morse_code)

# Example calls
print(encode_morse("EDABBIT CHALLENGE"))
print(encode_morse("HELP ME !"))
