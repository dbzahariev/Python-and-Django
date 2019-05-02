my_dict = {}


def print_result(this_dict):
    for key, value in this_dict.items():
        print(f"Post: {key} | Likes: {value['like']} | Dislikes: {value['dislike']}")
        print(f'Comments:')
        if not value['comment']:
            print('None')
            continue
        for comment in value['comment']:
            print(f"*  {comment[0]}: {comment[1]}")


while True:
    entrance = input()
    if entrance.lower() == 'drop the media':
        print_result(my_dict)
        break

    entrance = entrance.split()
    post_name = entrance[1]
    command = entrance[0].lower()

    if command == 'post':
        my_dict[post_name] = {'like': 0, 'dislike': 0, 'comment': []}
    else:
        if post_name in my_dict.keys():
            if command == 'like' or command == 'dislike':
                my_dict[post_name][command] += 1
            elif command == 'comment':
                if len(entrance) >= 4:
                    my_dict[post_name][command].append((entrance[2], ' '.join(entrance[3:])))
