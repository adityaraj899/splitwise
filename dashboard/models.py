from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Friend(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Friend, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Bill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=128)
    amount = models.IntegerField(default=0)
    paidby = models.ForeignKey(Friend, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
