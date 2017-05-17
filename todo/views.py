from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Memo

# Create your views here.

#トップ画面でTodoの一覧を表示する。
def todo_list(request):
    todo_list = get_list_or_404(Memo)
    print(todo_list)
    return render(request,'todo/list.html', {'todo_list': todo_list})

def todo_detail(request, pk):
    todo = get_object_or_404(Memo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})



