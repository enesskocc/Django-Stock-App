# from django.urls import path, include

# urlpatterns = [
# ]

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# after '/stock/':
router.register('firm', FirmView)
router.register('category', CategoryView)
router.register('brand', BrandView)
router.register('product', ProductView)
router.register('stock', StockView)

urlpatterns = router.urls