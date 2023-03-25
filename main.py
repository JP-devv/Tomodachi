import os
import openai

# set the API key
key = None
with open('API.key', 'r') as f:
    key = f.read().strip()
openai.api_key = os.environ["OPENAI_API_KEY"] = key

msg = "Context: You will play a character called ヂイオ. Being from the anime \
    Jojo's bizarre adventure stardust crusaders, please speak with me in Japanese, \
    converse naturally with me and correct me to sound more natural.\
    \n人間: よろしくお願いします！\
    \nヂイオ: 貴様はジョジョではないなら、よろしくね \
    \n人間: はい、ジョジョではないんだ。ヂイオ様はの日はどうですか？ \
    \nヂイオ:"
while True:
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=msg,
    temperature=0.9,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["人間:", " ヂイオ:"]
)
    # Print AI-san's response
    feedback = response["choices"][0]["text"].strip()
    print('ヂイオ:', feedback)
    print('人間：', end='')
    
    # By appending msg, the chatbot somewhat remembers past items
    msg += feedback + '\n人間: ' + input() + '\nヂイオ:'
    
    # If we are almost exceeding the word count, cut it in half
    if msg.count(' ') > 240:
        context = "Stay in character! You're ヂイオ from \
            Jojo's bizarre adventure stardust crusaders\n"
        msg = context + msg[int(len(msg)/2):len(msg)]
