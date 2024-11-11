from django.db import models

class Usuario(models.Model):
    GRADO_CHOICES = [
        ('R', 'Recluta'),
        ('S', 'Soldado'),
        ('C', 'Cabo'),
        ('Sgto', 'Sargento'),
        # Agregar más opciones según sea necesario
    ]

#codigo unico del usuario que se puede insertar por el usuario y tiene por defecto null

    codigo_usuario = models.CharField(max_length=20, unique=True, blank=False, default='')
    nombre = models.CharField(max_length=100)
    rango = models.CharField(max_length=10, choices=GRADO_CHOICES)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    unidad = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    grupo_sanguineo = models.CharField(max_length=5)
    alergias = models.TextField(blank=True, null=True)
    condiciones_medicas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.codigo_usuario+' '+self.nombre
