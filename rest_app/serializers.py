from rest_framework import serializers
from .models import Brand

class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    address = serializers.CharField(max_length=100)
    phone_number =  serializers.IntegerField()
    amount_earned = serializers.DecimalField(max_digits=10, decimal_places=2)

    date_created = serializers.DateTimeField()
    date_updated = serializers.DateTimeField()


class BrandValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    address = serializers.CharField(max_length=100)
    phone_number =  serializers.IntegerField()
    amount_earned = serializers.DecimalField(max_digits=10, decimal_places=2)

    date_created = serializers.DateTimeField(read_only=True)
    date_updated = serializers.DateTimeField(read_only=True)


# This is an improvement to BrandValidateSerializer (providing the create method)
class BrandValidateCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    address = serializers.CharField(max_length=100)
    phone_number =  serializers.IntegerField()
    amount_earned = serializers.DecimalField(max_digits=10, decimal_places=2)

    date_created = serializers.DateTimeField(read_only=True)
    date_updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Brand.objects.create(**validated_data)

"""BrandDemo and demo_serialization is just for elaboration purpose when I'm explaining serializers"""
class BrandDemoSerializer(serializers.Serializer):
    name = serializers.CharField()

class BrandDemo():
    def __init__(self, name):
        self.name = name


def demo_serialization():
    brand_demo = BrandDemo("Jane Doe")
    brand_serializer = BrandDemoSerializer(brand_demo)
    print(brand_serializer.data)