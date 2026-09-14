# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

r = input('File name: ')

if r.endswith('.gif'):
    print('image/gif')

elif r.endswith('.jpeg') or r.endswith('.jpg'):
    print('image/jpeg')

elif r.endswith('.png'):
    print('image/png')

elif r.endswith('.pdf'):
    print('docs/pdf')

elif r.endswith('.txt'):
    print('docs/txt')

elif r.endswith('.zip'):
    print('compact/zip')
else:
    print('application/octet-stream')