"""bestfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from best import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('application/',views.application),
    path('privacypolicy/',views.privacypolicy),
    path('terms/',views.terms),
    path('refund/',views.refund),
    path('six/', views.six),
    path('seven/',views.seven),
    url(r'^$', views.home, name='home'),
    path('eight/',views.eight),
    path('nine/',views.nine),
    path('ten/',views.ten),
    path('about/',views.about),
    path('update/', views.update),
    path('gallery/',views.gallery),
    path('brouchars/',views.brouchars),
    path('contact/',views.contact),
    path('student_login/',views.student_login),
    path('admin_login/',views.admin_login),
    path('pay/', views.payment),
    path('payment2/',views.payment2),
    path('bhimapp/',views.bhimapp)
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)