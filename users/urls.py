from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    # path('customers/', views.CustomerList.as_view()),
    # path('customers/<int:pk>/', views.CustomerDetail.as_view()),
    # path('suppliers/', views.SupplierList.as_view()),

    # path('payments/', views.PaymentsReceivedList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
