# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the checkout process
    url(r'^$', views.checkout),
    url(r'^capture/$', views.capture),
]
