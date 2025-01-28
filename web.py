import requests
import json
import time

import ollama
from getweb import search
prompt="你可以联网，如果你需要查阅网页，请输出网址"
messages=[{"role":"system","content":prompt}]
content=open("content.txt","r").read()
messages.append( {"role":"user","content":content})
messages.append( {"role":"user","content":search(content)})
#print(messages)

while 1:
    stream = ollama.chat(model='deepseek-r1:1.5b', messages=messages,stream=True)
    response=""
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        response+=chunk['message']['content']
    messages.append({"role":"robot","cotent":response})    