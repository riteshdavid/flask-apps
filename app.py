
from flask import Flask, render_template, request, jsonify


WTF_CSRF_SECRET_KEY = 'something here'



app = Flask(__name__)
app.secret_key = 'secret key'

app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif','pdf','json'])



 
    # in ALLOWED_EXTENSIONS

def allow_file(filename):
    return filename.rsplit('.', 1)[1].lower()


@app.route('/file-upload', methods=['POST'])
def file_upload():

    # check if the post request has the file part
    if len(request.files)==2:
        file1,file2=request.files['file1'],request.files['file2']
        ext_file1=allow_file(file1.filename)
        ext_file2=allow_file(file2.filename)
        
    # check to see if file has other types
        if  not(ext_file1=='json' and ext_file2=='pdf'):
            resp = jsonify({'message':'Check For First File is json and Second file is pdf' })
            resp.status_code=400
            return resp
    # Run if first file is json and second file is pdf
        resp = jsonify({"message" : f"First File is {ext_file1} and Second is {ext_file2}"})
        resp.status_code=200
        return resp   
        
    # Otherwise send message 
    else:
        resp = jsonify({'message' : 'Send Two files (file1,file2) one JSON file and one PDF file' })
        resp.status_code = 400
        return resp

    





if __name__ == "__main__":
    app.run(port=8001)
