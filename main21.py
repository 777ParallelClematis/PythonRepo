import sys
from datetime import datetime

def get_response(text: str) -> str:
    lowered = text.lower()

    if lowered in ['hello', 'hi', 'hey']:
        return 'Hey there!'
    elif 'how are you' in lowered:
        return "I'm good, thanks."
    elif 'your name' in lowered:
        return 'My name is: Bot :)'
    elif 'time' in lowered:
        current_time = datetime.now()
        return f'The time is: {current_time:%H%M}'
    elif lowered in ['bye', 'see you', 'goodbye']:
        return 'It was nice talking to you.'
    else:
        return f'Sorry, I do not understand: "{text}".'

# Main loop (should not be inside the function)
while True:
    user_input = input('You: ')

    if user_input.lower() == 'exit':
        print('It was a pleasure talking to you.')
        sys.exit()

    bot_response = get_response(user_input)
    print(f'Bot: {bot_response}')

#futurework:
#add more functionality