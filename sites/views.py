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
        "title": "Add Log Format",
    }
    return render(request, 'log_format_add.html', context)


def site_list_page(request):
    log_list = Site.objects.order_by("-id")
    lglst = list(log_list)
    for log in lglst:
        log.serial = lglst.index(log)+1
    context = {
        "log_list": log_list,
        "count": 1,
        "title": "List of site",
    }
    return render(request, 'log_format_list.html', context)


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
    return render(request, 'log_format_add.html', context)


def site_delete_page(request, id=None):
    detail = get_object_or_404(Site, id=id)
    detail.delete()
    return HttpResponseRedirect("/sites/list/")
