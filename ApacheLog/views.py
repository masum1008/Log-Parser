from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import xlwt
from apache_logs.models import ApacheLog
from sites.models import Site


def home(request):
    return render(request, 'index.html', {})


def report(request):
    code_list = ['--all--', '100', '101', '102', '200', '201', '202', '203', '204', '205', '206', '207', '208', '226',
                 '300', '301', '302', '303', '304', '305', '306', '307', '308', '400', '401', '402', '403',
                 '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416',
                 '417', '418', '421', '422', '423', '424', '426', '428', '429', '431', '451', '500', '501',
                 '502', '503', '504', '505', '506', '507', '508', '510', '511'
                 ]

    log_list = []#ApacheLog.objects.order_by('-id')
    sites = Site.objects.all()
    site = request.GET.get('site','')
    ip = request.GET.get('ip','')
    method = request.GET.get('method','')
    code = request.GET.get('code','')
    flag = False
    # all parameters are not mandatory..site, from_date, to_date ei 3 ta..mark them at required in html
    if site == '' and method == '' and code == '' and ip=='':
        paginator = Paginator(ApacheLog.objects.order_by('-id'), 15)  # Show 20 logs per page
        page = request.GET.get('page',1)
        log_list = paginator.page(page)
    else:
        if code != '--all--':
            log_list = ApacheLog.objects.filter(Q(site_id=site) &
                                                Q(request_method__istartswith=method) &
                                                Q(status__istartswith=code)
                                               )
        elif method != 'all':
            log_list = ApacheLog.objects.filter(Q(site_id=site) &
                                                Q(request_method__istartswith=method) &
                                                Q(status__istartswith=code)
                                               )
        else:
            log_list = ApacheLog.objects.filter(Q(site_id=site) &
                                                Q(request_method__istartswith=method)
                                              )
        paginator = Paginator(log_list, 15)  # Show 20 logs per page
        page = request.GET.get('page',1)
        log_list = paginator.page(page)
    #import pdb;pdb.set_trace()
    # try:
    #     log_list = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     log_list = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     log_list = paginator.page(paginator.num_pages)
    context = {
        "title": "Report",
        "logs": log_list,
        "site_list": sites,
        "site_id": int(site or 0),
        "code_list": code_list
    }
    return render(request, 'report.html', context)


def export_xls(request, log_list, flag):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="apache_log_parser_report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('ApacheLog')
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Receive Time', 'Method', 'Response', 'Time', 'URL']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    font_style.font.wrap = 1
    font_style.font.height = 240
    font_style.font._weight = 240

    if flag:
        rows = log_list.all().values_list('time_received_tz', 'request_method', 'status', 'time_us',
                                          'request_url_path')
    else:
        rows = ApacheLog.all().values_list('time_received_tz', 'request_method', 'status', 'time_us',
                                           'request_url_path')

    # import pdb; pdb.set_trace()
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    ws.col(0).width = 7000
    ws.col(4).width = 15000

    wb.save(response)
    return response
