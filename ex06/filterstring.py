import sys
from ft_filter import ft_filter


def filter_words(text, length_threshold):
    """Filters words from a text string based on their length.

    Args:
        text (str): The input text string.
        length_threshold (int):  Words longer than this threshold are included.

    Returns:
        list: A list of words from the text that exceed the length threshold.
    """
    words = text.split(" ")
    filtered_words = [
            ft_filter(lambda word: len(word) > length_threshold, words)
    ]
    return filtered_words


def main():
    """Handles argument processing, input validation, and word filtering."""

    if len(sys.argv) != 3:
        raise AssertionError("The arguments are bad")

    try:
        text = sys.argv[1]
        length_threshold = int(sys.argv[2])
    except (ValueError, AssertionError):  # Catch both potential errors
        raise AssertionError("The arguments are bad")

    result = filter_words(text, length_threshold)
    print(result)


if __name__ == "__main__":
    main()
