from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PhotoForm
from .models import Photo

# index.htmlを返す
def index(request):
    # テンプレートを読み込んで変数にセット
    template = loader.get_template('animalai/index.html')
    context = {'form':PhotoForm()}
    # return HttpResponse("Hello World!")
    return HttpResponse(template.render(context, request))

def predict(request):
    # データが送られてきたか確認する
    if not request.method == 'POST':
        return redirect('animalai:index')
    
    form = PhotoForm(request.POST, request.FILES)
    # 有効なデータだと先に進む
    if not form.is_valid():
        raise ValueError('Formが不正です')

    photo = Photo(image=form.cleaned_data['image'])
    # 返り値を受け取る
    predicted, percentage = photo.predict()
    template = loader.get_template('animalai/result.html')
    context = {
        "photo_data": photo.image_src(),
        "photo_name":photo.image.name,
        "predicted":predicted,
        "percentage":percentage,}
    return HttpResponse(template.render(context, request))

    # return HttpResponse("Show predictions")

