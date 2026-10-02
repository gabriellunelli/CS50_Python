# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

r = input('File name: ').lower().strip()

if r.endswith('.gif'):
    print('image/gif')

elif r.endswith('.jpeg') or r.endswith('.jpg'):
    print('image/jpeg')

elif r.endswith('.png'):
    print('image/png')

elif r.endswith('.pdf'):
    print('application/pdf')

elif r.endswith('.txt'):
    print('text/plain')

elif r.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')