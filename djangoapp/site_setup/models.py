from django.db import models

# Create your models here.

class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'
    
    title = models.CharField(max_length=65)
    descritpiton = models.CharField(max_length=255)
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu Link"
        verbose_name_plural = "Menu Links"
    
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    site_setup = models.ForeignKey(
        SiteSetup,
        on_delete=models.CASCADE,
        null= True,
        blank= True,
        default = None
        )

    def __str__(self):
        return self.text