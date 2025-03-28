
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from todolist import views

router = routers.SimpleRouter()
router.register('todo',views.TodoViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls))

]
