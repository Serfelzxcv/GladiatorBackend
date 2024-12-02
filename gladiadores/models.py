from django.db import models # type: ignore

# Create your models here.
class Gladiador(models.Model):
    name                = models.CharField(max_length=100)
    health              = models.IntegerField()
    attackPower         = models.IntegerField()
    specialMoveChance   = models.FloatField()
    subclass            = models.CharField(max_length=50)
    imagePath           = models.BinaryField()  # Para almacenar la URL de la imagen
    

    def __str__(self):
        return self.name
    