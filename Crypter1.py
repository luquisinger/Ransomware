from Crypto.Cipher import AES

class Crypter:
    def __init__(self, key, ctr):
        self.cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

    def encrypt(self, data):
        return self.cipher.encrypt(data)

    def decrypt(self, data):
        return self.cipher.decrypt(data)


def change_files(filename, cryptoFn, block_size=16):
    with open(filename, "r+b") as f:
        block = f.read(block_size)

        while block:
            out = cryptoFn(block)

            if len(out) != len(block):
                raise ValueError("Block size mismatch.")

            f.seek(-len(block), 1)
            f.write(out)
            block = f.read(block_size)
