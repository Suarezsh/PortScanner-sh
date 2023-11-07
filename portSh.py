#fines de prueba {sh}
import socket
from urllib.parse import urlparse

url = input('Ingrese el URL del sitio: ')
parsed_url = urlparse(url)
target = parsed_url.netloc

try:
    target_IP = socket.gethostbyname(target)
    print('sh>> Comenzando el escaneo en el host:', target_IP)

    for port in range(1, 100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target_IP, port))
        if result == 0:
            print('sh>> Puerto {} esta abierto'.format(port))
        s.close()

except socket.gaierror:
    print('Error: Nombre o servicio no reconocido. Por favor, introduce una URL válida.')
