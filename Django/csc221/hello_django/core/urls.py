from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
        path('', TemplateView.as_view(template_name='core/index.html')),
        path('icecream/<str:flavor>', TemplateView.as_view(template_name='core/icecream.html')),
        path('count', views.page_count, name='count'),
        path('bmi', views.Bmi.as_view(), name='count'),
        path('bread', views.Bread.as_view(), name='bread'),
]
