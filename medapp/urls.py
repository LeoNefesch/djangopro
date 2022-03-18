from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from medapp import views

urlpatterns = [
    path('patients/', views.PatientList.as_view()),
    path('patients/<int:pk>/', views.PatientDetail.as_view()),
    path('cases/', views.CaseList.as_view()),
    re_path('^cases/(?P<patient_id>.+)/$', views.CaseList.as_view()),
    path('cases/<int:pk>/', views.CaseDetail.as_view()),
    path('documents/', views.DocumentList.as_view()),
    path('documents/<int:pk>/', views.DocumentDetail.as_view()),
    path('bodies/', views.DocumentBodyList.as_view()),
    path('bodies/<int:pk>/', views.DocumentBodyDetail.as_view()),
    path('log/', views.RequestLogList.as_view()),
    path('log/<int:pk>/', views.RequestLogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
