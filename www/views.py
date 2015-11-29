from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

import json
import logging

from django_user_agents.utils import get_user_agent

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponsePermanentRedirect
from django.conf import settings
from django.db import transaction, IntegrityError
from django.db.models import F
from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    print 'hello'
    return render_to_response('login.html', {}, context_instance=RequestContext(request))
