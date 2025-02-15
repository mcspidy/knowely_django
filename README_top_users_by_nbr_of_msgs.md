# Get top users by number of the messages

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
- sent - time when the message was sent
- is_delivered - boolean value, True if the message was delivered successfully
- user - foreign key, points to the sender
- chat - foreign key, points to the chat where the message was sent

Implement a get_top_users_by_number_of_the_messages function that should return the top 3 users by number of messages sent, with an additional num_messages field containing a value equal to this number.

    users = get_top_users_by_number_of_the_messages()
    
    print(
        users[0].username,  # "user1"
        users[0].num_messages  # 7
    )
