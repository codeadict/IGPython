from django import template
from django.utils.html import format_html

from base.models import Setting

register = template.Library()


@register.inclusion_tag('reports/header.html', takes_context=True)
def render_header(context):
    company_name = Setting.get_val('company_name')
    
    street1 = Setting.get_val('street1')
    street2 = Setting.get_val('street2')
    city = Setting.get_val('city')
    state = Setting.get_val('state')
    postcode = Setting.get_val('postcode')
    
    company_address = '%s %s, %s, %s %s' %(street1, street2, city, state, postcode)
    
    context.update({'company_name': company_name, 'company_address': company_address})
    return context