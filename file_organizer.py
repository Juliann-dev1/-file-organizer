import shutil
import os
documentos_carpeta = input("Enter the documents folder name: ")
fotos_carpeta = input("Enter the photos folder name: ")
videos_carpeta = input("Enter the videos folder name: ")
musica_carpeta = input("Enter the music folder name: ")

if not os.path.exists(documentos_carpeta):    
    os.makedirs(documentos_carpeta)
if not os.path.exists(videos_carpeta):    
    os.makedirs(videos_carpeta)
if not os.path.exists(fotos_carpeta):    
    os.makedirs(fotos_carpeta)
if not os.path.exists(musica_carpeta):    
    os.makedirs(musica_carpeta)

extensiones_documentos = (".txt", ".pdf", ".doc", ".docx", ".odt", ".rtf", ".md", ".ppt", ".pptx", ".xls", ".xlsx", ".csv")
extensiones_fotos = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg")
extensiones_videos = (".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpeg")
extensiones_musica = (".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a")

archivos = os.listdir()

for archivo in archivos:
    if archivo.endswith(extensiones_documentos):
        shutil.move(archivo,documentos_carpeta)
        print(f"Moved file: {archivo} to folder {documentos_carpeta}")
    elif archivo.endswith(extensiones_musica):
        shutil.move(archivo, musica_carpeta)
        print(f"Moved file: {archivo} to folder {musica_carpeta}")
    elif archivo.endswith(extensiones_fotos):
        shutil.move(archivo,fotos_carpeta)
        print(f"Moved file: {archivo} to folder {fotos_carpeta}")
    elif archivo.endswith(extensiones_videos):
        shutil.move(archivo,videos_carpeta)
        print(f"Moved file: {archivo} to folder {videos_carpeta}")
print("All operations completed successfully!")