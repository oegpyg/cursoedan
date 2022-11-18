.Crear virtual enviroment
#windows
    py -m venv ve_cursoedan
#linux o mac
    python -m venv cursoedan

#activar entorno virtual
    windows
    .\cursoedan\Scripts\activate
    
    linux
    source cursoedan/bin/activate


pip install django


#crea el proyecto django
django-admin startproject cursoedan

.cd cursoedan

#creamos la aplicacion para manejar el proyecto
django-admin startapp fixtures


#migracion de los datos en la base de datos
    #carga los cambios realizados en un fixture
    python manage.py makemigrations

    #para aplicar los cambios en la base de datos
    python manage.py migrate

#crear el usuario administrador
python manage.py createsuperuser
    #obs: user: og password: @@123@@


#correr el servidor
python manage.py runserver 0.0.0.0:8000

#para instalar si descagan del git
pip install -r requirements.txt

para entrar en el admin
http://localhost:8000/admin