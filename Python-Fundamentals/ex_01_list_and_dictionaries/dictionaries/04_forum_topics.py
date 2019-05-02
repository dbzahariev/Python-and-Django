forum_dict = {}

data = input()
while not data.lower() == 'filter':
    pair = data.split(' -> ')
    topic = pair[0]
    if topic not in forum_dict:
        forum_dict[topic] = []

    for hashtag in pair[1].split(', '):
        if hashtag not in forum_dict[topic]:
            forum_dict[topic].append(hashtag)

    data = input()

target_topic_set = set(input().split(', '))
for topic, hashtag in forum_dict.items():
    if target_topic_set.issubset(set(hashtag)):
        print(f"{topic} | {', '.join(list(map(lambda x: '#' + x, hashtag)))}")
