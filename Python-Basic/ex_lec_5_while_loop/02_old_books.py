book_to_find = input()
count_search = int(input())
count_checked = 0
is_found = "No"
while not count_search == 0:
    searched_book = input()
    if searched_book == book_to_find:
        print(f"You checked {count_checked} books and found it.")
        is_found = "Yes"
        break
    count_checked += 1
    count_search -= 1
if is_found == "No":
    print(f"The book you search is not here!")
    print(f"You checked {count_checked} books.")
