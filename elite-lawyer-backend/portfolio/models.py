from django.db import models

# Create your models here.
from django.db import models


class PracticeArea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Practice Area"
        verbose_name_plural = "Practice Areas"
        ordering = ['id']

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()

    class Meta:
        verbose_name = "Selected Experience"
        verbose_name_plural = "Selected Experience"
        ordering = ['id']

    def __str__(self):
        return self.title


class Credential(models.Model):
    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.title


class Philosophy(models.Model):
    body = models.TextField()

    def __str__(self):
        return "Legal Philosophy"
