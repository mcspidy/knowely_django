# Get count messages sent by first name

5xp

Consider the following models:

1. User model with the following fields:

- username - user's username
- first_name - user's first name
- last_name - user's last name
- bio - details such as age, country, or city

2. Chat model:

- title - chat title
- description - a short description of the chat
- users - many-to-many field, chat participants

3. Message model:

- text - message content
- sent - time when message was sent
- is_delivered - boolean value, True if the message was delivered successfully
- user - foreign key, points to the sender
- chat - foreign key, points to the chat where the message was sent

Implement a get_count_messages_sent_by_first_name function that should return the number of messages sent by all the users with a selected first_name.
