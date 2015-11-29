from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db import connection, transaction, IntegrityError
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.conf import settings as django_settings
from django.template import RequestContext
from datetime import datetime, timedelta

import json

from users.models import UserProfile, UserBankApplicationStatus, UserBank

# Create your views here.
def signup(request):
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    name = request.POST.get('name', '')
    user_type = request.POST.get('user_type', 'applicant')
    resp = {}
    resp['email'] = email
    resp['name'] = name
    resp['user_type'] = user_type

    try:
        try:
            profile = UserProfile.objects.select_related('user').get(email = email)
            user = profile.user
        except UserProfile.DoesNotExist:
            new_user = True
            user = User(username=email)
            if not password:
                user.set_unusable_password()
            else:
                user.set_password(password)
            profile = UserProfile(user_type = user_type,email=email)
            if name:
                profile.name = name
            print 'p??'
            user.email = email
            profile.email = user.email
            user.last_login=datetime.now()
            try:
                user.save()
            except IntegrityError:  #concurrency issues
                print 'conc'
                user = User.objects.get(username=email)
            profile.user = user
            profile.save()
        resp['status'] = 'success'
        user = authenticate(username=email, password=password)
        auth_login(request, user)
    except Exception, e:
        print e
        resp['status'] = 'failed'
        return HttpResponse(json.dumps(resp), content_type="application/json")
    return HttpResponseRedirect('%s%s' % (django_settings.DOMAIN, '/home/'))

@csrf_exempt
def login_user(request):
    error = ''
    email = ''
    password = ''

    print 'amol'
    if request.user.is_authenticated():
        print 'r1'
        return HttpResponseRedirect('%s%s' % (django_settings.DOMAIN, '/home/'))

    print 'amol'
    is_ajax = request.is_ajax()
    if request.method == 'POST':
        print 'amol', request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not password:
            error = 'Please enter password'
            if is_ajax:
                resp = {}
                resp['status'] = 'failed'
                resp['status_code'] = 400
                resp['message'] = error
                resp['error'] = error
                print 'r2'
                return HttpResponse(json.dumps(resp), content_type='application/json')
        if not email:
            error = 'Please enter email'
            if is_ajax:
                resp = {}
                resp['status'] = 'failed'
                resp['status_code'] = 400
                resp['message'] = error
                resp['error'] = error
                print 'r2'
                return HttpResponse(json.dumps(resp), content_type='application/json')
        print 'amol', error
        if not error:
            print 'no error'
            user = authenticate(username=email, password=password)
            if not user:
                error = 'Invalid email and password'
                print 'not user', error
                if is_ajax:
                    resp = {}
                    resp['status'] = 'failed'
                    resp['status_code'] = 400
                    resp['message'] = error
                    resp['error'] = error
                    print 'r3'
                    return HttpResponse(json.dumps(resp), content_type='application/json')
            else:
                try:
                    #auth users without profiles
                    print '>>>', user
                    profile = UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    error = 'Invalid email and password'
                    if is_ajax:
                        resp = {}
                        resp['status'] = 'failed'
                        resp['status_code'] = 400
                        resp['message'] = error
                        resp['error'] = error
                else:
                    ref = request.GET.get('ref', '') #None type cannot be concatenated with the string
                    auth_login(request, user)

                    next_page = '/home/'
                    print 'r4'

                    return HttpResponseRedirect(next_page)
    else:
        print 'dont come'
        raise Http404

def home(request):
    user = request.user
    print user
    profile = UserProfile.objects.get(user=user)

    if profile.user_type == 'approver':
        return approver_home(request)
    resp = {}
    resp['profile'] = profile
    return render_to_response('userarea.html',
        resp,
        context_instance = RequestContext(request))

def approver_home(request):
    user = request.user
    print user
    profile = UserProfile.objects.get(user=user)

    user_bank = UserBank.objects.get(user_profile=profile)
    ifsc = user_bank.bank.ifsc
    print ifsc
    applications = UserBankApplicationStatus.objects.filter(ifsc=ifsc)
    resp = {}
    resp['profile'] = profile
    print '----applications----'
    print applications
    print '----applications----'
    resp['applications'] = applications
    apl_data = []
    for apl in applications:
        apl_data.append({
            'name': apl.user_profile.name,
            'date': apl.applied_on,
            'status': apl.status,
            'user_id': apl.user_profile.id
        })
    print 'data'
    resp['apl_data'] = apl_data
    print resp
    return render_to_response('bankarea.html',
        resp,
        context_instance = RequestContext(request))

def profile(request):
    user = request.user
    print user
    profile = UserProfile.objects.get(user=user)

    resp = {}
    resp['profile'] = profile
    return render_to_response('profile.html',
        resp,
        context_instance = RequestContext(request))

def signout(request):
    if request.user.is_authenticated():
        print 'user logged out'
        auth_logout(request)
    print 'response redirection now'
    return HttpResponseRedirect('/')

@csrf_exempt
def update_kyc_details(request):
    name = request.POST.get('name')
    phone = request.POST.get('mob')
    uid = request.POST.get('aadhaar')
    pan_card = request.POST.get('pan')
    gender = request.POST.get('gender')
    dob = request.POST.get('date')
    permanent = request.POST.get('permanent')
    user = request.user
    profile = UserProfile.objects.get(user=user)
    dob = datetime.strptime(dob, '%d/%m/%y')
    photo = request.FILES['photo']

    print 'will update now'
    profile.name = name
    profile.phone = phone
    profile.uid = uid
    profile.pan_card = pan_card
    profile.gender = gender
    profile.dob = dob
    profile.permanent = permanent
    profile.photo = photo
    profile.save()
    resp = {}
    resp['profile'] = profile
    next_page = '/profile'
    print 'r4'

    return HttpResponseRedirect(next_page)
    return render_to_response('userarea.html',
        resp,
        context_instance = RequestContext(request))

@csrf_exempt
def apply_for_wallet(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    ifsc = request.POST.get('ifsc')
    print request.POST
    print request.GET

    print ifsc
    resp = {}
    try:
        apply_bank = UserBankApplicationStatus.objects.create(user_profile=profile, ifsc=ifsc)
        apply_bank.applied_on = datetime.now()
        apply_bank.save()
        resp['status'] = 'success'
    except IntegrityError, e:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type='application/json')
