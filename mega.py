import requests
import urllib3
import sys
import argparse
import re
urllib3.disable_warnings()#Disable ssl warnings
def has_numbers(inputString): #to check if string contains numbers
     return any(char.isdigit() for char in inputString)
def mega_valid(id,type):
    if type == 'folder':
    
        data = { "a": "f", "c": 1, "r": 1, "ca": 1 }
    else:
        data = { "a": "g", "p": id }
    
    
    url = 'https://g.api.mega.co.nz/cs?id=5644474&n='+id
    req0 = requests.post(url, json=data)
    #print(req0.text)
    #validation
    if has_numbers(req0.text) and int(req0.text) < 0:
        print('not valid')
        print('='*17)
        return 1
    else:
        print('valid')
        print('='*17)
        return 0
def patternMatch(url):
    pattern_mega = r'.*mega.nz\/(file|folder)\/([\s\S]*)#(([\s\S])*)'
    pattern_mega2 = r'.*mega.nz\/#F!(.*)!'
    pattern_mega3 = r'.*mega.nz\/#!(.*)!'
    patternList = [pattern_mega, pattern_mega2, pattern_mega3]

    for pattern in patternList:
        matched = re.match(pattern, url)

        if matched:
            if len(matched.groups()) > 1:
                    linkType = matched.group(1)
                    linkId = matched.group(2)

                    print(linkType)
                    print(linkId)
                    return 'not valid' if mega_valid(linkId,linkType) == 1 else 'valid'
                    #return 0
            else:        
                    linkId = matched.group(1)
                    print(linkId)
                    return 'not valid' if mega_valid(linkId,0) == 1 else 'valid'
                    #return 0

    print('not a mega link')
    return 'not a mega link'  

parser = argparse.ArgumentParser(description='Validate MEGA links')
parser.add_argument('-u','--url', help='to test one url')
parser.add_argument('-i','--input', help='input file with links')
parser.add_argument('-o','--output', help='output file, default "./output.txt"')
args = parser.parse_args()
print("""


███╗░░░███╗███████╗░██████╗░░█████╗░
████╗░████║██╔════╝██╔════╝░██╔══██╗
██╔████╔██║█████╗░░██║░░██╗░███████║
██║╚██╔╝██║██╔══╝░░██║░░╚██╗██╔══██║
██║░╚═╝░██║███████╗╚██████╔╝██║░░██║
╚═╝░░░░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝

Credits: Titoot
hope you like it!

for help:
    mega.py --help
""")

if args.url:
    
    f2 = open('output.txt', 'a')
    f2.write(args.url + ' | ' + validation(args.url))
if args.input:
    try:
        f1 = open(args.input,'r')

        if args.output:
            f2 = open(args.output, 'a')
        else:
            f2 = open('output.txt', 'a')

        for i in f1:   
            f2.write(i[:-1] + ' | ' + patternMatch(i) + '\n')
            #patternMatch(i)
    except FileNotFoundError:
        print('Error: File not found')
    