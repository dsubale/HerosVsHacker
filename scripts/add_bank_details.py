import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'wajood.settings'

ROOT_FOLDER = os.path.realpath(os.path.dirname(__file__))
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('/')]

if ROOT_FOLDER not in sys.path:
    sys.path.insert(1, ROOT_FOLDER + '/')

from django.db import IntegrityError
from users.models import Bank

f = open('bank_ifsc.csv', 'r')
for line in f:
    try:
        ifsc,b_name, br_name = line.strip().split(',')

        print ifsc, b_name, br_name
        b = Bank(ifsc=ifsc,bank_name=b_name,branch=br_name)
        b.save()
    except Exception,e :
        print e
