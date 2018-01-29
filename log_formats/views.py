from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import LogFormats
from .forms import LogFormatForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sites.models import Site
# Create your views here.


def logformat_add_page(request):
    form = LogFormatForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/logformats/list/")
    context = {
        "form": form,
        "title": "Add Log Format",
    }
    return render(request, 'log_formats/log_format_add_edit.html', context)


def logformat_list_page(request):
    log_list = LogFormats.objects.order_by("-id")

    # for search
    query = request.GET.get('q')
    if query:
        log_list = log_list.filter(Q(site__site_name__istartswith=query))

    # pagination
    paginator = Paginator(log_list, 20) # Show 30 logs per page
    page = request.GET.get('page')
    try:
        log_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        log_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        log_list = paginator.page(paginator.num_pages)
    context = {
        "log_list": log_list,
        "title": "List of Logformat",
    }
    return render(request, 'log_formats/log_format_list.html', context)


def logformat_edit_page(request, id=None):
    detail = get_object_or_404(LogFormats, id=id)
    #import pdb;pdb.set_trace();

    form = LogFormatForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/logformats/list/")
    context = {
        "form": form,
        "title": "Edit Log Format",
    }
    return render(request, 'log_formats/log_format_add_edit.html', context)


def logformat_delete_page(request, id=None):
    detail = get_object_or_404(LogFormats, id=id)
    detail.delete()
    return HttpResponseRedirect("/logformats/list/")

def set_default_logformat(request, id=None):
    detail = get_object_or_404(LogFormats, id=id)
    site_id = detail.site_id

    LogFormats.objects.filter(site_id=site_id).update(is_default=False)

    LogFormats.objects.filter(id=detail.id).update(is_default=True)

    return HttpResponseRedirect("/logformats/list/")

