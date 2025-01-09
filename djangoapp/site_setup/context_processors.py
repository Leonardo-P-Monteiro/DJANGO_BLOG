from site_setup.models import SiteSetup

# It allow that we access this context data into all of templates on our 
# project. After of definition this function we have do include this file on the
# setting.py on constant TEMPLATES on context processors key.
def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': setup
    }
