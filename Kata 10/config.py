def main():
   try:
     configuration = open('config.txt.')
   except FileNotFoundError:
        print("¡No se pudo localizar el archivo config.txt!")
   except IsADirectoryError:
        print("¡Se encontro config.txt, pero es un directorio, no se puede leer")
   except(BlockingIOError, TimeoutError):
        print("Sistema de archivos con carga alta, no se puede leer el archivo de configuración")
