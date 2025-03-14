from django.db import models
from utils.model_validators import validate_img
from utils.images import resize_image

# Create your models here.

class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'
    
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)
    favicon = models.ImageField(
    upload_to= 'assets/faicon/%Y/%m/',
    blank=True,
    default='',
    validators=[validate_img],
    )

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name) # Estamos pegando o nome (caminho do arquivo)
        # antres de salvar o novo arquivo que vai sobrescrever o arquivo que está no bd (se já
        # tiver sido salvo algo antes).

        # Estamos trazendo o método save original para dentro do nosso método
        # pois estamos sobrescrevendo-o.
        super().save(*args, **kwargs) # Aqui estamos salvado o que foi passado de informação nova
        # pelo forms desse nosso model.
        favicon_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name
        
        if favicon_changed:
            resize_image(self.favicon, 32)

    def __str__(self):
        return self.title


class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu Link"
        verbose_name_plural = "Menu Links"
    
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False) # Opens a new guide on the browser.
    site_setup = models.ForeignKey(
        SiteSetup,
        on_delete=models.CASCADE,
        null= True,
        blank= True,
        default = None
        )


    def __str__(self):
        return self.text