from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    warehouse = models.CharField(max_length=100, default='Unknown')  # Required field with default

    def __str__(self):
        return f"{self.name} (Warehouse: {self.warehouse})"

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)  # Optional field

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Client(User):
    PROVINCE_CHOICES = [
        ('AB', 'Alberta'),
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),
    ]
    company = models.CharField(max_length=50, null=True, blank=True)  # Made optional
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')  # Default set to Windsor
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    interested_in = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.username} ({self.company if self.company else 'No Company'})"

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        (0, 'Order Cancelled'),
        (1, 'Order Placed'),
        (2, 'Order Shipped'),
        (3, 'Order Delivered'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    num_units = models.PositiveIntegerField()
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=1)
    status_date = models.DateField(auto_now=True)

    def total_cost(self):
        return self.num_units * self.product.price

    def __str__(self):
        return f"Order {self.id} - {self.product.name} x{self.num_units} ({self.get_order_status_display()}) - Total: ${self.total_cost()}"
