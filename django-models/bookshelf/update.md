Update_book = Book.object.get(title = '1984')
Update_book.title = "Nineteen Eighty-Four"

Book.object.all()