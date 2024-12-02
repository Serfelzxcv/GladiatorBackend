# gladiadores/serializers.py
from rest_framework import serializers
from .models import Gladiador

class GladiatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gladiador
        fields = ['name', 'health', 'attackPower', 'specialMoveChance', 'subclass', 'imagePath']
        # Si el campo 'imagePath' está almacenado como BinaryField, no se necesita ninguna modificación adicional,
        # pero si es un ImageField, puedes usar el siguiente para manejar el archivo correctamente:
        # extra_kwargs = {'imagePath': {'required': False}}

    # Si se requiere una validación especial para la imagen, puedes agregarla aquí.
    def validate_imagePath(self, value):
        if isinstance(value, bytes):
            # Puedes hacer validaciones de los bytes de la imagen aquí si es necesario
            return value
        raise serializers.ValidationError("El archivo de imagen no es válido.")
