class Book:
    all_books = []

    def __init__(self, title, author, price, chapters):
        self.title = title,
        self.author = author,
        self.price = float(price),
        self.chapters = chapters,

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    @property
    def chapters(self):
        return self.__chapters

    @title.setter
    def title(self, title):
        self.__title = title[0]

    @author.setter
    def author(self, author):
        self.__author = author[0]

    @price.setter
    def price(self, price):
        self.__price = float(price[0])

    @chapters.setter
    def chapters(self, chapters):
        self.__chapters = chapters[0]

    def __str__(self):
        return f"SOLD: {self.title} with author {self.author}. Chapters in the book {len(self.chapters)}"


def detect_is_book_in_db(search):
    for book in data_base:
        if book.title == search:
            return book
    return False


data_base = []
while True:
    data = input()
    if data == 'on work':
        break
    data = data.split(' -> ')
    if len(data[0].split()) != 3:
        continue
    title, author, price = data[0].split()
    try:
        price = float(price)
    except:
        continue
    if price <= 0:
        continue
    chapters = data[1].split(', ')
    one_book = Book(title, author, price, chapters)
    data_base.append(one_book)

money = 0
not_found_books_count = 0
founded_books = []
while True:
    data = input()
    if data == 'end work':
        break
    detected_book = detect_is_book_in_db(data)
    if detected_book:
        founded_books.append(detected_book)
        # data_base.remove(detected_book)
        money += detected_book.price
    else:
        not_found_books_count += 1

for _ in range(not_found_books_count):
    print('No such book here')
for book in founded_books:
    print(book)

if money > 0:
    print(f'Money: {money:.2f}')
else:
    print(f'Bad day :(')
