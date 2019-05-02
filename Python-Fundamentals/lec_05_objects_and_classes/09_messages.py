class User:
    def __init__(self, Username):
        self.Username = Username
        self.ReceivedMessages = []


class Message:
    def __init__(self, Content, Sender):
        self.Content = Content
        self.Sender = Sender


users_list = []
usernames_list = []

while True:
    data = input().split()
    if data[0].lower() == 'exit':
        data = input().split()

        if len(data) != 2:
            print(f'No messages')
            break

        count_message = 0
        from_user = data[0]
        to_user = data[1]

        if from_user not in usernames_list or to_user not in usernames_list:
            # print(f'No messages')
            break

        index = -1
        while True:
            if from_user == to_user:
                # count_message += 1
                break
            index += 1
            for_user = [from_user, to_user][index % 2 == 1]
            for_user_2 = [from_user, to_user][index % 2 == 0]
            if for_user not in usernames_list and for_user_2 not in usernames_list:
                break
            for user in users_list:
                if user.Username == for_user_2:
                    if len(user.ReceivedMessages) == 0:
                        del users_list[users_list.index(user)]
                        del usernames_list[usernames_list.index(user.Username)]
                        break
                    for message in user.ReceivedMessages:
                        if message.Sender == for_user:
                            count_message += 1
                            if [from_user, to_user].index(for_user) == 0:
                                print(f'{for_user}: {message.Content}')
                            if [from_user, to_user].index(for_user) == 1:
                                print(f'{message.Content} :{for_user}')
                            del user.ReceivedMessages[user.ReceivedMessages.index(message)]
                        else:
                            del user.ReceivedMessages[user.ReceivedMessages.index(message)]
                        if len(user.ReceivedMessages) == 0:
                            del users_list[users_list.index(user)]
                            del usernames_list[usernames_list.index(user.Username)]
                        break
        if count_message == 0:
            print(f"No messages")
        break
    if data[0].lower() == 'register':
        if len(data) != 2:
            break
        one_user = User(data[1])
        if one_user not in users_list:
            users_list.append(one_user)
        if one_user.Username not in usernames_list:
            usernames_list.append(one_user.Username)
    elif data[1].lower() == 'send':
        if len(data) != 4:
            break
        one_massage = Message(data[3], data[0])
        for user in users_list:
            if user.Username == data[2]:
                if data[0] in usernames_list and data[2] in usernames_list:
                    user.ReceivedMessages.append(one_massage)
                    break
