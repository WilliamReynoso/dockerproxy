# dockerproxy
## Configurar un Docker con Nginx con el puerto 80 eh instalar dentro de ese Docker Python.
Se utilizaron 2 contenedores uno de Nginx y uno de python que se juntaron con docker-compose.
![imagen](https://github.com/user-attachments/assets/8cdcb61e-9dd6-44d0-a3e3-711c6c5330aa)

### En este caso no se creó un usuario ya que se trabajo directo con la imagen de python:3 en lugar de una distribución de linux.
![imagen](https://github.com/user-attachments/assets/11146687-1bb0-4ece-ac08-e5e0f37b0a37)

## Ejecutar el ejemplo de FLASK configurar proxy para responder por enpoint /pagina para resolver el puerto 5000 del FLASK.
Ejecutamos los contenedores con docker-compose y revisamos localhost/ y localhost/pagina
![imagen](https://github.com/user-attachments/assets/58050e39-1189-4e04-b396-e8ad19059463)

![imagen](https://github.com/user-attachments/assets/82660531-e8f9-4c33-8ba1-cebd71c70f8c)
![imagen](https://github.com/user-attachments/assets/878ce709-e8f7-49b7-9b2e-8898752718c7)
