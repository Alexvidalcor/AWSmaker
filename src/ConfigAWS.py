import subprocess
from pathlib import Path
import getpass as gp

def CheckDirectories():
    mainUser = gp.getuser()
    if Path(f"/home/{mainUser}/.aws").exists():
        print("Carpeta AWS detectada")    
    else:
        print("¿Primera vez en AWS? Creando directorios...")
        Path(f"/home/{mainUser}/.aws").mkdir(parents=True, exist_ok=True)
        print("OK")

def CreateCredentials(keyID, accessID):
    try:
        f = open(f"/home/{gp.getuser()}/.aws/credentials", "x+")
        print("Escribiendo nuevas credenciales...")
        f.write("[default]\n")
        f.write(f"aws_access_key_id = {keyID}\n")
        f.write(f"aws_secret_access_key = {accessID}\n")
        f.close
        print("OK")

    except FileExistsError:
        print("Modificando viejas credenciales...")
        Path(f"/home/{gp.getuser()}/.aws/credentials").unlink()
        f = open(f"/home/{gp.getuser()}/.aws/credentials", "x+")
        f.write("[default]\n")
        f.write(f"aws_access_key_id = {keyID}\n")
        f.write(f"aws_secret_access_key = {accessID}\n")
        f.close
        print("OK")

def AskCredentials():
    keyPass = gp.getpass("Introduce key: ")
    accessPass = gp.getpass("Introduce access: ")
    tokenPass = gp.getpass("Introduce tu token")
    return keyPass, accessPass, tokenPass

if __name__ == "__main__":
    createdCheck = CheckDirectories()
    accessPass, keyPass = AskCredentials()
    if keyPass != "" and accessPass != "":
        CreateCredentials(keyPass, accessPass)
    else:
        print("Credenciales vacías. Programa terminado")