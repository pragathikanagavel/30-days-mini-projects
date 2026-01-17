# Pattern Compression Engine
# Compresses repeated characters in a string


def compress_string(text):
    if not text:
        return ""

    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    # Add last character
    compressed += text[-1] + str(count)

    return compressed


# Main Program
def main():
    text = input("Enter a string to compress: ")

    result = compress_string(text)
    print("Compressed output:", result)


# Run program
main()
