#!/usr/bin/env python
# coding: utf-8

# In[75]:


import itertools
import subprocess
import requests

start="""curl -i -s -k -X $'POST' \
    -x 'http://127.0.0.1:8080' \
   -H $'Host: puzzler7.imaginaryctf.org:9004' -H $'Content-Length: 133' -H $'Accept: application/json' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' -H $'Content-Type: application/json' -H $'Origin: http://puzzler7.imaginaryctf.org:9004' -H $'Referer: http://puzzler7.imaginaryctf.org:9004/' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' -H $'Connection: close' \
   -b $'_y=d309c8f2-8717-44D8-D9EC-3EAA0EF02E48; _shopify_y=d309c8f2-8717-44D8-D9EC-3EAA0EF02E48; epb_previous_pathname=/; _s=d6d54883-B1A6-4C89-1F67-4F5AA9B74FBD; _shopify_s=d6d54883-B1A6-4C89-1F67-4F5AA9B74FBD; _shopify_sa_t=2023-01-22T00%3A16%3A07.939Z; _shopify_sa_p=' \
   --data-binary $'{\"page_id\":\"61216424102\",\"article_id\":\"\",\"product_id\":\"\",\"collection_ids\":\"\",\"version\":\"2\",\"password\":\""""
   
key = 'yellowgreenblueorangepinkred'
   
end= """\"}' \
   $'http://puzzler7.imaginaryctf.org:9004/apps/password-protect/authenticate' """ 

prime = 'pink'
colors = ['yellow', 'green', 'blue', 'orange', 'red']
combo = [p for p in itertools.permutations(colors)]
#req = requests.get('')
for data in combo:
    #print("Number of permutations {}".format(len(combo)))
    data = (prime + "".join(map(str, data)))
    #print(data)
    #print(start + str(data) + end)
    cmdstr = (start + str(data) + end)
    subprocess.run(["bash", "-c", cmdstr], stdout=True)
    print()
    print("#"*100)


# In[ ]:




