from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django import http
from django.utils import simplejson
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse
from django.contrib import messages


from base.models import Configuration
from base.forms import CompanyForm, CompanyLogoForm

@login_required
def edit(request, slug):
    school = get_object_or_404(Configuration, slug=slug)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, _('School updated!'))
            return http.HttpResponseRedirect(
                reverse('schools_edit', kwargs=dict(slug=school.id)))
    else:
        form = CompanyForm(instance=school)

    return render_to_response('schools/school_edit_summary.html', {
        'form': form,
        'school': school,
        'summary_tab': True,
    }, context_instance=RequestContext(request))


@login_required
@require_http_methods(['POST'])
def edit_logo_async(request, slug):
    school = get_object_or_404(Configuration, slug=slug)
    form = CompanyLogoForm(request.POST, request.FILES,
                                          instance=school)
    if form.is_valid():
        instance = form.save()
        return http.HttpResponse(simplejson.dumps({
            'filename': instance.logo.name,
        }))
    return http.HttpResponse(simplejson.dumps({
        'error': 'There was an error uploading your image.',
    }))


@login_required
def edit_logo(request, slug):
    school = get_object_or_404(Configuration, slug=slug)
    if request.method == 'POST':
        form = CompanyLogoForm(request.POST, request.FILES,
                                              instance=school)
        if form.is_valid():
            messages.success(request, _('Image updated'))
            form.save()
            return http.HttpResponseRedirect(reverse('school_edit_logo',
                kwargs={'slug': school.slug}))
        else:
            messages.error(request,
                           _('There was an error uploading your image'))
    else:
        form = CompanyLogoForm(instance=school)
    return render_to_response('schools/school_edit_logo.html', {
        'school': school,
        'form': form,
        'logo_tab': True,
    }, context_instance=RequestContext(request))
