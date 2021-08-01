import os
import requests
def notify(title, subtitle, message):
    #send notification
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))





url="https://api.quotable.io/random"
r = requests.get(url=url)
data = r.json()
# print(data['author'])
# print(data['content'])

notify("Peverishhh",0,data['content']+data['author'])