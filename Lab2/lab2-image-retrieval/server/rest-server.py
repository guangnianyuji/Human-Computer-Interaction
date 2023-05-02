#!flask/bin/python
################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------
# This file implements the REST layer. It uses flask micro framework for server implementation. Calls from front end reaches
# here as json and being branched out to each projects. Basic level of validation is also being done in this file. #
# -------------------------------------------------------------------------------------------------------------------------------
################################################################################################################################
from flask import Flask, jsonify, abort, request, make_response, url_for, redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
import shutil
import numpy as np
from search import recommend
import tarfile
from datetime import datetime
from scipy import ndimage
#from scipy.misc import imsave

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
from tensorflow.python.platform import gfile

app = Flask(__name__, static_url_path="")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

# ==============================================================================================================================
#
#    Loading the extracted feature vectors for image retrieval
#
#
# ==============================================================================================================================
extracted_features = np.zeros((2955, 2048), dtype=np.float32)
with open('saved_features_recom.txt') as f:
    for i, line in enumerate(f):
        extracted_features[i, :] = line.split()
print("loaded extracted_features")


# ==============================================================================================================================
#
#  This function is used to do the image search/image retrieval
#
# ==============================================================================================================================
@app.route('/imgUpload', methods=['GET', 'POST'])
# def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_img():
    print("image upload")
    result = 'static/result'
    if not gfile.Exists(result):
        os.mkdir(result)
    shutil.rmtree(result)

    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:  # and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            recommend(inputloc, extracted_features)
            os.remove(inputloc)
            image_path = "/result"
            image_list = [os.path.join(image_path, file) for file in os.listdir(result)
                          if not file.startswith('.')]
            phototag = [[""], [""], [""], [""], [""], [""], [""], [""], [""]]

            # region tagfinder
            print(phototag)
            # region 将result文件夹中的图片名字保存到result_list中
            resultPath = 'static/result'
            result_list = os.listdir(resultPath)
            print(result_list)
            for i in range(0, len(result_list)):
                result_list[i] = result_list[i][2:]  # 去除搜索结果图片名中的im

                (filename, extension) = os.path.splitext(result_list[i])  # 划分文件名和后缀名
                result_list[i] = filename
            print(result_list)
            # endregion

            tagPath = 'database/tags'
            tag_list = os.listdir(tagPath)

            tagset = set()
            for tagnow in tag_list:
                with open("database/tags/" + tagnow, "r") as fp:
                    str_list = fp.readlines()  # 读取文件的全部信息存储到str_list中
                    (tagnowname,extension)=os.path.splitext(tagnow)
                    for ii in range(0, len(str_list)):
                        str_list[ii] = str_list[ii].rstrip()  # 去除行尾的\n

                    for jj in range(0, len(result_list)):
                        if str_list.count(result_list[jj]):    # 如果有第jj张图
                            print(result_list[jj])
                            print(jj)
                            print("已经有")
                            print(phototag[jj])
                            print("添加")
                            print(tagnowname)
                            phototag[jj].append(tagnowname)  # tag名加入
                            tagset.add(tagnowname)


            print(phototag)
            # endregion

            copy_list = image_list.copy()
            for i in range(0, len(copy_list)):
                copy_list[i] = copy_list[i][10:]
                (filename, extension) = os.path.splitext(copy_list[i])
                copy_list[i]=filename
            print(copy_list)


            taglist = []
            for tag in tagset:
                taglist.append(tag)

            images = {
                'image0': [image_list[0]],
                'image1': [image_list[1]],
                'image2': [image_list[2]],
                'image3': [image_list[3]],
                'image4': [image_list[4]],
                'image5': [image_list[5]],
                'image6': [image_list[6]],
                'image7': [image_list[7]],
                'image8': [image_list[8]],
                'tags': taglist,
                'phototag': phototag,
            }
            print("sourcepath")
            print(taglist)
            print(image_list)
            return jsonify(images)


# ==============================================================================================================================
#
#                                           Main function                                                        	            #
#
# ==============================================================================================================================
@app.route("/")
def main():
    return render_template("syfmain.html")


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
