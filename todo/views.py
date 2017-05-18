from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Memo
from .forms import EditForm


# Create your views here.

#トップ画面でTodoの一覧を表示する。
def todo_list(request):
    todo_list = get_list_or_404(Memo)
    print(todo_list)
    for todo in todo_list:        
        print(todo.id)
    return render(request,'todo/list.html', {'todo_list': todo_list})

#詳細ビュー
def todo_detail(request, pk):
    print(pk)
    memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': memo})

#新規作成ビュー
def todo_new(request):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('detail', pk=memo.id)
    else:
        form = EditForm()        
    return render(request, 'todo/todo_edit.html', {'form':form})

#編集ビュー
def todo_edit(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if request.method == "POST":
        form = EditForm(request.POST, instance=memo)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('detail', pk=memo.id)
    else:
        form = EditForm(instance=memo)
    return render(request, 'todo/todo_edit.html', {'form': form})

def todo_delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if request.method == "POST":
        #削除する
        memo.delete()
        return redirect('top')
    return render(request, 'todo/todo_delete.html', {'todo': memo})
