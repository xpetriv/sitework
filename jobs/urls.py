from django.urls import path
from . import views
urlpatterns = [
    path('', views.jobs_home, name='jobs_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.JobsDetailView.as_view(), name='jobsdetail'),
    path('<int:pk>/update', views.JobsUpdateView.as_view(), name='jobsupdate'),
    path('<int:pk>/delete', views.JobsDeleteView.as_view(), name='jobsdelete')
]