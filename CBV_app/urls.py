from django.urls import path
from CBV_app import views

app_name = 'CBV_app'

urlpatterns = [
    path('CBV_app',views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(), name='detail'),
    path('create/',views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(), name='delete'),
]