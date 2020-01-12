from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):

    class Gender(models.TextChoices):

        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'
        BLANK = '', ''

    class AccountType(models.TextChoices):

        INDIVIDUAL = 'Individual', 'Individual'
        PROPERTY_OWNER = 'Property Owner', 'Property Owner'
        ESTATE_AGENT = 'Estate Agent', 'Estate Agent'
        PROPERTY_DEVELOPER = 'Property Developer', 'Property Developer'

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        default=Gender.BLANK
    )
    account_type = models.CharField(
        max_length=50,
        choices=AccountType.choices,
        default=AccountType.INDIVIDUAL
    )
    date_of_birth = models.DateField("date of birth", blank=True, null=True)
    phone_number = PhoneNumberField(
        verbose_name="phone number",
        null=True, blank=True
    )
    following = models.ManyToManyField(
        "self", through='Peer',
        symmetrical=False,
        related_name='followers'
    )

    def get_absolute_url(self):
        return reverse("user_profile", args=[self.username])


class Peer(models.Model):

    user_from = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='rel_from_set',
        on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='rel_to_set',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    expires_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ('-created_at',)
        unique_together = (('user_from', 'user_to'),)

    def __str__(self):
        return '%(user_from)s ---->> %(user_to)s' % {'user_from': self.user_from, 'user_to': self.user_to}


class TransactionLog(models.Model):

    class TransactionStatus(models.TextChoices):

        TRANSACTION_REJECTED = 'Rejected', 'Rejected'
        TRANSACTION_PAID = 'Paid', 'Paid'
        TRANSACTION_IN_PROGRESS = 'In Progress', 'In Progress'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=TransactionStatus.choices,
        default=TransactionStatus.TRANSACTION_IN_PROGRESS
    )
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def update_status(self, new_status):

        self.status = new_status
        self.save()

    class Meta:
        verbose_name = "Transaction Log"
        verbose_name_plural = "Transaction Logs"

    def __str__(self):
        return '{} ---- {} ---- {}'.format(self.user, self.status, self.description)

    def get_absolute_url(self):
        return reverse("TransactionLog_detail", kwargs={"pk": self.pk})
