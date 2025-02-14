# Get messages that contain a word

Consider the following models:

1. User model with the following fields:  

- username - user's username
- first_name - user's first name
- last_name - user's last name
- bio - details such as age, country, or city

2. Chat model  

- title - chat title
- description - a short description of the chat
- users - many-to-many field, chat participants

3. Message model:  

- text - message content
- sent - time when the message was sent
- is_delivered - boolean value, True if the message was delivered successfully
- user - foreign key, points to the sender
- chat - foreign key, points to the chat where the message was sent

Implement a get_messages_that_contain_word function that takes word as an argument and returns a list of messages that contain word in their text. Use a case-insensitive containment test.
