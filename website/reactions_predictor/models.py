from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_name(self):
        return self.first_name + " " + self.last_name


class Page(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, null=True)

    def __str__(self):
        return self.name


class UserPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_name() + " | " + self.page.name


class Post(models.Model):
    text = models.CharField(max_length=2000)
    page_name = models.CharField(max_length=100)

    def __str__(self):
        return self.text[:50]
