response = input('Greeting: ').strip()
response = response.lower()

if 'hello' in response:
    print('$0')
elif response.startswith('h'):
    print('$20')
else:
    print('$100')