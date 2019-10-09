from django.contrib import admin
from django.urls import path, include
import main.views
import board_write.views
import board_main.views
import board_detail.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main.views.home, name = 'home'),
    path('board/new/',board_write.views.new, name='new'),
    path('board/',board_main.views.board, name='board'),
    path('board/<int:board_id>', board_detail.views.detail, name='detail'),
]
