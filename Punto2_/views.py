from django.shortcuts import render
import os
import re
import fitz  # instale lib PyMuPDF
import django

# Configurar Django para acceder a la base de datos del proyecto 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adresMySite.settings")
django.setup()

from Punto2_.models import Punto2Pdf  # Importar el modelo del archivo Punto2_/models.py

CARPETA_FACTURAS = "./PDF"
CUFE_REGEX = re.compile(r"\b([0-9a-fA-F]\n*){95,100}\b")

def extraer_texto_pdf(ruta_pdf):
    with fitz.open(ruta_pdf) as doc:
        texto = ""
        for pagina in doc:
            texto += pagina.get_text("text")
    return texto

def extraer_cufe(texto):
    match = CUFE_REGEX.search(texto)
    return match.group(0) if match else "CUFE_NO_ENCONTRADO"

def procesar_pdfs():
   
    for archivo in os.listdir(CARPETA_FACTURAS):
        if archivo.lower().endswith(".pdf"):
            ruta_pdf = os.path.join(CARPETA_FACTURAS, archivo)

            # Verificar si el archivo ya existe en la BD para evitar duplicados al momento de cargar
            if not Punto2Pdf.objects.filter(Nombre_archivo=archivo).exists():
                texto = extraer_texto_pdf(ruta_pdf)
                cufe = extraer_cufe(texto)

                # save en la base de datos
                Punto2Pdf.objects.create(
                    Nombre_archivo=archivo,
                    Numero_paginas=fitz.open(ruta_pdf).page_count,
                    CUFE=cufe,
                    Peso_archivo=os.path.getsize(ruta_pdf) / 1024  # Peso se divide en 1024 oara verlo en KB
                )

def lista_pdfs(request):
    
    procesar_pdfs()  # Ejecutar la extracción y guardado de PDFs antes de mostrar la lista
    facturas = Punto2Pdf.objects.all()
    return render(request, "lista_pdfs.html", {"facturas": facturas}) #Se muestra en la web
