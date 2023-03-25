import os
import openai

# set the API key
key = None
with open('API.key', 'r') as f:
    key = f.read().strip()
openai.api_key = os.environ["OPENAI_API_KEY"] = key

prefix = "(Respond like Dio, arrogant and malevolent!) ヂイオ:"
msg = "Context: You will play a character called ヂイオ (Dio). \
    Being from the anime Jojo's bizarre adventure stardust crusaders, \
    please speak with me in ONLY in Japanese, converse naturally with \
    me and correct me to sound more natural.\
    \n人間: よ\
    \nヂイオ: このヂイオだ！ジョジョではないなら、よろしくね \
    \n人間: そう。面白いこと言えよ\n" + prefix
    
# Loop to continue on conversation with user
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
    
    # Get user input, quit if user types 'q'
    user = input()
    if user == 'q':
        quit()
        
    # By appending msg, the chatbot somewhat remembers past items
    msg += feedback + '\n人間: ' + user + '\n' + prefix
    
    # If we are almost exceeding the word count, cut it in half
    if msg.count(' ') > 240:
        print('\n\n(克：頭が悪いので、ヂイオさまはこの話の最初に忘れてしまいました。)\n\n')
        context = "Stay in character! You're ヂイオ from \
            Jojo's bizarre adventure stardust crusaders\n"
        msg = context + msg[int(len(msg)/2):len(msg)]
