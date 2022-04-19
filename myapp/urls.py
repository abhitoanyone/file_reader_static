from django.urls import path

from . import views


urlpatterns = [
    path("", views.csv_file_accept),
    # path("/table_view/", views.table_view)
]