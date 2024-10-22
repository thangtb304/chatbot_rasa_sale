import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def search_info_product(name_product):
    with open('../raw_data/Product.json','r',encoding='utf-8') as f:
        content=json.load(f)

        for x in content:
            if x['name_product'].lower()==name_product.lower():
                return x


# h=search_info_product('Fitness Tracker XYZ')
# print(h)