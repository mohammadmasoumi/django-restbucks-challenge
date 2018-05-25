from django.conf.urls import url
from django.urls import include
from .views.user import CreateUserAPIView, UserRetrieveUpdateAPIView, authenticate_user, UserViewSet
from .views.product import ProductViewSet, CategoryViewSet, ProductCustomizationViewSet, CreateProductAPIView, \
    CreateCategoryAPIView, CreateProductCustomizationAPIView
from .views.order import OrderViewSet, UserCheckListViewSet, CreateCheckListOrderAPIView, view_his_order
from rest_framework import routers

# routers
router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_customizations', ProductCustomizationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_checklist', UserCheckListViewSet)

# restframework url patterns
urlpatterns = [
    # used for creating user
    url(r'^create_user/$', CreateUserAPIView.as_view(), name='create'),

    # used for obtaining user jwt Token
    url(r'^obtain_token_user/$', view=authenticate_user, name='obtain_token'),

    # used for updating or getting user information
    url(r'^update_user/$', UserRetrieveUpdateAPIView.as_view(), name='update'),

    # used for creating category [Category -> Product -> ProductCustomization]
    url(r'^create_category/$', CreateCategoryAPIView.as_view(), name='category'),

    # used for creating product [Category -> Product -> ProductCustomization]
    url(r'^create_product/$', CreateProductAPIView.as_view(), name='product'),

    # used for creating product customization [Category -> Product -> ProductCustomization]
    url(r'^create_product_customization/$', CreateProductCustomizationAPIView.as_view(), name='product_customization'),

    # used for ordering
    url(r'^create_order_checklist/$', CreateCheckListOrderAPIView.as_view(), name='create_order_checklist'),

    # used for review the orders and billing list
    url(r'^view_orders/$', view=view_his_order, name='view_order'),

    # including routers URL
    url(r'^', include(router.urls))
]
