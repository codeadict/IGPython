from django import template
from django.contrib.admin.templatetags.admin_static import static
from django.utils.html import format_html
from django.forms import BaseForm

register = template.Library()


@register.filter(name='boolean_icon')
def boolean_icon(field_val):
    icon_url = static('admin/img/icon-%s.gif' %
                      {True: 'yes', False: 'no', None: 'unknown'}[field_val])
    return format_html('<img src="{0}" alt="{1}" title="{1}" />', icon_url, field_val)


@register.inclusion_tag('includes/form.html', takes_context=True)
def render_form(context, form_obj):
    if not isinstance(form_obj, BaseForm):
        raise TypeError("Error including form, it's not a form, it's a %s" % type(form_obj))
    context.update({'form': form_obj})
    return context