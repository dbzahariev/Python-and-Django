text_to_search = input()

found_carats = []
while True:
    count_diamonds = 0
    start_index = text_to_search.find('<')
    end_index = text_to_search.find('>')
    if start_index == -1 or end_index == -1:  # print carats
        if len(found_carats) == 0:
            print('Better luck next time')
        else:
            for carat in found_carats:
                print(f'Found {carat} carat diamond')
        break
    mini_text = text_to_search[start_index + 1:end_index]
    for letter in mini_text:
        if letter.isdigit():
            count_diamonds += int(letter)
    text_to_search = text_to_search[end_index + 1:]  # next part of text
    if count_diamonds != 0:
        found_carats.append(count_diamonds)
