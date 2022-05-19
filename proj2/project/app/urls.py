from django.urls import path
from . import views, user_auth

urlpatterns = [

        path('', views.apiOverview),
        path('task-list/', views.taskList, name="task-list"),
        path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
        path('task-create/', views.taskCreate, name="task-create"),
        path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
        path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
        path('task-list-1/', views.taskList1, name="task-list"),
        path('task-detail-1/<str:pk>/', views.taskDetail1, name="task-detail"),
        path('task-create-1/', views.taskCreate1, name="task-create"),
        path('task-update-1/<str:pk>/', views.taskUpdate1, name="task-update"),
        path('task-delete-1/<str:pk>/', views.taskDelete1, name="task-delete"),
        path('task-list-add/', views.taskList2, name="task-list"),
        path('task-detail-add/<str:pk>/', views.taskDetail2, name="task-detail"),
        path('task-create-add/', views.taskCreate2, name="task-create"),
        path('task-update-add/<str:pk>/', views.taskUpdate2, name="task-update"),
        path('task-delete-add/<str:pk>/', views.taskDelete2, name="task-delete"),
        path('hello/', user_auth.HelloView.as_view(), name='hello'),
]



