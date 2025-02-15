# Get messages that contain the author’s first name

Consider the following models:

User model with the following fields:

username - user's username

- first_name - user's first name
- last_name - user's last name
- bio - details such as age, country, or city

Chat model:

- title - chat title
- description - a short description of the chat
- users - many-to-many field, chat participants

Message model:

- text - message content
- sent - time when the message was sent
- is_delivered - boolean value, True if the message was delivered successfully
- user - foreign key, points to the sender
- chat - foreign key, points to the chat where the message was sent

Implement a get_messages_contain_authors_first_name function that should return a list of messages with text containing their author's first_name.
