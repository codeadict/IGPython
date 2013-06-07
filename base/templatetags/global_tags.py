from django import template
from django.contrib.admin.templatetags.admin_static import static
from django.utils.html import format_html

register = template.Library()


@register.filter(name='boolean_icon')
def boolean_icon(field_val):
    icon_url = static('admin/img/icon-%s.gif' %
                      {True: 'yes', False: 'no', None: 'unknown'}[field_val])
    return format_html('<img src="{0}" alt="{1}" title="{1}" />', icon_url, field_val)