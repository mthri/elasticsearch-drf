from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(verbose_name=_('آدرس ایمیل'), unique=True)


class Car(models.Model):
    class Meta:
        verbose_name = _('خودرو')
        verbose_name_plural = _('خودرو ها')


    name = models.CharField(verbose_name=_('نام'), max_length=50)
    num_cylinders = models.PositiveIntegerField(verbose_name=_('تعداد سیلندر'))
    num_seats = models.PositiveIntegerField(verbose_name=_('تعداد سرنشین'))
    color = models.CharField(verbose_name=_('رنگ'), max_length=20)
    engine_capacity = models.DecimalField(verbose_name=_('حجم سیلندر'), max_digits=5,
                                          decimal_places=2)
    owner = models.CharField(verbose_name=_('مالک خودرو'), max_length=50)
    create_at = models.DateTimeField(verbose_name=_('تاریخ ایجاد'), auto_now_add=True)


    def __str__(self):
        return self.name + ' ' + self.color