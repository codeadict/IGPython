from django import template
from django.contrib.admin.templatetags.admin_static import static
from django.utils.html import format_html
from django.forms import BaseForm, ModelForm

register = template.Library()


@register.filter(name='boolean_icon')
def boolean_icon(field_val):
    icon_url = static('admin/img/icon-%s.gif' %
                      {True: 'yes', False: 'no', None: 'unknown'}[field_val])
    return format_html('<img src="{0}" alt="{1}" title="{1}" />', icon_url, field_val)


@register.inclusion_tag('includes/form.html', takes_context=True)
def render_form(context, form_obj):
    if not isinstance(form_obj, ModelForm):
        raise TypeError("Error including form, it's not a form, it's a %s" % type(form_obj))
    context.update({'form': form_obj})
    return context

@register.tag
def annotate_form_field(parser, token):
    """
    Set an attribute on a form field with the widget type

    This means templates can use the widget type to render things differently
    if they want to.  Django doesn't make this available by default.
    """
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError(
            "annotate_form_field tag requires a form field to be passed")
    return FormFieldNode(args[1])


class FormFieldNode(template.Node):
    def __init__(self, field_str):
        self.field = template.Variable(field_str)

    def render(self, context):
        field = self.field.resolve(context)
        field.widget_type = field.field.widget.__class__.__name__
        return ''