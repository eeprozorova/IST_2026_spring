def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_repeated = ""

    while len(keyword_repeated) < len(plaintext):
        keyword_repeated += keyword
    keyword_repeated = keyword_repeated[: len(plaintext)]

    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = keyword_repeated[i]
            shift = ord(key_char.lower()) - ord("a")
            if char.isupper():
                shifted = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            else:
                shifted = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            ciphertext += shifted
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_repeated = ""

    while len(keyword_repeated) < len(ciphertext):
        keyword_repeated += keyword
    keyword_repeated = keyword_repeated[: len(ciphertext)]

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = keyword_repeated[i]
            shift = ord(key_char.lower()) - ord("a")
            if char.isupper():
                shifted = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            else:
                shifted = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
            plaintext += shifted
        else:
            plaintext += char

    return plaintext
