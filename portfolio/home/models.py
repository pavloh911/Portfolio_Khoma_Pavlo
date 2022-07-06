from datetime import datetime

from django.db import models

status_choise = (
    ('new', 'new'),
    ('worked', 'worked')
)


# Create your models here.
class MessagesForUs(models.Model):
    user_name = models.CharField('name', max_length=20)
    user_email = models.CharField('email', max_length=50)
    user_message = models.TextField('message')
    data = models.DateTimeField('data', default=datetime.now())
    status = models.CharField(max_length=20, choices=status_choise, default='new')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
