import pandas as pd
import requests
from threading import Thread


class Getter(Thread):

    res = []
    THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'

    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())


threads = []
num_of_genres = 30
for i in range(num_of_genres):
    thread = Getter()
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
df = pd.DataFrame(Getter.res, columns=['Genre'])

file_name = "pandas.txt"
file = open(file_name, mode='w', encoding='utf8')
file.close()
df = df.to_csv('Pandas.txt')

with open(file_name, mode="r", encoding='utf8') as f:
    text = f.read()
    print(text)
