import os
import json
import requests
import openai
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextSendMessage

# LineBotのアクセストークン
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
# LINE Developer CenterのWebhook URLに設定した任意の値
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
# OpenAIのAPIキー
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# OpenAIの組織ID
OPENAI_ORGANIZATION_ID = "org-FES790D6H5dR94Ts8ckyHF3B"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(LINE_CHANNEL_SECRET)
openai.api_key = OPENAI_API_KEY
openai.organization = OPENAI_ORGANIZATION_ID
openai.Model.list()


def line_webhook(request):
    """LINE Messaging APIからPOSTされたデータを受け取り、レスポンスを行う。
    param request: request情報
    Returns:_type_: _description_
    LINE Messaging API: https://developers.line.biz/ja/reference/messaging-api/
    """
    if request.method != 'POST':
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'request_method is not POST'})
        }

    # リクエスト情報取得
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        # 署名を検証し、イベント情報をパース
        events = parser.parse(body, signature)
        # イベントがMessageEventだった場合
        for event in events:
            if isinstance(event, MessageEvent):
                message_text = event.message.text
                res_text = request_openai(message_text)
                # LINEにレスポンスを返す
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=res_text)
                )        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'success'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request'})
        }



def request_openai(message_text: str ) -> str:
    """OpenAI APIにリクエストを送信して、返答を取得する関数
    param str message_text: OpenAIへの質問文
    Returns:str: _description_
    API Referrence :https://platform.openai.com/docs/guides/chat/introduction
    """
    try:
        # OpenAIにリクエストを送信
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message_text},
            ]
        )
        # response check and return
        res_finish_reason = response['choices'][0]['finish_reason']
        res_message_content = response['choices'][0]['message']['content']
        if res_finish_reason == "stop":
            return res_message_content
        elif res_finish_reason == "length":
            return (res_message_content + "トークンの制限により、不完全な回答です。")
        else:
            return "回答を得られませんでした。"
    except openai.OpenAIError as e:
        return f"エラーが発生しました: {e}"
