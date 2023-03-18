# chatgpt_for_line
概要：
LINE Messaging APIからPOSTされたデータを受け取り、
OpenAI APIにリクエストを送信して応答を取得し、
LINEにレスポンスを返す処理を実行します。

使い方：
LINE botからメッセージを送信します。
このアプリはAWS lambda、GCP cloud functionsなどの環境で実行される事を想定したコードです。

セットアップ：
・LINE　Messaging APIでbotを作成してください。
　LINE Messaging API: https://developers.line.biz/ja/reference/messaging-api/
・チャネルシークレット、チャネルアクセストークンを取得してください。

・OpenAI ChatGPTのAPI＿KEY、組織IDを取得してください。
API Referrence :https://platform.openai.com/docs/guides/chat/introduction

・バックエンドサーバを構築してください。（AWS lambda、GCP cloud functionsなどを想定したコードです）
・scriptのアップロードと環境変数に情報を設定してください。
 LINE_CHANNEL_ACCESS_TOKEN,
 LINE_CHANNEL_SECRET,
 OPENAI_API_KEY,
 OPENAI_ORGANIZATION_ID

・Messaging APIのwebhook先を用意してwebhook先に登録してください。
　AWS lambda、GCP cloud functionsなどの場合、API Gatewayなどを容易に用意することができます。

