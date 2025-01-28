print("main.py开始执行")
import ollama
content=open("content.txt","r").read()

stream = ollama.chat(model='deepseek-r1:1.5b', messages=[
     {
     'role': 'user',
    'content': content,
  },
],stream=True
)
#import tqdm
#print(response['message']['content'])
for chunk in (stream):
    print(chunk['message']['content'], end='', flush=True)