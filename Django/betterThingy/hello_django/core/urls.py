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
  path('solvetime', views.SolveTime.as_view(), name='solvetime'),
  path('todo', views.Todo.as_view(), name='todo'),
  path('taskConfirmDelete/<int:id_from_url>', views.TodoDelete.as_view(), name='todoDelete'),
  
  path('econProject/home', views.EconIndex.as_view(), name='econProject/index.html'),
  path('econProject/background', views.EconBginfo.as_view(), name='econProject/bginfo.html'),
  path('econProject/map', views.EconMap.as_view(), name='econProject/map.html'),
  path('econProject/economy', views.EconEcon.as_view(), name='econProject/econ.html'),
]
