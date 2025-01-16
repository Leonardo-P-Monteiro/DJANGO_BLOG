import string
from random import SystemRandom
from django.utils.text import slugify

def random_latters(k=5):
    return ''.join(SystemRandom().choices(string.ascii_lowercase + 
            string.digits, k=k))

def slugify_new(text, k=5):

    return slugify(text) + '-' + random_latters(k=k)


it = 'LP'

if __name__ == '__main__':
    print(slugify_new('testando o meu slug'))