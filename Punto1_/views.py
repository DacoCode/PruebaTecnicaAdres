import re
from django import forms
from django.shortcuts import render
from django.core.validators import EmailValidator
from django.http import HttpResponse

# Form para subir el archivo
class TXTUploadForm(forms.Form):
    file = forms.FileField()

# validación
def validate_txt(file):
    errors = []
    expected_columns = 5
    
    # para leer el archivo TXT
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = [line.split(',') for line in decoded_file]
    
    for row_num, row in enumerate(reader, start=1):
        if len(row) != expected_columns:
            errors.append(f"Fila {row_num}: Número incorrecto de columnas ({len(row)})")
            continue
        
        # Validaciones por columna
        if not re.match(r'^[0-9]{3,10}$', row[0]):
            errors.append(f"Fila {row_num}, Columna 1: Número entero inválido")
        try:
            EmailValidator()(row[1])
        except:
            errors.append(f"Fila {row_num}, Columna 2: Correo inválido")
        if row[2] not in ['CC', 'TI']:
            errors.append(f"Fila {row_num}, Columna 3: Tipo de documento inválido")
        try:
            value = int(row[3])
            if not (500000 <= value <= 1500000):
                errors.append(f"Fila {row_num}, Columna 4: Valor fuera de rango")
        except:
            errors.append(f"Fila {row_num}, Columna 4: No es un número válido")
        
    return errors


def upload_file(request):
    if request.method == 'POST':
        form = TXTUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            errors = validate_txt(file)
            if errors:
                return render(request, 'upload.html', {'form': form, 'errors': errors})
            else:
                return render(request, 'upload.html', {'form': form, 'success': "Archivo validado correctamente"})
    else:
        form = TXTUploadForm()
    return render(request, 'upload.html', {'form': form})
