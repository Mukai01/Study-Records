from django.shortcuts import render
# usertableに保存するためにimport
from django.contrib.auth.models import User
# エラー処理のためにimport 
from django.db import IntegrityError

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