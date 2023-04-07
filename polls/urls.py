from django.urls import path
from . import views

app_name = 'polls'

## func views
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<int:qu_id>/', views.detail, name='detail'),
#    path('<int:qu_id>/results/', views.results, name='results'),
#    path('<int:qu_id>/vote/', views.vote, name='vote')
#]

# class views
urlpatterns = [
#    path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:qu_id>/vote/', views.vote, name='vote')
]
