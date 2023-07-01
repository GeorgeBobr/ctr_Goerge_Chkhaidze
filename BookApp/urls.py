from django.urls import path
from .views import records_view, add_record, edit_record, delete_record

urlpatterns = [
    path('', records_view, name='records_view'),
    path('create/', add_record, name='create'),
    path('edit/<int:id>/', edit_record, name='edit'),
    path('delete/<int:id>/', delete_record, name='delete')
]



















































