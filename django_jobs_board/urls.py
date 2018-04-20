"""
Definition of urls for to_do_app.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import todo.forms
import todo.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'todo/login.html',
            'authentication_form': todo.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('todo.urls'))
]
