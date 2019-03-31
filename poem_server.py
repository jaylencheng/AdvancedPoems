# coding=utf8
import os
from flask import Flask, request, render_template
from write_poem import WritePoem, start_model

app = Flask(__name__)
application = app

# # 获取当前工作目录
# path = os.getcwd()
# print(path)

writer = start_model()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/poem')
def poem():
    params = request.args
    head = None
    poem = None
    swag = 'Random'

    if 'start' != 'undefined':
        head = params['start']
    if 'style' != 'undefined':
        swag = params['style']

    print('HEAD====='+head)
    print('STYLE===='+swag)

    if head and head != 'undefined':
        if swag == 'GeHead' and len(head) > 1:
            poem = writer.cangtou(head)
        else:
            poem = writer.hide_words(head)
    else:
        head = '无题'
        if swag == 'Random':
            poem = writer.free_verse()
        elif swag == 'Rhymes':
            poem = writer.rhyme_verse()

    if poem:
        sentences = poem.split('。')
        poem = [sentence + '。' for sentence in sentences if sentence != '']

    return render_template('poem.html', head=head, poem=poem)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
