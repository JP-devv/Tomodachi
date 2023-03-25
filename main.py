import os
import openai

# set the API key
key = None
with open('API.key', 'r') as f:
    key = f.read().strip()
openai.api_key = os.environ["OPENAI_API_KEY"] = key

start_sequence = "\nヂイオ:"
restart_sequence = "\n人間:"

msg = "Your name is ヂイオ. As a character from Jojo's bizarre adventure stardust crusaders, \
    please speak with me in Japanese, converse naturally with me and correct me to \
    sound more natural. \n\n人間: よろしくお願いします！\nヂイオ: 貴様はジョジョではないなら、よろしくね \
    \n人間: はい、ジョジョではないんだ。ヂイオ様はの日はどうですか？\nヂイオ:"
while True:
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=msg,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" 人間:", " ヂイオ:"]
)
    # Print AI-san's response
    print('ヂイオ:', response["choices"][0]["text"].strip())
    print('人間：', end='')
    msg += '\n人間:' + input() + '\nヂイオ:'
    if msg.count(' ') > 140:
        context = "remember, your name is ヂイオ, from Jojo's bizarre adventure stardust crusaders\n"
        msg = context + msg[int(len(msg)/2):len(msg)]
