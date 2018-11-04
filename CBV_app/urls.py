from django.urls import path
from CBV_app import views

app_name = 'CBV_app'

urlpatterns = [
    path('CBV_app',views.SchoolListView.as_view(),name = 'list')
]