from django.urls import path

from .views import todo_list, todo_details, todo_create, todo_update, todo_delete

app_name = 'todos'

urlpatterns = [
    #first parameter is the path the second parameter is the function in "views.py" that should be referenced. 
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_details),
    path('<id>/update/', todo_update),
    path('<id>/delete/', todo_delete),
]