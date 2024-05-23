from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectListCreateView, UserProjectsView, ProjectDetailView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:id>/', ClientDetailView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
    path('user/projects/', UserProjectsView.as_view(), name='user-projects'),
]
