from django.db import models
from django.contrib.auth.models import User

# def upload_to(self, y):
#     return 'userprofiles/%s/%s.%s' % (self.id, self.id, y.split('.')[-1])

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', unique=True, related_name='profile')
    uid = models.CharField(max_length=12, db_index=True, blank=True, null=True, default=None)
    pan_card = models.CharField(max_length=10, db_index=True, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, default=None)
    dob = models.DateTimeField(default=None, null=True)
    gender = models.CharField(max_length=15, default='male', choices=(
        ('male', 'Male'),
        ('female', 'Female'),
        ('transgender', 'Transgender'),))
    phone = models.CharField(max_length=10, db_index=True, null=True, default=None)
    email = models.EmailField(unique=True, db_index=True, default=None)
    user_type = models.CharField(max_length=10, default='applicant', choices=(
        ('applicant', 'Applicant'),
        ('approver', 'Approver'),))
    permanent = models.TextField(null=True, blank=True, default=None)
    photo = models.ImageField(upload_to='documents/%Y/%m/%d', null=True)

    def upload_to(self, y):
        return 'userprofiles/%s/%s.%s' % (self.id, self.id, y.split('.')[-1])

class UserProfileAddress(models.Model):
    user_profile = models.ForeignKey('UserProfile', related_name='address')
    address_type = models.CharField(max_length=10, default='permanent', choices=(
        ('local', 'Local'),
        ('permanent', 'Permanent'),))
    co_name = models.CharField(max_length=255, blank=True, null=True)
    house = models.TextField(null=True, blank=True, default=None)
    street_name = models.TextField(null=True, blank=True, default=None)
    landmark = models.TextField(null=True, blank=True, default=None)
    locality = models.TextField(null=True, blank=True, default=None)
    city = models.CharField(max_length=255, blank=True, null=True)
    sub_district_name = models.CharField(max_length=255, blank=True, null=True)
    district_name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    post_office_name = models.CharField(max_length=255, blank=True, null=True)
    local_language = models.CharField(max_length=255, blank=True, null=True)

class Bank(models.Model):
    ifsc = models.CharField(unique=True, db_index=True, max_length=11, blank=True, null=True)
    branch = models.CharField(db_index=True, max_length=255, blank=True, null=True)
    bank_name = models.CharField(db_index=True, max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('ifsc','branch','bank_name')

class UserBank(models.Model):
    user_profile = models.ForeignKey('UserProfile', related_name='banks')
    bank = models.ForeignKey('Bank', related_name='banks', default=None)

class UserBankApplicationStatus(models.Model):
    user_profile = models.ForeignKey('UserProfile', related_name='bankapplications')
    ifsc = models.CharField(db_index=True, max_length=11, blank=True, null=True)
    status = models.CharField(max_length=10, default='applied', choices=(
        ('applied', 'Applied'),
        ('rejected', 'Rejected'),
        ('approved', 'Approved'),))
    applied_on = models.DateTimeField(null=True, blank=True, auto_now=False, db_index=True)

    class Meta:
        unique_together = ('user_profile','ifsc')