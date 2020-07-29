from django.urls import path

from .views import EmployeeCreate, EmployeeList

app_name = 'main'

urlpatterns = [
    path('', EmployeeCreate.as_view()),
    path('detail/', EmployeeList.as_view()),
]
