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

        # the encryption key is associated with the uid - the part of the URL we are encrypting or decrypting
        key = self.key + uid
        if argname == "crypt":
            # XOR function which encrypts the necessary string
            xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(uid, cycle(str(key))))
            # method returns a bytearray object which is an array of the given bytes.
            bin_array = bytearray(xored, 'utf-8')
            # encode to Base64 format
            encode = base64.standard_b64encode(bin_array)
            # decode to utf-8 format
            final = encode.decode('utf-8')
            return url + "=" + final
        elif argname == "decrypt":
            # method returns a bytearray object which is an array of the given bytes.
            bin_array = bytearray(uid, 'utf-8')
            # decode from Base64 format
            decode = base64.standard_b64decode(bin_array)
            # decode to utf-8 format
            xored = decode.decode('utf-8')
            final = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(xored, cycle(str(key))))
            # again using the XOR function with the same encryption key returns the original value of the string
            return url + "=" + final
        else:
            print("bad arg")
