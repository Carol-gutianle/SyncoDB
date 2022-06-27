"""matlabweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.conf.global_settings import MEDIA_ROOT
from django.urls import path, re_path, include
from django.views.static import serve
from . import views
from pathlib import Path
import os
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
urlpatterns = {
    path('admin/', admin.site.urls),
    path('api/return_datas/', views.show_datas),
    path('api/cdata_post/', views.cdata_post),
    path('api/get_datas/', views.return_datas),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # url(r'^webtest/', views.PythonWebDemo.webtest),#添加api路由
    # path(r'',TemplateView.as_view(template_name="index.html"))
}

# #设置静态文件路径
# urlpatterns += staticfiles_urlpatterns()

