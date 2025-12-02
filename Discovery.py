#!/usr/bin/env python3

import os   
print("Executando arquivo:", __file__)
def discover(inicial_path, extensions=None):
     # Lista de extensões padrão
    if extensions is None:
        extensions = [
            # Documentos
            "txt", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
            "odt", "ods", "odp", "rtf", "csv", "md",

            # Imagens
            "jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg",

            # Áudio
            "mp3", "wav", "aac", "flac", "ogg", "m4a",

            # Vídeo
            "mp4", "mkv", "mov", "avi", "wmv", "flv",

            # Arquivos compactados
            "zip", "rar", "7z", "tar", "gz",

            # Código (úteis para análise/logs/estudo)
            "py", "js", "java", "c", "cpp", "cs", "html", "css", "json", "xml", "yml"
        ]

    for dirpath, dirs, files in os.walk(inicial_path):
        for file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, file))
            ext = absolute_path.split('.')[-1].lower()
            if ext in extensions:
                yield absolute_path

if __name__ == "__main__":
    x = discover(os.getcwd())
    for i in x:
        print(i)