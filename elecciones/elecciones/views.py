from django.shortcuts import render

def carga_datos(request):
    return render(request, 'elecciones/carga_datos.html', {})
