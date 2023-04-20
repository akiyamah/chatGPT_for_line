# 概要
LINE Messaging APIからPOSTされたデータを受け取り、OpenAI APIにリクエストを送信して応答を取得し、LINEにレスポンスを返す処理を実行します。

## 構成
・ユーザーはLINEからLINE　BOTへメッセージを送信。
・LINE Messaging APIからwebhook先に登録したAPI GatewayへPOST。
・当該機能が起動し、ChatGPTへリクエスト送信。
・ChatGPTからのレスポンスに適切な処理を行い、LINE Messaging APIへ返す。
・LINEでユーザーへ返す。

# 準備
### LINE　Messaging APIでbotを作成
　LINE Messaging API: https://developers.line.biz/ja/reference/messaging-api/
チャネルシークレット、チャネルアクセストークンを取得してください。

### OpenAI ChatGPTのAPI＿KEY、組織IDを取得
API Referrence :https://platform.openai.com/docs/guides/chat/introduction

### バックエンドサーバを構築
一例としてAWS lambda、GCP cloud functionsなどの環境でscriptのアップロードと環境変数に情報を設定してください。
 LINE_CHANNEL_ACCESS_TOKEN,
 LINE_CHANNEL_SECRET,
 OPENAI_API_KEY,
 OPENAI_ORGANIZATION_ID
 
### API Gateway作成
　AWS lambda、GCP cloud functionsなどの場合、API Gatewayなどを容易に用意することができます。

### webhook設定
Messaging APIのwebhook先を用意(API Gateway)してwebhook先に登録してください。

### botの登録
LINEアプリなどからbotを登録して下さい。

# 実行
### LINE BOTでメッセージ送信。
LINE BOTでメッセージ送信して下さい。
