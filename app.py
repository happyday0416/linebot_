# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

handler = WebhookHandler('9aac44af499a49df62d09d07fc63e12e') 
line_bot_api = LineBotApi('MeUVR5eGrkUWzG/Cx3p8TPAGpdCacdInZeM1vficawaAJsce9O+rjC4t/ugd82/zqGk1SfTtEb77wBmuLXN4VCh+taRCfPU26wmRB0OvrWan42Vl/2fwol7vP7IukcUmQjezmVC5APz1fgGp9yOr0AdB04t89/1O/w1cDnyilFU=') 


@app.route('/')
def index():
    return "<p>Hello World!</p>"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# ================= 機器人區塊 Start =================
@handler.add(MessageEvent, message=TextMessage)  # default
def handle_text_message(event):                  # default
    msg = event.message.text #message from user

    # 針對使用者各種訊息的回覆 Start =========
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))

    # 針對使用者各種訊息的回覆 End =========

# ================= 機器人區塊 End =================

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
