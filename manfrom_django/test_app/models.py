from django.db import models


# Create your models here.
class Worker(models.Model):
    customers_id = models.IntegerField()
    customers_cid = models.CharField(max_length=20)
    customers_vat_id = models.CharField(max_length=20)
    customers_vat_status = models.BooleanField()
    customers_warning = models.CharField(max_length=20)
    customers_status = models.IntegerField()
    customers_gender = models.CharField(max_length=20)
    customers_firstname = models.CharField(max_length=20)
    customers_secondname = models.CharField(max_length=20)
    customers_lastname = models.CharField(max_length=20)
    customers_dob = models.DateTimeField()
    customers_email_address = models.EmailField()
    customers_default_address_id = models.IntegerField()
    customers_telephone = models.CharField(max_length=20)
    customers_fax = models.CharField(max_length=20)
    customers_password = models.CharField(max_length=20)
    customers_newsletter = models.BooleanField()
    customers_newsletter_mode = models.IntegerField()
    member_flag = models.IntegerField()
    delete_user = models.BooleanField()
    account_type = models.IntegerField()
    password_request_key = models.CharField(max_length=20)
    payment_unallowed = models.BooleanField()
    shipping_unallowed = models.BooleanField()
    refferers_id = models.IntegerField()
    customers_date_added = models.DateTimeField()
    customers_last_modified = models.DateTimeField()
    orig_reference = models.URLField()
    login_reference = models.URLField()
    login_tries = models.IntegerField()
    login_time = models.DateTimeField()
    customers_username = models.CharField(max_length=20)
    customers_fid = models.IntegerField()
    customers_sid = models.IntegerField()
    customers_personal_discount = models.FloatField()

    def __str__(self):
        return f'{self.customers_id}-{self.customers_lastname}-{self.customers_firstname}'
