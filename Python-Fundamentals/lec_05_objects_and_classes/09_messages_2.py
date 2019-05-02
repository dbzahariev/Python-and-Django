class User:
    def __init__(self, Username):
        self.Username = Username
        self.ReceivedMessages = []

    def add_message(self, data, sender):
        if sender in get_all_usernames():
            sender = get_one_user(sender)
            one_message = Message(data[3], sender)
            self.ReceivedMessages.append(one_message)


class Message:
    def __init__(self, Content, Sender):
        self.Content = Content
        self.Sender = Sender


def print_message(username_one, username_two):
    if username_one not in get_all_usernames() or username_two not in get_all_usernames():
        return

    # Get messages for user
    all_messages_for_user_one = get_one_user(username_one).ReceivedMessages
    all_messages_with_user_two = list(filter(lambda x: x.Sender.Username == username_two, all_messages_for_user_one))
    all_messages_for_user_two = get_one_user(username_two).ReceivedMessages
    all_messages_with_user_one = list(filter(lambda x: x.Sender.Username == username_one, all_messages_for_user_two))

    if len(all_messages_with_user_two) == 0 and len(all_messages_with_user_one) == 0:
        print('No messages')

    i = -1
    while True:
        i += 1
        if i >= len(all_messages_with_user_one) and i >= len(all_messages_with_user_two):
            break
        if i < len(all_messages_with_user_two):
            print(f'{username_one}: {all_messages_with_user_two[i].Content}')
        if i < len(all_messages_with_user_one):
            print(f'{all_messages_with_user_one[i].Content} :{username_two}')


def get_all_usernames():
    return list(map(lambda x: x.Username, all_users))


def get_one_user(searched_name):
    user = list(filter(lambda x: x.Username == searched_name, all_users))
    if len(user) != 0:
        return user[0]
    return -1


all_users = []
while True:
    data = input().split()

    if data[0].lower() == 'exit':
        data = input().split()
        if len(data) == 2:
            print_message(data[0], data[1])
        break
    if data[0].lower() == 'register':
        one_username = User(data[1])
        if one_username.Username not in get_all_usernames():
            all_users.append(one_username)
            get_all_usernames().append(one_username.Username)
    elif data[1].lower() == 'send':
        if data[0] in get_all_usernames() and data[2] in get_all_usernames():
            get_one_user(data[0]).add_message(data, data[2])
