#  <p align="center">🛣️ PEAJE VILLADA 2022 🛣️</p>
***

## 🖊️ INTRODUCCION 🖊️
Se nos planteo la siguiente [problematica](Consigna.pdf): un cliente que poseia la concesion de varias rutas de la provincia de cordoba necesitaba un sistema en el cual cada empleado pudiera cargar los autos que pasaran por cada casilla asignada en su turno. Cada casilla contaba con una computadora con Wndows 10 corriendo.Las tarifas que se cobran en estos peajes son marcadas por la ley provincial de transito Nro. 8560.
Como metodo de organizacion y control se nos pidio que generemos un reporte de recaudaciones para las estaciones con los numeros del dia.
## ⚙️ SOLUCION PROPUESTA ⚙️
Para resolver los problemas de esta empresa, nos propusimos crear un proyecto django. Este contiene la administracion de las estaciones de esta empresa, como tambien la utilidades necesarias para que el trabajador pueda ingresar a la pagina y cargar sus turnos y los tickets por cada dia laborable. Esta cuetna con una base de datos que posee la informacion de los trabajadores, estaciones y tickets guardados desde su implementacion. Con este sistema buscamos la mejora y facilidad para los empleados de cargar los autos que pasan por alli, como tambien la mejor organizacion en la administracion de la empresa mediante registros creados por nosotros de los registros de los autos.
La pagina cuenta con multiples views las cuales son ingreso de los tickets,informes, turnos y quejas, como tambien un administrador general. Tambien posee multiples informes por dia, estacion y turnob.
## 💻 INSTALACION 💻
``` bash
$ git clone https://github.com/tomasguell/Peaje_Villada_2022.git
$ cd ../Peaje_Villada_2022
$ pip install -r requirements.txt
$ cd ../Peaje_Villada_2022/AppPeaje
``` 
``` sql
$ CREATE USER 'bdi'@'localhost' IDENTIFIED BY 'pepe1234';
$ mysql -ubdi -ppepe1234
$ CREATE DATABASE Peaje;
``` 
``` bash
$ python3 manage.py migrate
$ python3 manage.py makemigrations
$ python3 manage.py runserver

```
## 📷 SCREENSHOT 📷
![Admin](Complementos/admin.png)
![Admin](Complementos/informe.png)
![Admin](Complementos/inicial.png)
![Admin](Complementos/quejas.png)
## 🦾 TECNOLOGIAS USADAS 🦾
```
> Python
> Django
> Sql
> UML
```
## 🧙‍♂️ CREADORES 🧙‍♂️
```
Tomas Guell
Francisco Giayetto
Facundo Oliva Marchetto
Agustin Odetti
```