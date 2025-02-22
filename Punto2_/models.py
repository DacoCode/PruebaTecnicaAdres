from django.db import models


class Punto2Pdf(models.Model):
    Nombre_archivo = models.CharField(max_length=200, default="Sin Nombre")
    Numero_paginas = models.IntegerField(default=0)
    CUFE = models.TextField(default="SIN_CUFE", null=True, blank=True)
    Peso_archivo = models.FloatField(default=0.1) 