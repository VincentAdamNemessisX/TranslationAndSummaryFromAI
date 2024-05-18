# Author: 
# created_time:
import json

import requests
from flask import Flask, request, url_for, jsonify

app = Flask(__name__)

translation_result = None
translate_state = False


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


@app.route('/api/v1/get/translation/from/zh-hans', methods=['POST'])
def get_translation_result_from_zh_hans():
    """
    获取中译英翻译结果
    :return: 中译英翻译结果
    """
    if request.method == 'POST':
        global translate_state
        global translation_result
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer app-sH92UTScnJGS5rR4hViuGmkA'
        }
        data = {
            "inputs": {
                "user_text": request.form.get('text'),
            },
            "user": "用户"
        }
        response = requests.post('https://api.dify.ai/v1/workflows/run',
                                 headers=headers, data=json.dumps(data))
        translation_result = response.json()
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': translation_result
        })
    return jsonify({
        'code': 400,
        'message': 'error',
        'data': 'method not allowed'
    })


@app.route('/api/v1/get/translation/from/eng', methods=['POST'])
def get_translation_result_from_eng():
    return 'get_translation_result'


@app.route('/api/v1/get/translate/progress', methods=['POST'])
def get_translate_progress():
    return 'get_translate_progress'
