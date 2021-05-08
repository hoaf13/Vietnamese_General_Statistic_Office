import json 
import random 
import string 
import itertools

f = open('dataset1.json', 'r')
data = json.load(f)

data_dict = dict()
res = dict()

def generate(province_dict, district_dict, ward_dict):
    try:
        ans = dict()
        ward = ward_dict['name']
        district = district_dict['name']
        province = province_dict['name']

        text = str(ward)  + ' '  + str(district) + ' '  + str(province) 
        text = " ".join(text.split())
        res[text] = dict()
        res[text]['ward'] = None
        res[text]['district'] = None
        res[text]['province'] = None
        
        if ward != None:    
            
        if district != None:
            pass
        if province != None:
            pass
            
    
        return text
        
    except:
        print("Exception",ward, district, province)
        print()
        print()
        print()

f = open('dataset_gen2.txt','w')

for province_code in data:
    province_data = data[province_code]['child']
    province_dict = {
        'name': data[province_code]['name'],
        'type': data[province_code]['type'],
        'name_with_type': data[province_code]['name_with_type']
    }
    for district in province_data:
        district_data = district['child']
        district_dict = {
            'name': district['name'],
            'type': district['type'],
            'name_with_type': district['name_with_type']
        }
        for ward in district_data:
            ward_dict = {
                'name': ward['name'],
                'type': ward['type'],
                'name_with_type': ward['name_with_type']
            }        
             
            # print(province_dict)
            # print(district_dict)
            # print(ward_dict)
            res = generate(province_dict, district_dict, ward_dict)
            print(res)
            f.writelines('- ' + str(res) + '\n')

# print(data_dict)

