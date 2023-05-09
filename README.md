[English]
Using the power of GPT 3.5 Turbo, we have our own japanese tutor AI that will help us with JLPT N5 level japanese.

This requires that you create a file in the same directory called API.key, and you insert your davinci-003 key from OpenAI first.
found here https://platform.openai.com/account/api-keys. If you don't have one, its really cheap. It costs 3 cents per 1K tokens.

Also make sure you install the voicevox engine found here https://voicevox.hiroshiba.jp, by far the best I have found.
After installing their client, just run the program. This will also run a speech synthesis server in the background we will use.

make sure to run
python3 -m pip install -r requirements.txt

Afterwards, just run
python3 main.py

And you can talk with the AI! If you want the AI to repeat itself, just type "r" by itself, and if you want to quit type "q".

[日本語]
GPT 3.5 Turboの力を使って、私たちはJLPT N5レベルの日本語を教えてくれる独自の日本語チューターAIを持っています。

これには、API.keyという名前のファイルを同じディレクトリに作成し、最初にOpenAIから取得したdavinci-003キーを挿入する必要があります。
こちらから見つけることができます：https://platform.openai.com/account/api-keys。取得していない場合は、非常に安価で、1Kトークンあたり3セントかかります。

また、最高のエンジンとして見つけたvoicevoxエンジンをインストールすることも必要です。こちらからダウンロードできます：https://voicevox.hiroshiba.jp。
クライアントをインストールした後、プログラムを実行するだけで、バックグラウンドで音声合成サーバーも実行されます。

次に、以下を実行してください：
python3 -m pip install -r requirements.txt

その後、以下を実行するだけです：
python3 main.py

これでAIと話すことができます！ AIに自分自身を繰り返させたい場合は、単に「r」と入力し、終了する場合は「q」と入力してください。
