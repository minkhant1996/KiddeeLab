from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('Location/', views.location_list, name='location_list'),
    # path('Course/', views.CourseListView.as_view(), name='course_list'),
    path('Course/', views.CourseListView, name='course_list'),
    path('Course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('Teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('About/', views.about, name='about'),
]

