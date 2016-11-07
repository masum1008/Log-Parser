from django.shortcuts import render
from sites.models import Site
from .models import Site

# Create your views here.

def index(request):
        return render(request,'index.html', {})


def sitelist(request):
       # engine = create_engine('mysql://root:''@127.0.0.1:3306/APACHELOGPARSER')
        #sess=engine.
        #conn = engine.connect()
        #a= conn.execute("SELECT * FROM APACHELOGPARSER.sites").fetchall()
        a= Site.select()
        print a.execute().fetchone()
        #engine = create_engine("mysql+pymysql://sylvain:passwd@localhost/db?host=localhost?port=3306")
        #sess = orm.scoped_session()
        return render(request, 'sitelist.html', {})

def addSite (request):
        return  render(request,'add_site.html', {})

def saveSite (request):
        name = request.POST.get('site_name')
        url = request.POST.get('site_url')
        site_obj = Site(name = name, url = url)
        site_obj.save()
        print "Saved Successfully"

        return  render(request,'index.html', {})