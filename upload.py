'''
@author：KongWeiKun
@file: upload.py
@time: 17-12-6 下午4:33
@contact: 836242657@qq.com
'''
import os
from flask import Flask,request,url_for,send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/kongweikun/PycharmProjects/flask_uplaod/picture'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.getcwd() #返回当前工作目录
app.config['MAX_CONTENT_LENGTH']=16*1024*1024


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=upload>
    </form>
    '''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/',methods=['POST','GET'])
def upload_file():
    if request.method=='POST':
        file=request.files['file']
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            file_url=url_for('uploaded_file',filename=filename)

            return html+'<br><img src='+file_url+'>'
    return html


if __name__ == '__main__':
    app.run(port=9006,debug=True)