from django.shortcuts import render
import sympy as sp
import re

from .metodos.biseccion import metodo_biseccion
from .metodos.newton import metodo_newton_raphson
from .metodos.newton_modificado import metodo_newton_raphson_modificado
from .graficas import generar_grafica

def corregir_expresion(expresion):
    expresion = expresion.replace('^', '**')
    expresion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expresion)
    expresion = re.sub(r'([a-zA-Z])\(', r'\1*(', expresion)
    expresion = re.sub(r'\)([a-zA-Z])', r')*\1', expresion)
    return expresion

def convertir_funcion(expresion):
    x = sp.symbols('x')
    funcion_simbolica = sp.sympify(expresion)
    return sp.lambdify(x, funcion_simbolica, 'math'), sp.lambdify(x, funcion_simbolica.diff(x), 'math')

def calculadora(request):
    resultado = None
    mensaje_error = None
    imagen_grafica = None
    tabla_iteraciones = None

    if request.method == 'POST':
        try:
            expresion_funcion = request.POST.get('funcion')
            expresion_funcion = corregir_expresion(expresion_funcion)

            metodo = request.POST.get('metodo')
            cantidad_iteraciones = int(request.POST.get('iteraciones', 10))

            funcion_evaluable, derivada_funcion = convertir_funcion(expresion_funcion)

            if metodo == 'newton':
                valor_inicial = float(request.POST.get('x0'))
                resultado, tabla_iteraciones = metodo_newton_raphson(funcion_evaluable, derivada_funcion, valor_inicial, cantidad_iteraciones)

            elif metodo == 'newton_modificado':
                valor_inicial = float(request.POST.get('x0'))
                resultado, tabla_iteraciones = metodo_newton_raphson_modificado(funcion_evaluable, derivada_funcion, valor_inicial, cantidad_iteraciones)

            elif metodo == 'biseccion':
                limite_inferior = float(request.POST.get('a'))
                limite_superior = float(request.POST.get('b'))
                resultado, tabla_iteraciones = metodo_biseccion(funcion_evaluable, limite_inferior, limite_superior, cantidad_iteraciones)

            imagen_grafica = generar_grafica(funcion_evaluable)

        except Exception as error:
            mensaje_error = f"Error: {str(error)}"

    return render(request, 'calculadora_nueva.html', {
        'resultado': resultado,
        'mensaje_error': mensaje_error,
        'imagen_grafica': imagen_grafica,
        'tabla_iteraciones': tabla_iteraciones,
    })
