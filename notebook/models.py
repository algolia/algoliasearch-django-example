from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=40)
    service = models.CharField(max_length=40)

    def __str__(self):
        return self.username + "@" + self.service


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    company = models.CharField(max_length=40)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=8)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    web = models.CharField(max_length=30)
    followers = models.IntegerField(default=0)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    accounts = models.ManyToManyField(Account)

    def __str__(self):
        return self.name

    def account_names(self):
        return [str(account) for account in self.accounts.all()]

    def account_ids(self):
        return [account.id for account in self.accounts.all()]
