class Cipher:
    def encrypt(plain_text, key=16):
        encrypted = ""
        for c in plain_text:
            if c.isupper():
                c_index = ord(c) - ord('A')
                c_shifted = (c_index + key) % 26 + ord('A')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.islower():
                c_index = ord(c) - ord('a') 
                c_shifted = (c_index + key) % 26 + ord('a')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.isdigit():
                c_new = (int(c) + key) % 10
                encrypted += str(c_new)
            else:
                encrypted += c
        encrypted = base64.b64encode(base64.b32encode(bytes(encrypted, encoding='utf-8')))
        return encrypted