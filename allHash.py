import hashlib

def md5_hash(text):
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(text.encode('utf-8'))
    return md5_hash_object.hexdigest()

def sha1_hash(text):
    sha1_hash_object = hashlib.sha1()
    sha1_hash_object.update(text.encode('utf-8'))
    return sha1_hash_object.hexdigest()

def sha512_hash(text):
    sha512_hash_object = hashlib.sha512()
    sha512_hash_object.update(text.encode('utf-8'))
    return sha512_hash_object.hexdigest()

def sha256_hash(text):
    sha256_hash = hashlib.sha356()
    sha256_hash.update(text.encode('utf-8'))
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    # Get user input for the text to be hashed
    input_text = input("Enter the text to be hashed: ")

    # Calculate hashes using different algorithms
    md5_hashed_text = md5_hash(input_text)
    sha1_hashed_text = sha1_hash(input_text)
    sha512_hashed_text = sha512_hash(input_text)
    sha256_hashed_text = sha256_hash(input_text)

    # Print the original text and its hashes
    print(f"Original Text: {input_text}")
    print(f"MD5 Hash: {md5_hashed_text}")
    print(f"SHA-1 Hash: {sha1_hashed_text}")
    print(f"SHA-512 Hash: {sha512_hashed_text}")
    print(f"SHA-512 Hash: {sha256_hashed_text}")
