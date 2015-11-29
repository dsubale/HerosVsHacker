from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wajood.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'www.views.home'),
    url(r'^users/signup/$', 'users.views.signup'),
    url(r'^users/signout/$', 'users.views.signout'),
    url(r'^users/update-kyc-details/$', 'users.views.update_kyc_details'),
    url(r'^login/$', 'users.views.login_user'),
    url(r'^home/$', 'users.views.home'),
    url(r'^profile/$', 'users.views.profile'),
    url(r'^users/apply-for-wallet/$', 'users.views.apply_for_wallet'),
    
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
