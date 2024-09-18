from social.models import Link


def get_social_links(request):
    social_reds = Link.objects.all()
    links = {link.key: link.url for link in social_reds}
    
    return links
