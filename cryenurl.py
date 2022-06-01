import base64
from itertools import cycle


class ProtectUidToUrl:
    """
    With this class you call a function to encrypt and decrypt the ID in your URL
    """
    def __init__(self):

        # secret key
        # you can change this key to any string
        self.key = "Cookiesarebetterthaneverythingelse"

    def crypt_decrypt(self, url: str, argname: str, uid: str) -> str:

        """
        Crypt and decrypt object.

        :param url: The part of the url that is without id
        :type url: str
        :param argname: Choice between encryption and decryption -> "crypt" or "decrypt"
        :type argname: str
        :param uid: The part of the URL to work with
        :type uid: str
        :return: Returns an encrypted or decrypted URL
        """

        key = self.key + uid
        if argname == "crypt":
            xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(uid, cycle(str(key))))
            bin_array = bytearray(xored, 'utf-8')
            encode = base64.standard_b64encode(bin_array)
            final = encode.decode('utf-8')
            return url + "=" + final
        elif argname == "decrypt":
            bin_array = bytearray(uid, 'utf-8')
            decode = base64.standard_b64decode(bin_array)
            xored = decode.decode('utf-8')
            final = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(xored, cycle(str(key))))
            return url + "=" + final
        else:
            print("bad arg")
