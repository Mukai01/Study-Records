from django.shortcuts import render

# renderの第1引数はrequest, 第2引数はtemplateとして使用する
# 第3引数はhtmlの中で、{{ somedata }} とすると使うことが可能
def signupview(request):
    # print文を入れるとterminalで表示される
    # print('signup function is called')
    
    # username_dataを表示させる
    print(request.POST.get('username_data'))
    return render(request, 'signup.html', {'somedata':100})