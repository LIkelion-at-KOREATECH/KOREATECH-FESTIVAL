from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from board_write.models import Board

import math
import os
import random
import string

# Create your views here.

def board(request):
        boards = Board.objects
        boards_list = Board.objects.all()
        paginator = Paginator(boards_list,3)
        if(request.GET.get('page') == None):
            page=1
        else:
            page = int(request.GET.get('page'))
    
        posts = paginator.get_page(page)
        page_range = 5 #페이지 범위 지정 예 1, 2, 3, 4, 5 / 6, 7, 8, 9, 10
        current_block = math.ceil(page/page_range) #해당 페이지가 몇번째 블럭인가
        start_block = (current_block-1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
        return render(request, 'board.html',{'boards' : boards , 'posts':posts , 'p_range':p_range , 'page': page})