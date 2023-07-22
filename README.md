[English README is here](https://github.com/Pumi1a/ReactionDetectR/blob/main/README-en.md)
## はじめに
以前、Discord の返信や応答などに使われるリアクションに気づかないことがあり不便なため、リアクションに反応して通知してくれる Bot を作りました。ユーザがリアクションすると Bot がメッセージ主にメンションする流れになっています。動作に関しては[こちら](https://qiita.com/Pumila/items/cf447c24538e13994a38)を参考にして下さい。この度、この Bot を公開させて頂くことにしました（需要があるかは知りませんが…）。ぜひ使ってみて下さい。
![キャプチャ.PNG](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1115291/54a2de5e-a96a-3964-c84e-80a5daf9b0b7.png)

## 注意点
エラー報告は開発者の [Twitter](https://twitter.com/Pumi1a) か [github](https://github.com/Pumi1a/ReactionDetect) までお知らせ下さい。
なお、利用しているホスティングサービスは "Railway" になります。性能はメモリが 8GB、CPU が 8 コアになります。そこまで負荷のかかる Bot ではないと思いますが、もしかしたら安定しなくなるかもしれません。"Railway" については[こちら](https://qiita.com/Pumila/items/29f26fb349d5592046ae)を参考にして下さい。

# 導入方法
**注意：Bot の導入はサーバの管理者権限を持っている方しか出来ません。**

[こちら](https://discord.com/api/oauth2/authorize?client_id=1063085355726798869&permissions=2048&scope=bot%20applications.commands)からクリックしてログイン後、導入したいサーバを選択して[はい]、続いて認証を押下して下さい。ロボットかどうかの確認画面でチェックして導入完了です。

必要なくなったら、サーバ負荷軽減のために追放して頂けると助かります。

## 使い方
### 各スラッシュコマンドの説明
Bot の各スラッシュコマンドについて説明していきます。スラッシュコマンド実行時にエラーが出たときはもう一度コマンドを実行してみて下さい。

#### 通知先のチャンネルを変更する
通知先のチャンネルを変更することができます。デフォルトはシステムメッセージのチャンネルになっています。
1. "/" を入力して、リアクション通知くんのアイコンをクリックし、コマンド一覧から、`/set_channel` を選択して下さい。
2. 通知をさせたいチャンネル名を入力し、実行して下さい。候補として挙がっているものから選択しても構いません。
3. Bot に投稿権限がないチャンネル、もしくはテキストチャンネルではないチャンネルを選択した場合、以下のような警告が出ます。`Warning: No permission to post in the channel {new_channel.name}.`, `{new_channel.name} is not a text channel.`。
3. Bot から `Set channel to {new_channel_name}.` とメッセージが来ます。
![キャプチャ.PNG](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1115291/08c532b7-ca08-59f8-18f7-7aaec400dd19.png)

## 最後に
Discord のリアクションに反応し通知する Bot を作ったはいいものの、公開しようと思いつつ色々と忙しくて、公開できませんでした。ちょうど機会があったのでこの度公開させて頂きました。ぜひ使ってみて下さい。
サーバの維持費用のために、この Bot を気に入ってくれた方はご寄付して頂けると助かります。

【Amazon ギフト券 受取人：yskl6695@gmail.com】

https://www.amazon.co.jp/dp/B004N3APGO

【PayPal】

https://www.paypal.com/paypalme/IrsPumila

ご意見、ご感想、ご要望、エラー報告などは[Twitter](https://twitter.com/Pumi1a) まで。

