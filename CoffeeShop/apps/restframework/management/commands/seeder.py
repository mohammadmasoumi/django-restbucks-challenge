from django.core.management.base import BaseCommand
from ...models import Product, Category, ProductCustomization, MyUser
import logging


class Command(BaseCommand):
    help = 'database seeder '

    def handle(self, *args, **options):
        """
            get competitions from football api
        """
        # create superuser
        try:
            MyUser.objects.create_superuser(
                email='mohammad.masoomy74@gmail.com',
                first_name='mohammad',
                last_name='masoumi',
                date_of_birth='1996-12-16',
                password='mmmm1374'
            )

            logging.info('*** super user created ***')
        except:
            logging.info('*** super user creation failed ***')

        # create user
        email = 'mohammad.masoomy74_test@gmail.com'
        first_name = 'mohammad_test'
        last_name = 'masoumi_test'
        date_of_birth = '1996-12-12'
        password = 'mmmm1374'

        user = MyUser.objects.filter(email=email)

        if not user:
            user = MyUser.objects.create_user(email=email, date_of_birth=date_of_birth,
                                              first_name=first_name, last_name=last_name,
                                              password=password)
            logging.info('*** user created ***')
        # create category
        category, created = Category.objects.get_or_create(
            name='royal'
        )
        if created:
            logging.info('*** category created ***')
        # create product

        product_obj = Product.objects.filter(name='Latte').first()
        if not product_obj:
            product_list = [
                'Latte',
                'Cappuccino',
                'Espresso',
                'Tea',
                'Hot chocolate',
                'Cookie'
            ]
            product_object_list = []
            for product in product_list:
                product_object_list.append(Product(name=product, category=category))

            Product.objects.bulk_create(product_object_list)
            logging.info('*** products created ***')
        # creating product customization

        for product in Product.objects.all():
            if product.name == 'Latte':
                product_customization1, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='skim',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization2, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='semi',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization3, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='whole',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
            elif product.name == 'Cappuccino':
                product_customization4, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='small',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization5, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='medium',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization6, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='large',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
            elif product.name == 'Espresso':
                product_customization7, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='single',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization8, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='double',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization9, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='triple',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
            elif product.name == 'Tea':
                product_customization10, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='single',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
            elif product.name == 'Hot chocolate':
                product_customization11, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='small',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization12, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='medium',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization13, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='large',
                    price=5000,
                    is_available=True
                )
            else:
                product_customization14, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='chocolate',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization15, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='chip',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
                product_customization16, created = ProductCustomization.objects.get_or_create(
                    product=product,
                    customizable='ginger',
                    price=5000,
                    is_available=True
                )
                if created:
                    logging.info('*** product_customization created ***')
