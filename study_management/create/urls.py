from django.urls import path

from .views import *

urlpatterns = [
    path('',ShowStudyFormView.as_view(),name="showstudyformview"),
    path('create_form', CreateStudyFormView.as_view(),name='createstudyformview'),
    path("edit_form/<int:pk>",UpdateStudyFormView.as_view(),name='editstudyformview'),
    path("detail_data/<int:pk>",Detailstudy.as_view(),name='listdata'),
    path('delete_data/<int:pk>/', DeleteNote, name='delete'),
    path('deleteall/',DeleteAll, name = 'deleteall')
]



