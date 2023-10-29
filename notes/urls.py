from django.urls import path
from notes.views import (
    CustomerCreate,
    CustomerDelete,
    CustomerDetail,
    CustomerList,
    CustomerUpdate,
)

urlpatterns = [
    # Customer Routes
    path("create/", CustomerCreate.as_view(), name="create-customer"),
    path("<int:pk>/", CustomerDetail.as_view(), name="get-customer"),
    path("", CustomerList.as_view()),
    path("update/<int:pk>/", CustomerUpdate.as_view(), name="update-customer"),
    path("delete/<int:pk>/", CustomerDelete.as_view(), name="remove-customer")
]
