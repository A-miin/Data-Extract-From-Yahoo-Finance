from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Data(models.Model):
    company = models.CharField(
        _("Name"),
        max_length=64,
        null=True,
        blank=True
    )
    date = models.DateField(_('Date'))
    open = models.FloatField(_('Open'))
    high = models.FloatField(_('High'))
    low = models.FloatField(_('Low'))
    close = models.FloatField(_('Close*'))
    adj_close = models.FloatField(_('Adj Close**'))
    volume = models.PositiveIntegerField(_('Volume'))

    def __str__(self):
        return f'{self.id}. {self.company}'

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')