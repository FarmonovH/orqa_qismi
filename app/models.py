from django.db import models
from django.utils.html import format_html


# Create your models here.
class Social_links(models.Model):
    telegram = models.URLField(help_text="Telegram manzilingizni kiriting", verbose_name="telegram",
                               default="")
    instagram = models.URLField(help_text="instagram manzilingizni kiriting", verbose_name="instagram",
                                default="")
    github = models.URLField(help_text="github manzilingizni kiriting", verbose_name="GitHub",
                             default="")
    facebook = models.URLField(help_text="facebook manzilingizni kiriting", verbose_name="Facebook",
                               default="")
    youtube = models.URLField(help_text="youtebe manzilingizni kiriting", verbose_name="youtube",
                               default="")
    twitter = models.URLField(help_text="twitter manzilingizni kiriting", verbose_name="twitter",
                               default="")

    def __str__(self):
        return "ijtimoiy sahifa url manzillarini kiriting"
    class Meta:
        verbose_name = "Social link"
        verbose_name_plural = "Social links"

class Portfolio(models.Model):
    name = models.CharField(max_length=150, help_text="ismingizni kiriting", verbose_name="Ismingiz")
    image = models.ImageField(upload_to="profil_image", help_text="rasmingizni yuklang", verbose_name="Rasmingiz")
    age = models.IntegerField(help_text="yoshingizni kiriting", verbose_name="Age")
    techlonoligies = models.TextField(help_text="ishlatgan texnologiyalaringizni kiriting ", verbose_name="Technologies")
    jop = models.CharField(max_length=150, help_text="kasbingizni kiriting ", verbose_name="Jop")
    languages = models.CharField(max_length=150, default="Uzbek", help_text="yana boshqa tillarni bilsangiz kiriting",
                                 verbose_name="Language")
    qilingan_ish = models.FileField(upload_to="resumes", help_text="rezumengizni yuklang", verbose_name="Resumes")
    profession_years = models.IntegerField(default="1.5", help_text="tajribangizni kiriting", verbose_name="ish tajribasi")
    projects = models.IntegerField(help_text="qilgan ishlaringizni kiriting ", verbose_name="loyihalar")
    def __str__(self):
        return self.name
    # @property
    # def image_url(self):
    #     return format_html('<img src={} width="50" height="50" style="border-radius:10"'.format(self.image_url))


class Visitors(models.Model):
    count = models.IntegerField(default=1)


class Portfolio_project(models.Model):
    title = models.CharField(max_length=150, help_text="loyiha nomini kiriting", verbose_name="Title")
    loyiha_url = models.URLField(help_text="loyiha url kiriting ", verbose_name="URL")
    images = models.ImageField(upload_to="loyiha_images", help_text="loyiha rasmini yuklang", verbose_name="image")
    def __str__(self):
        return self.title

    # @property
    # def photo(self):
    #     return format_html('<img src={} width="50" height="50" style="border-radius:10"'.format(self.photo))


class Info(models.Model):
    email = models.EmailField(help_text="emailingizni kiriting", verbose_name="email")
    phone_number = models.CharField(max_length=150, help_text="telefon raqamingizni kiriting", verbose_name="phone number")
    location = models.CharField(max_length=150, help_text="joylashuvingizni kiriting", verbose_name="joylashuv")
    def __str__(self):
        return "INFO"

class Xabarlar(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

