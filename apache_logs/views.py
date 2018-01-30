import json
from django.shortcuts import render
from table.views import FeedDataView

from .models import ApacheLog, LogTable
from sites.models import Site
from log_formats.models import LogFormats
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction,connection
import apache_log_parser


def create(request):
    siteObj = Site.objects.order_by("-id")
    siteList = list(siteObj)
    return render(request, 'upload_log.html', {'sites':siteList})


def parseLog(request):
    siteObj = Site.objects.order_by("-id")
    siteList = list(siteObj)
    logFormatId = int(request.POST.get('log_format_id'))
    site_id = int(request.POST.get('site_id'))
    log_formatObg = LogFormats.objects.filter(id=logFormatId)
    logFormat = str(log_formatObg[0].log_format)
    print logFormat
    print logFormatId
    # % h % l % u % t \"%r\" %>s %b
    # %h %A - - %t \"%r\" %>s %b \"%{User-Agent}i\"
    # print logFormat
    line_parser = apache_log_parser.make_parser(""+logFormat)

    fileitem=request.FILES.get('ufile')

    flag = True
    # Insert into table (r1,r2....rn) values (v1,v2,v3...vn),(v1,v2,v3...vn),(v1,v2,v3...vn)....
    strQuery = "INSERT INTO "+ str(ApacheLog._meta.db_table) +" (local_ip,request_url_path,time_received_tz," \
                                                              "time_received_tz_isoformat,status,response_bytes_clf,remote_host,time_us," \
                                                              "request_method,format_id,site_id) VALUES "
    for line in fileitem.file:
        if(flag == True):
            strQuery += ' ('
        else:
            strQuery += ', ('

        try:
            data=line_parser(line.strip())
            #pprint(data)
            #break
        except Exception, e:
            #return HttpResponse("Formet Doesnt Match ......!")
            return render(request, 'upload_log.html', {'msg': "Invalid file or Log formet!", 'site_id': site_id, 'sites': siteList})

        strQuery += '"'+str(data.get('local_ip'))+'","'+str(data.get('request_url_path'))+'","'+ str(data.get('time_received_datetimeobj')) + '","' + str(data.get('time_received'))[1:-1].replace(':',' ',1).replace('/','-')+'","'
        strQuery +=  str(data.get('status')) + '","' + str(data.get('response_bytes_clf')) + '","' + str(data.get('remote_host')) + '","'
        strQuery +=  str(data.get('time_us'))+'","'+ str(data.get('request_method'))+'",'+ str(log_formatObg[0].id) +','+ str(site_id) +')'
        # if(flag == True):
        #     print  strQuery
        flag = False

        # orm query
        #     db = ApacheLog(
        #         status=data.get('status'),request_first_line=data.get('request_first_line'),
        #         response_bytes_clf=data.get('response_bytes_clf'),remote_host=data.get('remote_host'),
        #         request_http_ver=data.get('request_http_ver'),request_url_port=data.get('request_url_port'),
        #         remote_logname=data.get('remote_logname'),request_method=data.get('request_method')
        #     )
        #     db.save()

    cursor = connection.cursor()
    #import pdb;pdb.set_trace()
    try:
		cursor.execute(strQuery)
		
        
    except Exception, e:
        return render(request, 'upload_log.html', {'msg': e[1],'site_id':site_id,'sites':siteList})
    return HttpResponseRedirect('/log/loglist')

def log_list(request):
    last_obj = ApacheLog.objects.order_by('-id').first()
    if(not last_obj):
        return render(request,'log_list.html',{})
    last_id = last_obj.format_id

    # print last_site_id[0].site_id
    logs = list(ApacheLog.objects.filter(format_id=last_id).order_by('id')[:30])
    #site_id=logs[0]
    #print logs
    # pagination
    paginator = Paginator(ApacheLog.objects.filter(format_id=last_id), 20) # Show 30 logs per page
    page = request.GET.get('page')
    try:
        logs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        logs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        logs = paginator.page(paginator.num_pages)
    site_name = Site.objects.filter(id=logs[0].site_id)[0].site_name
    return render(request, 'log_list.html', {'logs':logs,'siteName':site_name})

def log_list(request):
    table = LogTable()
    return render(request, "log_list.html", {'logs': table})

def loadLogFormat(request):
    site_id = request.GET.get('site_id')
    logList = LogFormats.objects.filter(site_id=site_id)
    return HttpResponse(json.dumps(list (logList.values())), content_type="application/json")

