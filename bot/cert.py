import certifi
import requests

try:
    print('Checking connection to Discord...')
    test = requests.get(url='https://discordapp.com', verify=True)
    print('Connection to Discord OK.')
except requests.exceptions.SSLError as err:
    print('SSL Error. Adding custom certs to Certifi store...')
    cafile = certifi.where()
    with open('ssl764977.cloudflaressl.com.pem', 'rb') as infile:
        customca = infile.read()
    with open(cafile, 'ab') as outfile:
        outfile.write(customca)
    print('That might have worked.')