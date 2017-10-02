"Functions used to demonstrate code in this directory."

def headline(line):
    "Return a headline string with a separator."
    max_len = 78
    sep_len = int((max_len - len(line)) / 2) - 2

    return "\n [" + "=" * sep_len + "  " + line + "  " + "=" * sep_len + "]"

if __name__ == "__main__":
    print("This file does nothing useful on its own.")
