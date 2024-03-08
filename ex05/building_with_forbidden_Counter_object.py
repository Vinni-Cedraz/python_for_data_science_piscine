import sys
import string
from collections import Counter


def count_characters(text):
    """Counts different character types in a given text.

    Args:
        text: The input text string.

    Returns:
        A dictionary containing counts for upper-case, lower-case, punctuation,
        digits, and spaces.
    """

    classifiers = {
        "upper": string.ascii_uppercase,
        "lower": string.ascii_lowercase,
        "digits": string.digits,
        "spaces": string.whitespace,
    }
    results = Counter(
            category for char in text
            for category, chars in classifiers.items() if char in chars
    )
    results["punctuation"] = len(text) - sum(results.values())
    results["len"] = len(text)
    return results


def main():
    """Handles argument processing, user input, and character counting."""

    if len(sys.argv) > 2:
        raise AssertionError("Only one argument is allowed.\n")

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the input text? ")

    counts = count_characters(text)

    print(f"The text contains {counts['len']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


if __name__ == "__main__":
    main()
