#!/usr/bin/env python3
import os   

def discover(initial_path, extensions=None):
    # Lista de extensões padrão (só usamos se nada for passado)
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

            # Código e configs
            "py", "js", "java", "c", "cpp", "cs", "html", "css", "json", "xml", "yml"
        ]

    for dirpath, dirs, files in os.walk(initial_path):
        for file in files:
            full_path = os.path.abspath(os.path.join(dirpath, file))

            # Pega apenas a extensão
            ext = full_path.split('.')[-1].lower()

            if ext in extensions:
                yield full_path
