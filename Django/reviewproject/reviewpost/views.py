from django.shortcuts import render
# usertableに保存するためにimport
from django.contrib.auth.models import User
# エラー処理のためにimport 
from django.db import IntegrityError
# login画面の為にimport
from django.contrib.auth import authenticate, login
# listviewのためにimport
from .models import ReviewModel

# renderの第1引数はrequest, 第2引数はtemplateとして使用する
# 第3引数はhtmlの中で、{{ somedata }} とすると使うことが可能
def signupview(request):
    # print文を入れるとterminalで表示される
    # print('signup function is called')
    
    # username_dataを表示させる
    # print(request.POST.get('username_data'))

    # ifでmethodにより処理を分岐させる
    # if request.method == 'POST':
    #     print('POST method')
    # else:
    #     print('GET method probably')

    if request.method == 'POST':
        # signup.htmlのnameで指定した名前
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        # usertableに追加
        # UserはUserテーブルを表しており、objectsがテーブルの中のデータを表している
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています。'})
    else:
        # all()は全データを表示
        print(User.objects.all())
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_date']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        # userがテーブルにある時
        if user is not None:
            # loginしたユーザーの情報はsessionの中に保存される
            login(request, user)
            # ページ遷移はredirect
            # renderはページの描画
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

def listview(request):
    object_list = ReviewModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

# 引数にpkが必要
def detailview(request, pk):
    # pkが一致するもののみデータを抽出
    object = ReviewModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})