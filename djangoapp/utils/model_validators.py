from django.core.exceptions import ValidationError



def validate_img(image):
# Aqui conseguimos acessar o atributo "name" da image por que o arquivo enviado
# para o Django é tratado como um File Object. Essa classe permite acessar alguns
# atributos de arquivos - não só arquivos de imagens, mas de qualquer arquivo.
    if not image.name.lower().endswith('.png'):
        raise ValidationError('The image needs to have .png format.')
