class Book:
    def __init__(self, title:str, author:str,content:str)->str:

        self.title = title
        self.author = author
        self.content = content



class BookSaver:
    @staticmethod
    def save_to_file(book: Book, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Title: {book.title}\nAuthor: {book.author}\n\n{book.content}")