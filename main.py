import tag_capture
import book_capture


print("capture tags example:")

tags =  tag_capture.captureTags()
for catalog in tags:
    name = catalog['name']
    tagsLen = len(catalog['tags'])
    exampleTagLink = catalog['tags'][0]['link']
    print(name, tagsLen, 'example:', exampleTagLink)

print('-----------------');
print('capture books example, only capture 20 lines:')

books = book_capture.listBooks('/tag/小说', 0)
# for bookLink in books:
#    print(bookLink)
print(books[0])

print('-----------------');
print('capture book info example:')

info = book_capture.captureBook(books[0])
print(info)