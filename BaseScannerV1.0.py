import requests
from colorama import Fore
from colorama import Style
from bs4 import BeautifulSoup

print(F'''{Fore.GREEN}
  ____                    _____                                 
 |  _ \                  / ____|                                
 | |_) | __ _ ___  ___  | (___   ___ __ _ _ __  _ __   ___ _ __ 
 |  _ < / _` / __|/ _ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |_) | (_| \__ \  __/  ____) | (_| (_| | | | | | | |  __/ |   
 |____/ \__,_|___/\___| |_____/ \___\__,_|_| |_|_| |_|\___|_|      

 Build by: XSPHERE AND CYB3R4C3                                                                                                                                                                                                                                                                                                                                                                    
{Style.RESET_ALL}''')

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My kera jasto Agent 99999.99',
        'From': 'lado@pornhub.com'
    }
)

i = 1
while i > 0:
    url = input("Enter the url: ").lower()
    if not ((('http://') == (url[:7])) or (("https://") == (url[:8]))):
        print("Please add full url including http or https")
        print("Check if the url is correct")
        i = 1
    else:
        i = -1
        print("URL acceptable")


def check_version_feed(urlx):
    '''This function checks the version of
    the wordpress site'''

    print("Checking version......")
    if ((urlx[-1]) == "/"):
        urly = "feed"
    else:
        urly = "/feed"
    urlformated = urlx + urly
    response = requests.get(urlformated, headers=headers)
    if response.status_code == 200:
        ver_soup = BeautifulSoup(response.content, 'html.parser')
        ver_fin = ver_soup.generator.string
        print(f'{Fore.GREEN}Wordpress version Detected: {Style.RESET_ALL}' + ver_fin[-5:])

        rss = requests.get(urlformated)
        if 'Response' in rss:
            print('rss not founnd')
        else:
            print(f'{Fore.GREEN}Rss Feed Found: {Style.RESET_ALL}' + urlformated)
    else:
        print(f'{Fore.RED}Not valid Wordpress site : {Style.RESET_ALL}' + urlformated)


def adminpan(urlx):
    '''This function checks if a site
    have admin panel or not'''

    if ((urlx[-1]) == "/"):
        urly = "wp-admin"
    else:
        urly = "/wp-admin"
    urlformated = urlx + urly
    cp = requests.head(urlformated)
    fetch = cp.status_code
    if cp.status_code == 301:
        print(f'{Fore.RED}Admin Panel not found most probably it has been moved to different path {Style.RESET_ALL}')
    else:
        print(f'{Fore.GREEN}Admin Panel Found : {Style.RESET_ALL}' + urlformated)


def xmrpc_check(urlx):
    '''This function checks if a site is
    vulnerable to bruteforce attack or not'''

    if ((urlx[-1]) == "/"):
        urly = "xmlrpc.php"
    else:
        urly = "/xmlrpc.php"
    urlformated = urlx + urly
    xmrpc = requests.head(urlformated)
    if xmrpc.status_code == 409:
        print(f'{Fore.RED}XMLRPC found: {Style.RESET_ALL}', 'Site maybe vulnerable to brute attack')
    else:
        print("XMLRPC not found")


def userfinder(urlx):
    '''This function just extracts a json
    data and find users from the data'''

    if ((urlx[-1]) == "/"):
        urly = "wp-json/wp/v2/users"
    else:
        urly = "/wp-json/wp/v2/users"
    url = urlx + urly

    print("Finding users.....")
    r = requests.get(url, headers=headers)
    if str(r.status_code) == "200":
        JsonAll = r.json()
        print(f'{Fore.GREEN}Users found\n--------------------- {Style.RESET_ALL}')
        for i in range(0, len(JsonAll)):
            j = i + 1
            print(str(j), ". ", JsonAll[i]['name'])
    else:
        print(f'{Fore.RED}Fuck!!! We got a error {Style.RESET_ALL}')
        print(f'{Fore.RED}Status Code: {Style.RESET_ALL}', r.status_code)


check_version_feed(url)
adminpan(url)
xmrpc_check(url)
userfinder(url)

# https://english.onlinekhabar.com
