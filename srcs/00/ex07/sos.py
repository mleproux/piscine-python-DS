import sys


def parse_args() -> int:
    """Parse the arguments inside sys.argv\n
        - One arguments is required
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)


def get_morse() -> dict:
    """Return a dictionary of the alphanumerical Morse Code"""
    return {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        " ": "/"}


def main():
    """Convert an alphanumerical string to morse.\n
    - #1: A string
    """
    nested_morse = get_morse()
    text = None
    result = []
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        text = sys.argv[1].upper()
        assert all(c in nested_morse for c in text), "the arguments are bad"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    for c in text:
        result.append(nested_morse[c])
    print(" ".join(result))


if __name__ == "__main__":
    main()
