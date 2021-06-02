from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def static_cdn(url):
    if settings.CDN_ENABLED:
        url = settings.STATIC_URL.replace(settings.AWS_S3_CUSTOM_DOMAIN, settings.AWS_S3_CDN_DOMAIN).replace('/static/', '/')
        return url
    else:
        return settings.STATIC_URL