from django.core.validators import MinValueValidator
from django.db import models
from django.core.mail import send_mail
from .product import ProductCustomization
from .user import MyUser


# Create your models here.

class Order(models.Model):
    # dictionary for casting status into integer
    STATUS = {
        'WAITING': 0,
        'PREPARATION': 1,
        'READY': 2,
        'DELIVERED': 3,
        'CANCELED': 4,
    }

    # status choices
    STATUS_CHOICES = (
        (STATUS['WAITING'], 'waiting'),
        (STATUS['PREPARATION'], 'preparation'),
        (STATUS['READY'], 'ready'),
        (STATUS['DELIVERED'], 'delivered'),
        (STATUS['CANCELED'], 'canceled'),
    )

    # dictionary for casting consume_location into integer
    CONSUME_LOCATION = {
        'TAEE_AWAY': 0,
        'IN_SHOP': 1,
    }

    # consume_location choices
    CONSUME_LOCATION_STATUS = (
        (CONSUME_LOCATION['TAEE_AWAY'], 'take_away'),
        (CONSUME_LOCATION['IN_SHOP'], 'in_shop'),
    )

    # number of order , order id
    order_number = models.PositiveSmallIntegerField(
        'order_number',
        primary_key=True,
        validators=[MinValueValidator(1)],
    )

    # order status
    # Choices : 0-WAITING, 1-PREPARATION, 2-READY, 3-DELIVERED, 4-CANCELED
    status = models.PositiveSmallIntegerField(
        'status',
        choices=STATUS_CHOICES
    )

    # order consume_location
    # Choices : 0-TAEE_AWAY 1-IN_SHOP
    consume_location = models.PositiveSmallIntegerField(
        'consume_location',
        choices=CONSUME_LOCATION_STATUS
    )

    # order user
    # foreign key into user.MyUser
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name=('order_user')
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.order_number)

    def __unicode__(self):
        return str(self)

    # override save method
    # whenever status changed into "canceled" an emil will send into user
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.order_number:

            # save previous state
            old_instance = Order.objects.filter(order_number=self.order_number).first()

            if old_instance:
                # compare previous state with current state
                if old_instance.status != 4 and self.status == 4:
                    print("Sending Email Function Called")

                    try:
                        send_mail('subject', 'body of the message', 'mohammad.masoomy74@gmail.com',
                                  [self.user.email, ])
                    except:
                        print("Sending Email Failed")

        super(Order, self).save()

    @property
    def is_canceled(self):
        """
            check cancellation of order
        :return: True id order canceled
        """

        if self.status == self.STATUS['CANCELED']:
            return True
        else:
            return False

    @property
    def bill(self):
        """
            calculate bill
        :return: bill
        """

        return sum([product.price * product.number for product in self.order_content.all()])


class OrderCheckList(models.Model):
    # foreign key to order.Order model
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='order_content'
    )

    # foreign key to product.ProductCustomization
    product_customization = models.ForeignKey(
        ProductCustomization,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='order_product'
    )

    # number of product customization
    number = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        default=1
    )

    # price of product customization
    price = models.PositiveSmallIntegerField(
        default=5000
    )

    class Meta:
        verbose_name = 'OrderCheckList'
        verbose_name_plural = 'OrderCheckList'

    def __str__(self):
        return str(self.product_customization)

    def __unicode__(self):
        return str(self)
