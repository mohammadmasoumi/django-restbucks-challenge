from django.test import TestCase

# Create your tests here.


from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from rest_framework_jwt import utils
from rest_framework_jwt.compat import get_user_model

from CoffeeShop import settings as main_settings

MyUser = get_user_model()
from .models.product import Category, Product, ProductCustomization
from .models.order import Order

factory = APIRequestFactory()


class CoffeeShopRESTAPITests(TestCase):

    def setUp(self):
        """
            setup test database
        """
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.email = 'mohammad.masoomy74_test@gmail.com'
        self.first_name = 'mohammad_test'
        self.last_name = 'masoumi_test'
        self.date_of_birth = '1996-12-12'
        self.password = 'mmmm1374'
        self.user = MyUser.objects.create_user(email=self.email, date_of_birth=self.date_of_birth,
                                               first_name=self.first_name, last_name=self.last_name,
                                               password=self.password)

        self.category = Category.objects.create(name='royal_test')

        self.product1 = Product.objects.create(name='Latte_test', category=self.category)
        self.product2 = Product.objects.create(name='Cappuccino_test', category=self.category)
        self.product3 = Product.objects.create(name='Espresso_test', category=self.category)
        self.product4 = Product.objects.create(name='Tea_test', category=self.category)
        self.product5 = Product.objects.create(name='Hot chocolate_test', category=self.category)
        self.product6 = Product.objects.create(name='Cookie_test', category=self.category)

        self.product_customization1 = ProductCustomization.objects.create(
            product=self.product1,
            customizable='skim_test',
            price=5000,
            is_available=True
        )
        self.product_customization2 = ProductCustomization.objects.create(
            product=self.product1,
            customizable='semi_test',
            price=5000,
            is_available=True
        )
        self.product_customization3 = ProductCustomization.objects.create(
            product=self.product1,
            customizable='whole_test',
            price=5000,
            is_available=True
        )
        self.product_customization4 = ProductCustomization.objects.create(
            product=self.product2,
            customizable='small_test',
            price=5000,
            is_available=True
        )
        self.product_customization5 = ProductCustomization.objects.create(
            product=self.product2,
            customizable='medium_test',
            price=5000,
            is_available=True
        )
        self.product_customization6 = ProductCustomization.objects.create(
            product=self.product2,
            customizable='large_test',
            price=5000,
            is_available=True
        )
        self.product_customization7 = ProductCustomization.objects.create(
            product=self.product3,
            customizable='single_test',
            price=5000,
            is_available=True
        )
        self.product_customization8 = ProductCustomization.objects.create(
            product=self.product3,
            customizable='double_test',
            price=5000,
            is_available=True
        )
        self.product_customization9 = ProductCustomization.objects.create(
            product=self.product3,
            customizable='triple_test',
            price=5000,
            is_available=True
        )
        self.product_customization10 = ProductCustomization.objects.create(
            product=self.product4,
            customizable='single_test',
            price=5000,
            is_available=True
        )
        self.product_customization11 = ProductCustomization.objects.create(
            product=self.product5,
            customizable='small_test',
            price=5000,
            is_available=True
        )
        self.product_customization12 = ProductCustomization.objects.create(
            product=self.product5,
            customizable='medium_test',
            price=5000,
            is_available=True
        )
        self.product_customization13 = ProductCustomization.objects.create(
            product=self.product5,
            customizable='large_test',
            price=5000,
            is_available=True
        )
        self.product_customization14 = ProductCustomization.objects.create(
            product=self.product6,
            customizable='chocolate_test',
            price=5000,
            is_available=True
        )
        self.product_customization15 = ProductCustomization.objects.create(
            product=self.product6,
            customizable='chip_test',
            price=5000,
            is_available=True
        )
        self.product_customization16 = ProductCustomization.objects.create(
            product=self.product6,
            customizable='ginger_test',
            price=5000,
            is_available=True
        )

    def test_user_creation(self):
        """
            test user creation
        """

        # content
        content = {
            "email": "restapi_test@gmail.com",
            "first_name": "restapi_test",
            "last_name": "restapi_test",
            "date_of_birth": "1996-12-12",
            "password": "mmmm1374"
        }

        # response
        response = self.csrf_client.post(
            main_settings.BASE_URL + '/api/create_user/', content)

        # get created object
        user_object = MyUser.objects.filter(email="restapi_test@gmail.com").first()

        # check db (test db)
        self.assertTrue(user_object)

        # check response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MyUser.objects.count(), 2)

    def test_obtain_token_user(self):
        """
            test obtain token method
        """

        # content
        content = {
            "email": "mohammad.masoomy74_test@gmail.com",
            "password": "mmmm1374"
        }

        # response
        response = self.csrf_client.post(
            main_settings.BASE_URL + '/api/obtain_token_user/', content
        )

        # check response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        """
            test user update
        """

        # generate token
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        auth = 'JWT {0}'.format(token)

        # response
        response = self.csrf_client.get(
            main_settings.BASE_URL + '/api/update_user/',
            HTTP_AUTHORIZATION=auth, format='json')

        # check response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        """
            test category
        """

        # generate token
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        auth = 'JWT {0}'.format(token)

        # content
        content = {
            'name': 'royal'
        }

        # response
        response = self.csrf_client.post(
            main_settings.BASE_URL + '/api/create_category/', content,
            HTTP_AUTHORIZATION=auth, format='json')

        # check response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 2)

    def test_create_product(self):
        """
            test product
        """

        # generate token
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        auth = 'JWT {0}'.format(token)

        # content
        content = \
            [
                {
                    "name": "Latte",
                    "category": "royal_test"
                },
                {
                    "name": "Cappuccino",
                    "category": "royal_test"
                },
                {
                    "name": "Espresso",
                    "category": "royal_test"
                },
                {
                    "name": "Tea",
                    "category": "royal_test"
                },
                {
                    "name": "Hot chocolate",
                    "category": "royal_test"
                },
                {
                    "name": "Cookie",
                    "category": "royal_test"
                }
            ]

        # response
        response = self.csrf_client.post(
            main_settings.BASE_URL + '/api/create_product/', content,
            HTTP_AUTHORIZATION=auth, format='json')

        # check response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 12)

    def test_create_product_customization(self):
        """
            test product customization
        """

        # generate token
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        auth = 'JWT {0}'.format(token)

        # content
        content = \
            [
                {
                    "product": "Latte_test",
                    "customizable": "skim",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Latte_test",
                    "customizable": "semi",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Latte_test",
                    "customizable": "whole",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Cappuccino_test",
                    "customizable": "small",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Cappuccino_test",
                    "customizable": "medium",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Cappuccino_test",
                    "customizable": "large",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Espresso_test",
                    "customizable": "single",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Espresso_test",
                    "customizable": "double",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Espresso_test",
                    "customizable": "triple",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Tea_test",
                    "customizable": "single",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Hot chocolate_test",
                    "customizable": "small",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Hot chocolate_test",
                    "customizable": "medium",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Hot chocolate_test",
                    "customizable": "large",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Cookie_test",
                    "customizable": "chocolate",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Cookie_test",
                    "customizable": "chip",
                    "price": 5000,
                    "is_available": True
                },
                {
                    "product": "Cookie_test",
                    "customizable": "ginger",
                    "price": 5000,
                    "is_available": True
                }
            ]
        # response
        response = self.csrf_client.post(
            main_settings.BASE_URL + '/api/create_product_customization/', content,
            HTTP_AUTHORIZATION=auth, format='json')

        # check response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductCustomization.objects.count(), 32)

    def test_create_order_checklist(self):
        """
            test order and checklist order
            test checkout billing information
        """

        # generate token
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        auth = 'JWT {0}'.format(token)

        # content
        content = {
            "order_number": 1,
            "consume_location": 0,
            "status": 0,
            "content":
                [
                    {
                        "product_customization": 20,
                        "number": 1
                    },
                    {
                        "product_customization": 23,
                        "number": 2
                    }
                ]
        }

        # response
        response = self.csrf_client.post(
            main_settings.BASE_URL + '/api/create_order_checklist/', content,
            HTTP_AUTHORIZATION=auth, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

        # test checkout bill
        response = self.csrf_client.get(
            main_settings.BASE_URL + '/api/view_orders/',
            HTTP_AUTHORIZATION=auth, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
