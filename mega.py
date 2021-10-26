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
    print(req0.text)
    #validation
    if has_numbers(req0.text) and int(req0.text) < 0:
        print('not valid')
        print('='*17)
        return 1
    else:
        print('valid')
        print('='*17)
        return 0
def validation(url):        
    noindx = url.find('/#F!')

    m = re.match(pattern_mega, url)
    if noindx and not m:
 
        	
        m1 = re.match(pattern_mega2, url)
        if m1:
   
            id = m1[3]
            type = m1[2]
            print(id)
            print(type)
            if mega_valid(id,type) == 1:
           
                return 'not valid'
            else:
 
                return 'valid'
    if m:
        id = m[3]
        type = m[2]

        print(id)
        print(type)
        if mega_valid(id,type) == 1:

                return 'not valid'
        else:
  
                return 'valid'
        
        
    if not m:
       
                print("not a mega link") 
                return 'not a mega link'    

pattern_mega = re.compile('(https|http):\/\/mega.nz\/(file|folder)\/([\s\S]*)#(([\s\S])*)')	
pattern_mega2 = re.compile('(https|http):\/\/mega.nz\/(#F!)(.*)!.*')

parser = argparse.ArgumentParser(description='Validate MEGA links')
parser.add_argument('-u','--url', help='to test one url')
parser.add_argument('-i','--input', help='input file with links')
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
""")
#print("starting...")

if args.url:
    
    f2 = open('output.txt', 'a')
    f2.write(args.url + ' | ' + validation(args.url))
if args.input:
    try:
        f1 = open(args.input,'r')
        for i in f1:
 
            f2 = open('output.txt', 'a')
            f2.write(i[:-1] + ' | ' + validation(i) + '\n')
    except FileNotFoundError as e:
        print('Error: File not found')
    