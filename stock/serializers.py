from rest_framework import serializers
from .models import Firm, Category, Brand, Product, Stock

class FirmSerializer(serializers.ModelSerializer):
    class Meta :
        model = Firm
        fields = (
            "id",
            "name",
            "phone",
            "adress"
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = (
            "id",
            "name" )
        

class BrandSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Brand
        fields = (
            "id",
            "name" )

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    brand_id = serializers.IntegerField(write_only=True)
    class Meta :
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "category_id",
            "brand",
            "brand_id",
            "stockk"
        )

        # read_only_fields = ['stockk']

class StockSerializer(serializers.ModelSerializer):
    firm_id = serializers.IntegerField()
    product_id = serializers.IntegerField()

    class Meta :
        model = Stock
        fields =(
            'id',
            'user',
            'firm',
            'firm_id',
            'transaction',
            'product',
            'product_id',
            'quantitiy',
            'price',
            'price_total' )

        read_only_fields = ['price_total'] ## https://www.django-rest-framework.org/api-guide/serializers/ sayfainda "Specifying read only fields" bölümünde aciklama yaziyor!


    def validate(self, data):
        if data.get('transaction') == "O": #model choices den gelen "O", out islemi icin 
            product = Product.objects.get(id=data.get('product_id'))
            if data.get('quantitiy') > product.stockk:
                raise serializers.ValidationError(
                    f'Dont have enough stock. Current stock is {product.stockk}'
                )
        return data

                

        
