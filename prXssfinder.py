import requests
import re
import threading
import urllib3

# SUPPRESS WARNINGS ############################################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
list_urls = open("finder-xss-params.txt","r")

def send_requests():

    for line in list_urls:
        r_line = line.replace("\n", "")
        # print(r_line)
        try:
            req = requests.get(r_line,headers=headers_agent,timeout=1,allow_redirects=True,verify=False)
            # print(req)
            # print(req.status_code)
            # p = '/asdf("|<)/g'
            result = re.findall('asg64k"1|asg64k<1', req.text)
            print(r_line)
            print(result)
            # print(req.text)
        except Exception as error:
            print(error)
            continue
    list_urls.close()


processThread = threading.Thread(target=send_requests)
processThread.start()
