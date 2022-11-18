#Crear virtual enviroment
##windows
    py -m venv ve_cursoedan
##linux o mac
    python -m venv cursoedan

#Activar entorno virtual
##windows
    .\cursoedan\Scripts\activate
    
##linux
    source cursoedan/bin/activate


pip install django


#Crear el proyecto django
    django-admin startproject cursoedan

    cd cursoedan

#Creamos la aplicacion para manejar el proyecto
    django-admin startapp fixtures


#Migracion de los datos en la base de datos
##Carga los cambios realizados en un fixture
    python manage.py makemigrations

##Para aplicar los cambios en la base de datos
    python manage.py migrate

#Crear el usuario administrador
    python manage.py createsuperuser
##Obs: user: og password: @@123@@


#Correr el servidor
    python manage.py runserver 0.0.0.0:8000

#Para instalar si descagan del git
    pip install -r requirements.txt

#Para entrar en el admin
    http://localhost:8000/admin