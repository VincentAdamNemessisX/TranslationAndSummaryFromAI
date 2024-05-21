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


@app.route('/api/v1/get/function/list', methods=['GET', 'POST'])
def get_function_list():
    """
    获取功能列表
    :return: 功能列表
    """
    function_list = [
        {
            'name': '中译英（一次性返回）',
            'url': url_for('get_translation_result_from_zh_hans', trunk=0),
            'method': 'POST',
            'params': [
                {
                    'name': 'user_text',
                    'type': 'string',
                    'required': True,
                    'max_length': 10000,
                    'description': '需要翻译的文本'
                }
            ],
            'description': '将中文翻译为英文'
        },
        {
            'name': '中译英（流式传输，分段返回）',
            'url': url_for('get_translation_result_from_zh_hans', trunk=1),
            'method': 'POST',
            'params': [
                {
                    'name': 'user_text',
                    'type': 'string',
                    'required': True,
                    'max_length': 10000,
                    'description': '需要翻译的文本'
                }
            ],
            'description': '将中文翻译为中文'
        },
        {
            'name': '英译中（一次性返回）',
            'url': url_for('get_translation_result_from_eng', trunk=0),
            'method': 'POST',
            'params': [
                {
                    'name': 'user_text',
                    'type': 'string',
                    'required': True,
                    'max_length': 10000,
                    'description': '需要翻译的文本'
                }
            ],
            'description': '将英文翻译为中文'
        },
        {
            'name': '英译中（流式传输，分段返回）',
            'url': url_for('get_translation_result_from_eng', trunk=1),
            'method': 'POST',
            'params': [
                {
                    'name': 'user_text',
                    'type': 'string',
                    'required': True,
                    'max_length': 10000,
                    'description': '需要翻译的文本'
                }
            ],
            'description': '将英文翻译为中文'
        },
        {
            'name': '获取总结内容（一次性返回）',
            'url': url_for('get_summary', trunk=0),
            'method': 'POST',
            'params': [
                {
                    'name': 'user_text',
                    'type': 'string',
                    'required': True,
                    'max_length': 10000,
                    'description': '需要总结的内容'
                }
            ],
            'description': '总结输入的文本内容'
        },
        {
            'name': '获取总结内容（流式传输，分段返回）',
            'url': url_for('get_summary', trunk=1),
            'method': 'POST',
            'params': [
                {
                    'name': 'user_text',
                    'type': 'string',
                    'required': True,
                    'max_length': 10000,
                    'description': '需要总结的内容'
                }
            ],
            'description': '总结输入的文本内容'
        }
    ]
    return jsonify({
        'code': 200,
        'message': 'success',
        'data': function_list
    })


@app.route('/api/v1/get/translation/from/zh-hans/<int:trunk>', methods=['POST'])
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
                    "user": "用户",
                    "response_mode": "streaming"
                }
            else:
                data = {
                    "inputs": {
                        "type": "翻译",
                        "user_text": request.form.get('text')
                    },
                    "user": "用户"
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


@app.route('/api/v1/get/translation/from/eng/<int:trunk>', methods=['POST'])
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
                    "user": "用户",
                    "response_mode": "streaming"
                }
            else:
                data = {
                    "inputs": {
                        "type": "翻译",
                        "user_text": request.form.get('text')
                    },
                    "user": "用户"
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
def get_summary(trunk):
    if request.method == 'POST':
        global headers
        try:
            if trunk:
                data = {
                    "inputs": {
                        "type": "总结",
                        "user_text": request.form.get('text')
                    },
                    "user": "用户",
                    "response_mode": "streaming"
                }
            else:
                data = {
                    "inputs": {
                        "type": "总结",
                        "user_text": request.form.get('text')
                    },
                    "user": "用户"
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
