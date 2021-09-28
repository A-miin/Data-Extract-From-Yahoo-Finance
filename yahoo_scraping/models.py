from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Company(models.Model):
    date = models.DateField(_('Date'))
    open = models.FloatField(_('Open'))
    high = models.FloatField(_('High'))
    low = models.FloatField(_('Low'))
    close = models.FloatField(_('Close*'))
    adj_close = models.FloatField(_('Adj Close**'))
    volume = models.PositiveIntegerField(_('Volume'))

    def __str__(self):
        return f'{self.date.year}/{self.date.month}/{self.date.day}'

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')