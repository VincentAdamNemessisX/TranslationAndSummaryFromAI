# Author: 
# created_time:
import json

import requests
from flask import Flask, request, url_for, jsonify, Response

app = Flask(__name__)

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer app-sqOp6VXprejI5U1KH1kyskuX'
}


@app.route('/api/v1/get/function/list', methods=['GET'])
def get_function_list():
    """
    获取功能列表
    :return: 功能列表
    """
    if request.method == 'GET':
        function_list = [
            {
                'name': '中译英',
                'url': url_for('get_translation_result_from_zh_hans'),
                'method': 'POST',
                'params': [
                    {
                        'name': 'text',
                        'type': 'string',
                        'required': True,
                        'description': '需要翻译的文本'
                    }
                ],
                'description': '将中文翻译为英文'
            },
            {
                'name': '英译中',
                'url': url_for('get_translation_result_from_eng'),
                'method': 'POST',
                'params': [
                    {
                        'name': 'text',
                        'type': 'string',
                        'required': True,
                        'description': '需要翻译的文本'
                    }
                ],
                'description': '翻译英文到中文'
            },
            {
                'name': '获取翻译进度',
                'url': url_for('get_translate_progress'),
                'method': 'POST',
                'params': [
                    {
                        'name': 'text',
                        'type': 'string',
                        'required': True,
                        'description': '需要翻译的文本'
                    }
                ],
                'description': '翻译英文到中文'
            }
        ]
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': function_list
        })
    return jsonify({
        'code': 400,
        'message': 'error',
        'data': 'method not allowed'
    })


@app.route('/api/v1/get/translation/from/zh-hans/<int:trunk>/', methods=['POST'])
def get_translation_result_from_zh_hans(trunk=0):
    """
    获取中译英翻译结果
    :return: 中译英翻译结果
    """
    if request.method == 'POST':
        global headers
        try:
            if trunk:
                data = {
                    "inputs": {
                        "type": "翻译",
                        "user_text": request.form.get('text'),
                    },
                    "user": request.form.get('user'),
                    "response_mode": "streaming"
                }
            else:
                data = {
                    "inputs": {
                        "type": "翻译",
                        "user_text": request.form.get('text')
                    },
                    "user": request.form.get('user')
                }
        except Exception as e:
            return jsonify({
                'code': 400,
                'message': 'error',
                'data': 'params error' + str(e)
            })
        response = requests.post('http://localhost:5001/v1/workflows/run',
                                 headers=headers, data=json.dumps(data), stream=bool(trunk))

        def generate():
            for chunk in response.iter_content(chunk_size=1024):
                yield chunk

        if trunk:
            return Response(generate(), mimetype='text/event-stream')
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': response.json()
        })
    return jsonify({
        'code': 400,
        'message': 'error',
        'data': 'method not allowed'
    })


@app.route('/api/v1/get/translation/from/eng/[int:trunk]>/', methods=['POST'])
def get_translation_result_from_eng(trunk=0):
    if request.method == 'POST':
        global headers
        try:
            if trunk:
                data = {
                    "inputs": {
                        "type": "翻译",
                        "user_text": request.form.get('text'),
                    },
                    "user": request.form.get('user'),
                    "response_mode": "streaming"
                }
            else:
                data = {
                    "inputs": {
                        "type": "翻译",
                        "user_text": request.form.get('text')
                    },
                    "user": request.form.get('user')
                }
        except Exception as e:
            return jsonify({
                'code': 400,
                'message': 'error',
                'data': 'params error' + str(e)
            })
        response = requests.post('http://localhost:5001/v1/workflows/run',
                                 headers=headers, data=json.dumps(data), stream=bool(trunk))

        def generate():
            for chunk in response.iter_content(chunk_size=1024):
                yield chunk

        if trunk:
            return Response(generate(), mimetype='text/event-stream')
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': response.json()
        })
    return jsonify({
        'code': 400,
        'message': 'error',
        'data': 'method not allowed'
    })


@app.route('/api/v1/get/summary/from/paragraph/<int:trunk>', methods=['POST'])
def summary(trunk):
    if request.method == 'POST':
        global headers
        try:
            if trunk:
                data = {
                    "inputs": {
                        "type": "总结",
                        "user_text": request.form.get('text')
                    },
                    "user": request.form.get('user'),
                    "response_mode": "streaming"
                }
            else:
                data = {
                    "inputs": {
                        "type": "总结",
                        "user_text": request.form.get('text')
                    },
                    "user": request.form.get('user')
                }
        except Exception as e:
            return jsonify({
                'code': 400,
                'message': 'error',
                'data': 'params error' + str(e)
            })
        response = requests.post('http://localhost:5001/v1/workflows/run',
                                 headers=headers, data=json.dumps(data), stream=bool(trunk))

        def generate():
            for chunk in response.iter_content(chunk_size=1024):
                print(chunk)
                yield chunk

        if trunk:
            return Response(generate(), mimetype='text/event-stream')
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': response.json()
        })
    return jsonify({
        'code': 400,
        'message': 'error',
        'data': 'method not allowed'
    })


@app.route('/api/v1/get/generate/progress', methods=['POST'])
def get_translate_progress():
    return 'get_translate_progress'
