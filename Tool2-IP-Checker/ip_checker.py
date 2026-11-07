import requests
import csv
from datetime import datetime
key = "Your_API_Key"
headers = {"x-apikey": key}
ip = input("IP dalo:")
url = f"https://virustotal.com/api/v3/ip_addresses/{ip}"
try:
    r = requests.get(url,headers=headers)
    data = r.json()
    if "error" in data:
        print(f"Error : {data['error']['message']}")
    else:
        stats = data['data']['attributes']['last_analysis_stats']
        malicious = stats['malicious']
        harmless = stats['harmless']
        owner = data['data']['attributes'].get('as_owner','unknown')
        if malicious==0:
            result = "Safe"
        elif malicious >=1 and malicious <5:
            result = "Suspicious"
        else:
            result = "Malicious"
        print("\n---REPORT---")
        print(f"IP :{ip} | Owner :{owner} | Result :{result}")
        # CSV me save karna
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("ip_report.csv","a",newline="") as f:
            writer = csv.writer(f)
            if f.tell()==0:
                writer.writerow(["Date","IP","Owner","Malicious","Harmless","Result"])
            writer.writerow([time,ip,owner,malicious,harmless,result])
            print(f"\n Report save ho gye: ip_report.csv")
except Exception as e:
    print(f"Masla ho gya: {e}")

        