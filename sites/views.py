from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Site
from .forms import SiteForm
# Create your views here.


def site_add_page(request):
    form = SiteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/sites/list/")
    context = {
        "form": form,
        "title": "Add Site Info",
    }
    return render(request, 'site_add.html', context)


def site_list_page(request):
    siteObj = Site.objects.order_by("-id")
    siteList = list(siteObj)
    return render(request, 'site_list.html', {'siteList':siteList})

def site_edit_page(request, id=None):
    detail = get_object_or_404(Site, id=id)
    form = SiteForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/sites/list/")
    context = {
        "form": form,
        "title": "Edit Log Format",
    }
    return render(request, 'site_add.html', context)


def site_delete_page(request, id=None):
    detail = get_object_or_404(Site, id=id)
    detail.delete()
    return HttpResponseRedirect("/sites/list/")
