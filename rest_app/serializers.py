from rest_framework import serializers

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