from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import filters ## search icin
from django_filters.rest_framework import DjangoFilterBackend ## filter icin
from .models import Firm, Category, Brand, Product, Stock
from .serializers import FirmSerializer, CategorySerializer, BrandSerializer, ProductSerializer, StockSerializer


class FirmView(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = [permissions.DjangoModelPermissions] ## modelde kimi yetkilendirdiysek, ona göre yetki verecek!

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = [permissions.DjangoModelPermissions]

class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = [permissions.DjangoModelPermissions]

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "brand"] ## settinge de ekleme yapildi!
    search_fields = ["name"]
    permission_classes = [permissions.DjangoModelPermissions]

class StockView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["firm", "transaction", "product"]  
    search_fields = ["firm"] 
    permission_classes = [permissions.DjangoModelPermissions]


    def perform_create(self, serializer):   #transaction islemini yapan userı kayıt ediyor
        serializer.save(user=self.request.user)
