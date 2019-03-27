from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/tmp'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def hello():

     if request.method == 'POST':
#        f = request.files['file']
#        filename = secure_filename(f.filename)
#        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#        #return redirect(url_for('uploaded_file',filename=filename))
       return "hiiiii"
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
