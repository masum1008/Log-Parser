from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Site
from .forms import SiteForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    return render(request, 'site_add_edit.html', context)


def site_list_page(request):
    site_list = Site.objects.order_by("-id")[:20]
    site_list_all = Site.objects.order_by("-id")
    site_name = request.GET.get('site_name')
    if site_name:
        if(site_name == 'ALL'):
            site_list = Site.objects.order_by('-id')
        else:
            site_list = Site.objects.filter(site_name=site_name)

    # pagination
    paginator = Paginator(site_list, 20) # Show 20 logs per page
    page = request.GET.get('page')
    try:
        site_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        site_list = paginator.page(1)
    except EmptyPage:
        site_list = paginator.page(paginator.num_pages)
    return render(request, 'site_list.html', {'siteList':site_list,'site_list':site_list_all,'siteName':site_name})

def site_edit_page(request, id=None):
    detail = get_object_or_404(Site, id=id)
    form = SiteForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/sites/list/")
    context = {
        "form": form,
        "title": "Edit Site Info",
    }
    return render(request, 'site_add_edit.html', context)


def site_delete_page(request, id=None):
    detail = get_object_or_404(Site, id=id)
    detail.delete()
    return HttpResponseRedirect("/sites/list/")
