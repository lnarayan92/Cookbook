import requests

# Get request
response = requests.get('https://httpbin.org')
print(response.text)  # HTML body
print(response.status_code)
print(response.headers)

print('------------------------------------------')

# Post request
response = requests.post(
    'https://httpbin.org/anything',
    data={'form_field_name': 'form_field_value'},
    files={'filename': 'file_contents'},
    params={'dk1': 'dv1'}
)
print(response.headers)
print(response.status_code)
print(response.text)

print('------------------------------------------')

# Post request with file streaming
with open('test.txt', 'r') as file_contents:
    response = requests.post(
        'https://httpbin.org/anything',
        data=file_contents
    )
    print(response.text)

