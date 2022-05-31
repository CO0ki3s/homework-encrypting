from cryenurl import ProtectUidToUrl
import time

new_url = ProtectUidToUrl()

# loading test urls from a text file
lines = open('urls.txt', 'r')

for url in lines:

    # encrypting url
    nurl = new_url.crypt_decrypt(url.split("\n")[0].split("=")[0], "crypt", url.split("\n")[0].split("=")[1])
    print("---------------------------------------")
    print("DECRYPTED url:", url.split('\n')[0])
    print(f"ENCRYPTED url: {nurl}")

    # decrypting url and check
    ourl = new_url.crypt_decrypt(nurl.split("=")[0], "decrypt", nurl.split("=", 1)[1])
    print(url.split("\n")[0].split("=")[1] + " -> " + nurl.split("=", 1)[1] + " -> " + ourl.split("=", 1)[1])

    if url.split('\n')[0].split("=")[1] == ourl.split("=")[1]:
        print("OK")
    else:
        print("BAD")

    time.sleep(0.5)
