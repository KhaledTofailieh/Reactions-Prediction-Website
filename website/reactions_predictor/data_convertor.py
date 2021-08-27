import pandas as pd
from .models import Page
import time

PAGES_PATH = r'C:\Users\Khaled\Desktop\Django\project2_website\website\assets\data\pages.csv'


def convert_pages_to_sql(path):
    df = pd.read_csv(path)
    rests = []
    for i in range(len(df)):
        print(i)
        rests.append(Page(
            name=df.loc[i]['page_name'],
            email=''
        ))
    Page.objects.bulk_create(rests)
    time.sleep(5000)
    Page.save()



# convert_pages_to_sql(PAGES_PATH)

