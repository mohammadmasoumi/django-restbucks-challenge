from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from ..serializers.order import OrderSerializer, OrderCheckListSerializer
from ..models import Order, OrderCheckList
import json


class OrderViewSet(viewsets.ModelViewSet):
    """
        Create ViewSet of Order Model
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserCheckListViewSet(viewsets.ModelViewSet):
    """
        Create ViewSet of OrderCheckList Model
    """

    queryset = OrderCheckList.objects.all()
    serializer_class = OrderCheckListSerializer


class CreateCheckListOrderAPIView(APIView):
    """
        Creating Order
    """

    # authenticated with jwt web token
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        # request.data
        json_request = request.data

        # response
        response = {}

        # list of products in order
        product_list = []

        # order information
        order = {}

        # order information
        order.update(
            {
                "user": request.user.id,
                "status": json_request["status"],
                "consume_location": json_request["consume_location"],
                "order_number": json_request["order_number"]
            }
        )

        # serializing Order model
        order_serializer = OrderSerializer(data=order)
        order_serializer.is_valid(raise_exception=True)
        order_serializer.save()

        # order checklist information
        order_check_list = {}

        # for each product in order
        # serialize OrderCheckList
        for item in json_request['content']:
            order_check_list.update(
                {
                    "order": json_request["order_number"],
                    "product_customization": item["product_customization"],
                    "number": item["number"]
                }
            )
            # Serializing OrderCheckList model
            checklist_serializer = OrderCheckListSerializer(data=order_check_list)
            checklist_serializer.is_valid(raise_exception=True)
            checklist_serializer.save()

            # append serialized order checklist into product_list
            product_list.append(checklist_serializer.data)

        # update response
        response.update({
            "products": product_list,
            "user": request.user.id,
            "status": json_request["status"],
            "consume_location": json_request["consume_location"],
            "order_number": json_request["order_number"]

        })

        # return Response
        return Response(response, status=status.HTTP_201_CREATED)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated, ])
def view_his_order(request):
    """
        used for getting checkout list(product list, pricing & order status)
    :param request: request content:(user information)
    :return: checkout list
    """

    # requested user
    user = request.user

    # all orders of requested user
    orders = Order.objects.filter(user=user)

    # response
    response = []

    # products information per order
    products = {}

    # list of products information per order
    products_list = []

    # order information
    items = {}

    # for every order get orderCheckList
    # for every orderCheckList get productCustomization
    for order in orders:
        order_checklist = OrderCheckList.objects.filter(
            order=order
        )
        products_list.clear()
        for product in order_checklist:

            # productCustomization information per order
            products.update({
                "product": product.product_customization.product.name,
                "customizable": product.product_customization.customizable,
                "is_available": product.product_customization.is_available,
                "price": product.product_customization.price,
            })
            products_list.append(products)

        # order information
        items.update({
            "products": products_list,
            "bill": order.bill,
            "status": order.STATUS_CHOICES[order.status][1]
        })

        response.append(items)

    # return Response
    return Response(json.dumps(response), status=status.HTTP_200_OK)
