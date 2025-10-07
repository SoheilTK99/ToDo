from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ToDosViewsetApiView)

urlpatterns = [
    path('', views.all_todos),
    # path('<int:todo_id>', views.todo_detail_view),
    # path('cbv/', views.ToDosListApiView.as_view()),
    # path('cbv/<int:todo_id>', views.ToDosDetailApiView.as_view()),
    # path('mixins/', views.ToDosListMixinApiView.as_view()),
    # path('mixins/<pk>', views.ToDosDetailMixinApiView.as_view()),
    # path('generics/', views.ToDoGenericApiView.as_view()),
    # path('generics/<pk>', views.ToDoGenericDetailApiView.as_view()),
    path('viewsets/', include(router.urls)),
    path('users/', views.UserGenericApiView.as_view()),
]