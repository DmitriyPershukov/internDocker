
# Create your models here.


from django.db import models
from django.utils.safestring import mark_safe

class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=200)
    icon =models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def icon_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.icon))

    icon_tag.short_description = 'Image'

class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    photo = models.CharField(max_length=200)
    def photo_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo))

    photo_tag.short_description = 'Image'

class Word(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    transcription = models.CharField(max_length=200)
    example = models.CharField(max_length=200)
    sound = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def pronunciation_tag(self):
        return mark_safe('<audio controls="controls"><source src="%s"/>Your browser does not support the audio element.</audio>' % (self.sound))

    pronunciation_tag.short_description = 'Pronunciation'