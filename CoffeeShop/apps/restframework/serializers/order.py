from rest_framework import serializers
from ..models import Order, OrderCheckList


class OrderSerializer(serializers.ModelSerializer):
    """
        Serialize Order Model into JSON field
    """

    class Meta(object):
        model = Order
        fields = '__all__'


class OrderCheckListSerializer(serializers.ModelSerializer):
    """
            Serialize OrderCheckList Model into JSON field
    """
    class Meta:
        model = OrderCheckList
        fields = '__all__'

