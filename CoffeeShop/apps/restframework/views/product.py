from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..serializers.product import CategorySerializer, ProductSerializer, ProductCustomizationSerializer
from ..models import Product, ProductCustomization, Category


class CategoryViewSet(viewsets.ModelViewSet):
    """
        Create ViewSet of Category Model
    """

    # authenticate user with JWT token
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
        Create ViewSet of Product Model
    """

    # authenticate user with JWT token
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCustomizationViewSet(viewsets.ModelViewSet):
    """
        Create ViewSet of ProductCustomization Model
    """
    # authenticate user with JWT token
    permission_classes = (IsAuthenticated,)
    queryset = ProductCustomization.objects.all()
    serializer_class = ProductCustomizationSerializer


class CreateCategoryAPIView(APIView):
    """
        serialize and save Category
    """

    # authenticate user with JWT token
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        category = request.data
        serializer = CategorySerializer(data=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateProductAPIView(APIView):
    """
        serialize and save Product
    """

    # authenticate user with JWT token
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        products = request.data
        response = []
        for product in products:
            serializer = ProductSerializer(data=product)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response.append(serializer.data)

        return Response(response, status=status.HTTP_200_OK)


class CreateProductCustomizationAPIView(APIView):
    """
        serialize and save ProductCustomization
    """

    # authenticate user with JWT token
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        product_customizations = request.data

        response = []
        for product_customization in product_customizations:
            serializer = ProductCustomizationSerializer(data=product_customization)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response.append(serializer.data)

        return Response(response, status=status.HTTP_200_OK)
