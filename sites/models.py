from __future__ import unicode_literals

from django.db import models
#from sqlalchemy import orm, Table, MetaData, Column, INTEGER
from sqlalchemy import *

db = create_engine('mysql://root:''@127.0.0.1:3306/APACHELOGPARSER')
metadata = MetaData(db)

Site = Table('sites', metadata,
              Column('id', Integer, primary_key=True,autoincrement=True),
              Column('client_ip', String(50)),
              Column('domain_name', String(100)),
              Column('url', String(500)),
              Column('filename', String(100)),
              Column('upload_time', TIMESTAMP),
              )

# site_table = Table('sites', MetaData(),
#                    Column('id', INTEGER,primary_key=True,autoincrement=True),
#                    #Column('name')
#                    )
# # Create your models here.
# class Site(models.Model):
#     pass
#
# site_mapper = orm.mapper(Site, site_table)
