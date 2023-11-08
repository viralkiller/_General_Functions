from cryptography.fernet import Fernet


class Encryptor:

    def __init__(self):

        self.alpha_mass = 'sfbenf/cvhgjyft/l'

    def encrypt_String(self,input_string):

        gibl = ''.join(chr(ord(letter)-1) for letter in self.alpha_mass)

        #encode string to bytes
        encoded = input_string.encode()

        #get key
        file = open(gibl,'rb')
        key = file.read()
        file.close()

        #encrypt with key
        f = Fernet(key)
        encrypted = f.encrypt(encoded)

        return encrypted

    def decrypt_String(self,encrypted_string):

        gibl = ''.join(chr(ord(letter)-1) for letter in self.alpha_mass)

        #get key
        file = open(gibl,'rb')
        key = file.read()
        file.close()

        f = Fernet(key)
        decrypted = decrypted = f.decrypt(encrypted_string)

        #encode from bytes to text
        original_string = decrypted.decode()

        return original_string


    def decrypt_Bytes_As_String(self,encrypted_string):



        filter_string = str(encrypted_string)[2:-1]
        #print(filter_string)
        as_bytes = filter_string.encode('utf_8')
        #print(as_bytes)
        decrypt_a_string = self.decrypt_String(as_bytes)
        #print(decrypt_a_string)
        return decrypt_a_string


    def decrypt_Bytes_As_String_Special(self,encrypted_string):



        filter_string = str(encrypted_string)[2:-1]
        encrypted_string = encrypted_string.replace('"',"'")
        print(filter_string)
        as_bytes = filter_string.encode('utf_8')
        print(as_bytes)
        decrypt_a_string = self.decrypt_String(as_bytes)
        print(decrypt_a_string)
        return decrypt_a_string

    def de_Priv_Keys(self):
        pass




if __name__ == '__main__':

    e = Encryptor()

    encrypt_a_string = e.encrypt_String('lCGByoVq2cOc6QtGCdXtokHMurKYmp7kIHDw0CNjvvAm2kBhVol6QbushZIKAuOu')
    print(encrypt_a_string)
    #my_string = "b'gAAAAABik357B5syzTrLmCtP3OmyD7oBQQqXhtngCW2Tnjm10EREAnODFawGqRGw0PerGJrwyq9RtUXrblTEHAY1-MDL897z6kwHFN8luMR7HgjmZI9H5cH-3W86Z-BQrOI-P1lWCXfffhdrHSsxl79B3FVZsPNxBs5WCXNh9-QsHsLTOBgmmyg='"
    #my_string = "b'gAAAAABi1JNKnApHeUAz_a2LhWbqhdE-tjpLNHLSmCl1d30BRiA4PtW2JKydBX6klujMJLFVSNyGxtGvZXC8DxeBa1MGvJdkBQET_L-pBg3oxNc3pmVRNZowCj6N8DRfg7dpSEq41KqsjlXjSUkaBaF32OYrQmd3WQtSpmPf1XI1rECBI72VOlM='"
    #dec = e.decrypt_Bytes_As_String(my_string)
    #print(dec)

    encrypt_a_string = e.encrypt_String('43KcpNCCS3OUahHt8d8NJr0YwpXXQdrXICqGkJyHlaQLziLaQyQqjzBOrUiFUr3b')
    print(encrypt_a_string)







