import os
import subprocess
import stat

def run(cmd):
    print(f"Ejecutando: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def instalar_apache():
    # Detectar distribución
    if os.path.exists("/etc/debian_version"):
        run("sudo apt update")
        run("sudo apt install -y apache2")
        run("sudo systemctl start apache2")
        run("sudo systemctl enable apache2")
    elif os.path.exists("/etc/redhat-release"):
        run("sudo yum install -y httpd")
        run("sudo systemctl start httpd")
        run("sudo systemctl enable httpd")
    else:
        print("Distro no soportada")
        exit(1)

def crear_pagina():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>DevOps</title>
    </head>
    <body>
        <h1>¡Hola!</h1>
    </body>
    </html>
    """
    with open("/tmp/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    run("sudo mv /tmp/index.html /var/www/html/index.html")

if __name__ == "__main__":
    instalar_apache()
    crear_pagina()

# Otorgar permisos de ejecución al script
    script_path = os.path.realpath(__file__)
    os.chmod(script_path, os.stat(script_path).st_mode | stat.S_IEXEC)