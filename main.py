import os
import openai

# set the API key
key = None
with open('API.key', 'r') as f:
    key = f.read().strip()
openai.api_key = os.environ["OPENAI_API_KEY"] = key

context = "(use JLPT N3 japanese)さとし:"
msg = "Context: You are さとし, a JLPT N3 Japanese teacher. \
    You will help me learn japanese through natural conversation., \
    \n私: よ\
    \nさとし: こんにちは\
    \n私: そう。面白いことが言おう。なんでもいい\n" + context
    
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
    stop=["私:", "さとし:"]
)
    # Print AI-san's response
    feedback = response["choices"][0]["text"].strip()
    print('さとし:', feedback)
    user = 'r'
    while user == 'r':
      os.system(f"python3.11 /Users/johannplaster/github/tomodachi/voice-api.py '{feedback}'")
      print('私：', end='')
      user = input()

    if user == 'q':
      quit()
        
    # By appending msg, the chatbot somewhat remembers past items
    msg += feedback + '\n私: ' + user + '\n' + context 
    
    # If we are almost exceeding the word count, cut it in half
    if msg.count(' ') > 240:
        print('\n\n(克：頭が悪いので、さとしさまはこの話の最初に忘れてしまいました。)\n\n')
        msg = context + msg[int(len(msg)/2):len(msg)]
