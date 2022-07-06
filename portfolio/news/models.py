from django.db import models


# Create your models here.
class Group_of_news(models.Model):
    group = models.CharField(max_length=20)

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class News(models.Model):
    title = models.CharField(max_length=150)
    full_text = models.TextField()
    img = models.ImageField()
    author = models.CharField(max_length=50)  # may be auth and foreign key
    author_img = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group_of_news, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
