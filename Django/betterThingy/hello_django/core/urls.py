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
  path('todo', views.TodoIndex.as_view(), name='todo'),
  
  path('econProject/home', views.EconIndex.as_view(), name='econProject/index.html'),
  path('econProject/map', views.EconMap.as_view(), name='econProject/map.html'),
  path('econProject/imports', views.EconImports.as_view(), name='econProject/impexp.html'),
  path('econProject/economy', views.EconEcon.as_view(), name='econProject/econ.html'),

  path('enemies', views.EnemyIndex.as_view(), name='enemy_index'),
  path('enemies/create', views.EnemyAdd.as_view(), name='enemy_add'),
  path('enemies/edit/<int:pk>', views.EnemyRename.as_view(), name='enemy_update'),
  path('enemies/delete/<int:pk>', views.EnemyDelete.as_view(), name='enemy_delete'),
]
