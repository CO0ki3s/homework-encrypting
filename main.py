from cryenurl import ProtectUidToUrl


if __name__ == "__main__":

    new_url = ProtectUidToUrl()

    url = input("Add URL: ")

    # encrypting url
    new_url = new_url.crypt_decrypt(url.split("=")[0], "crypt", url.split("=")[1])

    # preview of the part of the url that was encrypted
    print(f"\n{url.split('=')[1]} -> {new_url.split('=', 1)[1]}\n")

    # new URL after encrypting
    print(f"ENCRYPTED url: {new_url}")
