import sys


def encode_morse(text):
    """Encodes a given text string into Morse Code using a dictionary lookup.

    Args:
        text (str): The input text to be encoded.

    Returns:
        str: The Morse Code representation of the input text.
    """

    NESTED_MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/",
    }

    encoded_chars = [NESTED_MORSE.get(char.upper(), "") for char in text]
    return " ".join(encoded_chars)


def main():
    """Handles argument processing, input validation, and Morse encoding."""

    if len(sys.argv) != 2:
        raise AssertionError("The arguments are bad")

    try:
        text = sys.argv[1]
    except (ValueError, AssertionError):
        raise AssertionError("The arguments are bad")

    encoded_text = encode_morse(text)
    print(encoded_text)


if __name__ == "__main__":
    main()
