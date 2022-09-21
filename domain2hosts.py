import requests
from datetime import datetime

try:
    yesterday = datetime.now()
    auto_date = datetime.strftime(yesterday, '%Y%m%d')

    def domain_list():
        list_domain = open("rawDomains.txt" ,"r")
        for line in list_domain:
            r_line = line.replace("\n" ,"")
            wayback_url = f"https://web.archive.org/cdx/search?url={r_line}/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*ico&limit=1000000&from=2022"
            print(wayback_url)
            try:
                req = requests.get(wayback_url)
                with open(f"hostsList-{auto_date}-raw" ,"a") as file:
                    file.write(req.text)
            except Exception as c:
                print(c)
                continue
            wayback_url2 = f"https://web.archive.org/cdx/search?url={r_line}/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*txt&limit=1000000&from=2022"
            print(wayback_url2)
            try:
                req = requests.get(wayback_url2)
                with open(f"hostsList-{auto_date}-raw", "a") as file:
                    file.write(req.text)
            except Exception as c:
                print(c)
                continue
        list_domain.close()

    domain_list()
except Exception as error:
    print(error)
