import hashlib

def text_to_hash(text):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes of the input text
    sha256_hash.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_text = sha256_hash.hexdigest()

    return hashed_text

if __name__ == "__main__":
    # Get user input for the text to be hashed
    input_text = input("Enter the text to be hashed: ")

    # Convert the text to hash
    hashed_text = text_to_hash(input_text)

    # Print the original text and its hash
    print(f"Original Text: {input_text}")
    print(f"Hashed Text: {hashed_text}")
