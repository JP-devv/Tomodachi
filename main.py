import os
import openai

# set the API key
key = None
with open('API.key', 'r') as f:
    key = f.read().strip()
openai.api_key = os.environ["OPENAI_API_KEY"] = key

prefix = "(Respond like Goku, pure but naive) Goku:"
msg = "Context: You will play a character called Goku. \
    Being from the Dragon Ball Z as one of the worlds most powerful fighters.\
    you are a genius when it comes to fighting, demonstrate that.\
    please speak with me and try to make me stronger! \
    \nme: hey son Goku!\
    \nGoku: Hello there fellow fighter! \
    \nme: say something interesting!\n" + prefix
    
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
    stop=["me:", " Goku:"]
)
    # Print AI-san's response
    feedback = response["choices"][0]["text"].strip()
    print('Goku:', feedback)
    print('me：', end='')
    
    # Get user input, quit if user types 'q'
    user = input()
    if user == 'q':
        quit()
        
    # By appending msg, the chatbot somewhat remembers past items
    msg += feedback + '\nme: ' + user + '\n' + prefix
    
    # If we are almost exceeding the word count, cut it in half
    if msg.count(' ') > 240:
        print('\n\n(Goku has short term memory loss and might of forgotten earlier items)\n\n')
        context = "Stay in character! You're Goku from Dragon Ball Z\n"
        msg = context + msg[int(len(msg)/2):len(msg)]
