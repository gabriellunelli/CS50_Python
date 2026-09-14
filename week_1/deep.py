response = input('What is the Answer to the Great Question of Life, the Universe, and Everything?').replace('-', ' ')
response = response.strip()
response = response.lower()

if response == 'forty two' or response == '42':
    print('Yes')
else:
    print('No')