from flask import Flask, request
import api

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def post_data():
    res = request.get_json()
    if res.get('message_type')=='private':# 如果是私聊信息
        print(res)
        uid = res.get('sender').get('user_id') # 获取信息发送者的 QQ号码
        gid = None
        message = res.get('raw_message') # 获取原始信息 
        message_id = res.get("message_id") # 获取群消息id
        message_role = res.get('sender').get('role')
        message_nickname = res.get('sender').get('nickname')
        api.keyword(message, uid, gid, message_id, message_role, message_nickname)
    if res.get('message_type')=='group':# 如果是群聊信息
        print(res)
        gid = res.get('group_id') # 获取群号
        uid = res.get('sender').get('user_id') # 获取信息发送者的 QQ号码
        message = res.get('raw_message') # 获取原始信息
        message_id = res.get("message_id") # 获取群消息id
        message_seq = res.get("message_seq")
        message_role = res.get('sender').get('role')
        if res.get('sender').get('card') != "":
            message_nickname = res.get('sender').get('card')
        else:
            message_nickname = res.get('sender').get('nickname')
        api.keyword(message, uid, gid, message_id, message_role, message_nickname)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8080)# 此处的 host和 port对应上面 yml文件的设置。-、=【-