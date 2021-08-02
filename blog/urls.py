from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('service', views.ServicePage, name='service'),
    path('service/<slug:slug>/', views.ServiceDetail, name='service_detail'),
    path('project', views.ProjectPage, name='project'),
    path('project/<slug:slug>/', views.ProjectDetail, name='project_detail'),
    path('contact', views.ContactPage, name='contact'),
]

urlpatterns += static(settings.FILE_URL,
                          document_root=settings.FILE_ROOT)