import os
from flask import Flask, request, redirect, url_for
from flask import flash
from werkzeug.utils import secure_filename
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np
import tensorflow
from keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical
from PIL import Image
from sklearn import model_selection

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)
# フォルダ名を指定
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

# エラーがでるので設定
app.secret_key = "super secret key"

# アップロード可能かどうかを確認する関数
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # もしメソッドがPOSTであれば
    if request.method == 'POST':
        # もしrequestの中にファイルが無ければ
        if 'file' not in request.files:
            flash('ファイルがありません')
            # アップロードのurlに返す
            return redirect(request.url)
        
        # ファイルを取り出す
        file = request.files['file']
        if file.filename =='':
            flash('ファイルがありません')
            return redirect(request.url)
        # もしファイルがあり、allowed_fileでTrueとなれば
        if file and allowed_file(file.filename):
            # 危険な文字を削除
            filename = secure_filename(file.filename)
            # 保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # アップロード後のurlのページに転送
            # return redirect(url_for('uploaded_file', filename=filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            model = load_model('./animal_cnn.h5')

            image = Image.open(filepath)
            image = image.convert('RGB') # Grayscaleの場合もカラーに変換
            image = image.resize((image_size, image_size))
            data = np.asarray(image)
            X = []
            X.append(data)
            X = np.asarray(X)

            result = model.predict([X])[0]
            predicted = result.argmax()
            percentage = int(result[predicted] * 100)
            return classes[predicted] + " " + str(percentage) + " %"
            
    return '''
    <!doctype html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>ファイルをアップロードして判定しよう</title></head>
    <body>
    <h1>ファイルをアップロードして判定しよう!</h1>
    <form method = post enctype = multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Upload>
    </form>
    </body>
    </html>
    '''

from flask import send_from_directory
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)