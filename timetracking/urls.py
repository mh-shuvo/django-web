from django.urls import path

from . import views
urlpatterns = [
    path("",views.index,name='index'),
    path("<int:id>/history",views.history,name='history'),
    path("/working_histories",views.get_working_histories,name='working_histories'),
]