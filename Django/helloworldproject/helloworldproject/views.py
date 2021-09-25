from django.http import HttpResponse

# urls.pyで指定したhelloworldfuncを定義する
# request はウェブサーバー⇒wsgiという流れで送られてきたrequestオブジェクトのこと
def helloworldfunc(request):
    # HttpResponseクラスからresponseオブジェクトを作成し返す
    responseobject = HttpResponse('<h1>hello world</h1>')
    return responseobject 