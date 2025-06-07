#Calculadora Web de Raíces de Funciones con Métodos Numéricos

Este es un proyecto web desarrollado con **Django** que permite calcular raíces de funciones utilizando los métodos de:

- Bisección  
- Newton-Raphson  
- Newton-Raphson Modificado

Algo muy bueno de este proyecto es que nos muestra la tabla de las iteraciones y la gráfica correspondiente de la función

Qué opciones son las que puedes realizar en la pagína:
- Ingresar funciones
- Seleccionar el método de cálculo
- Visualizar la **raíz aproximada**
- Ver una **tabla de iteraciones**
- Analizar la **gráfica de la función** con la raíz marcada

---
Ahora bien, si deseas utilizar esta calculadora estos son los pasos para poder utilizarla en tu pc:

Antes que nada debes tener instalado Visual Stude Code, allí es donde cargarás todo los archivos correspondientes

1. Clona este repositorio:

git clone https://github.com/JoshGab05/CalculadoraRaicesDjango.git
cd CalculadoraRaicesDjango

2. Crea y activa un entorno virtual:
py -m venv venv
venv\Scripts\activate

3. Instala los requisitos:
pip install -r requirements.txt

4. Ejecuta el servidor:
python manage.py runserver

5. Abre tu navegador en:
http://127.0.0.1:8000

Esta debe ser la estructura del proyecto que debes tener para poder utilizarla
CalculadoraDJangoFinal/
├── operaciones/
│   ├── views.py
│   ├── metodos/
│   │   ├── biseccion.py
│   │   ├── newton.py
│   │   └── newton_modificado.py
│   ├── graficas.py
├── templates/
│   └── calculadora_nueva.html
├── static/
│   └── graficas/
├── manage.py

