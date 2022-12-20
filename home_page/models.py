from django.db import models


class Menu(models.Model):
    MENU = (
        ("First courses", "First courses"),
        ("Second courses", "Second courses"),
        ("Desserts", "Desserts"),
        ("Wine Map", "Wine Map"),
        ("Drinks", "Drinks"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    menu = models.CharField(choices=MENU, max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to="")

    def __str__(self):
        return self.title


class Contact(models.Model):
    instagram = models.CharField(max_length=50, null=True)
    whatsApp = models.CharField(max_length=40, null=True)
    telegram = models.TextField(null=True)
    phone_number = models.CharField(max_length=40, null=True)
    address = models.TextField(null=True)
    address_map = models.ImageField(upload_to="", null=True)

    def __str__(self):
        return self.address


class Chef(models.Model):
    image = models.ImageField(upload_to="")
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=40, null=True)
    date = models.DateField()
    guests = models.IntegerField()
    BRANCHES = (
        ("Asanbai", "Asanbai"),
        ("Golden Stork", "Golden Stork"),
        ("Toktogula", "Toktogula"),
        ("Shopokova", "Shopokova"),
    )
    branch = models.CharField(choices=BRANCHES, max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    description = models.TextField()
    name = models.TextField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#  author = models.ForeignKey(User,on_delete=models.CASCADE)


class Branch(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="")
    description = models.TextField()

    def __str__(self):
        return self.name
