# Get chat dicts

Consider the following models:

1. User model with the following fields:

- username - user's username
- first_name - user's first name
- last_name - user's last name
- bio - details such as age, country ot city

Chat model:

- title - chat title
- description - a short chat description
- users - many-to-many field, chat participants

Message model:

- text - message content
- sent - time when the message was sent
- is_delivered - boolean value, True if the message was delivered successfully
- user - foreign key, points to the sender
- chat - foreign key, points to the chat where the message was sent

Implement a get_chat_dicts function that should return a list of chats represented by dicts. Each dict should contain the following fields:

- "id" - chat id
- "title" - chat title
- "users" - a list of the participants' usernames

    chats = get_chat_dicts()  
    print(chats[0])  
    \# {  
    \#    "id": 1,  
    \#    "title": "My family",  
    \#    "users": ["mom", "dad", "me"]  
    \# }
