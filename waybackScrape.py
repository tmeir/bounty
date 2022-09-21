import requests
import sys
from datetime import datetime, timedelta


try:

    print("-----------------------------------------------------------------")
    print('''
    host <site> ---- for single host search.\n
    list ---- for list file search\n
    custom <listname> ---- for custom list\n
    domain <name> ---- for full domain search\n
    domain_list <domain list> ---- for list of domains
    ''')
    print("-----------------------------------------------------------------")

    yesterday = datetime.now() - timedelta(2)
    auto_date = datetime.strftime(yesterday,'%Y%m%d')
    r_namefile = sys.argv[2]
    name_file = r_namefile[:-4]
    def single_host():
        host_input = sys.argv[2]
        date_input = auto_date
        wayback_url = f"https://web.archive.org/cdx/search?url={host_input}/&matchType=host&collapse=urlkey&output=text&fl=original&limit=100000&from={date_input}"

        req = requests.get(wayback_url)
        # print(req.text)
        with open(f"{name_file}-{date_input}-raw.txt", "w") as file:
            file.write(req.text)

    def list_hosts():
        # print("1")
        hosts_list = open("list-hosts.txt","r")
        for line in hosts_list:
            r_line = line.replace("\n","")
            wayback_url = f"https://web.archive.org/cdx/search?url={r_line}/&matchType=host&collapse=urlkey&output=text&fl=original&limit=10000&from={auto_date}"
            print(wayback_url[39:-80])
            try:
                req = requests.get(wayback_url)
                with open(f"list-{auto_date}-{sys.argv[2]}-raw.txt","a") as file:
                    file.write(req.text)
            except Exception as c:
                print(c)
                continue
        hosts_list.close()

    def custom_list():
        list_custom = open(sys.argv[2],"r")
        for line in list_custom:
            r_line = line.replace("\n","")
            wayback_url = f"https://web.archive.org/cdx/search?url={r_line}/&matchType=host&collapse=urlkey&output=text&fl=original&limit=100&from={auto_date}"
            print(wayback_url[39:-80])
            try:
                req = requests.get(wayback_url)
                with open(f"{name_file}-{auto_date}-raw.txt","a") as file:
                    file.write(req.text)
            except Exception as c:
                print(c)
                continue
        list_custom.close()

    def auto_domain():
        domain_name = sys.argv[2]
        wayback_url = f"https://web.archive.org/cdx/search?url={domain_name}/&matchType=domain&collapse=urlkey&output=text&fl=original&limit=100&from={auto_date}"
        req = requests.get(wayback_url)
        with open(f"{domain_name}-{auto_date}-raw.txt","a") as file:
            file.write(req.text)

    def domain_list():
        list_domain = open(sys.argv[2],"r")
        for line in list_domain:
            r_line = line.replace("\n","")
            wayback_url = f"https://web.archive.org/cdx/search?url={r_line}/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*ico&limit=1000000&from={auto_date}"
            print(wayback_url[20:-1])
            try:
                req = requests.get(wayback_url)
                with open(f"{name_file}-{auto_date}-raw.txt","a") as file:
                    file.write(req.text)
            except Exception as c:
                print(c)
                continue
        list_domain.close()



    if sys.argv[1] == "host":
        single_host()
    elif sys.argv[1] == "list":
        list_hosts()
    elif sys.argv[1] == "custom":
        custom_list()
    elif sys.argv[1] == "domain":
        auto_domain()
    elif sys.argv[1] == "domain_list":
        domain_list()
    else:
        print("Must choose an option ")

except Exception as error:
    print(error)



