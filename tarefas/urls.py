from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.tasks, name='tarefa'),
    path('task/<int:id>', views.taskviews, name='task'),
    path('new_task', views.nova_task, name='new_task'),
    path('edit/<int:id>', views.edittask, name='edittask'),
    path('changestatus/<int:id>', views.changestatus, name='changestatus'),
    path('delete/<int:id>', views.deletetask, name='deletetask'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)