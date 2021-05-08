import json
import os

"""
code
    name:
    slug:
    type:
    name with type: 
    code:
    parent code: 
    child: []

"276": {
    "name": "Thạch Thất",
    "type": "huyen",
    "slug": "thach-that",
    "name_with_type": "Huyện Thạch Thất",
    "path": "Thạch Thất, Hà Nội",
    "path_with_type": "Huyện Thạch Thất, Thành phố Hà Nội",
    "code": "276",
    "parent_code": "01"
}
"""

dataset = {}

def load_data(filename):
    f = open(filename,'r')
    data = json.load(f)
    return data

# tinh thanh pho, quan huyen
tinh_tp = load_data('dist/tinh_tp.json')
dataset = tinh_tp
for code in tinh_tp:
    dataset[code]['child'] = []

# quan, huyen, thanh pho
quan_huyen_tpnho = load_data('dist/quan_huyen.json')
for code in quan_huyen_tpnho:
    parent_code = quan_huyen_tpnho[code]['parent_code']
    dataset[parent_code]['child'].append(quan_huyen_tpnho[code])
    dataset[parent_code]['child'][-1]['child'] = []

    PREFIX_DIR = 'dist/xa-phuong/' 
    list_files = os.listdir(PREFIX_DIR)
    for filename in list_files:
        fullfilename = PREFIX_DIR + filename
        try:
            xa_phuong = load_data(fullfilename)
            for childcode in xa_phuong:
                parent_childcode = xa_phuong[childcode]['parent_code']
                if parent_childcode == code:
                    dataset[parent_code]['child'][-1]['child'].append(xa_phuong[childcode])
                # print(xa_phuong[code])
        except Exception:
            print("Khong ton tai {}".format(filename))
            # break


# # thi tran, thi xa, phuong, xa
# PREFIX_DIR = 'dist/xa-phuong/' 
# list_files = os.listdir(PREFIX_DIR)
# for filename in list_files:
#     fullfilename = PREFIX_DIR + filename
#     try:
#         xa_phuong = load_data(fullfilename)
#         for code in xa_phuong:
#             parent_code = xa_phuong[code]['parent_code']
                
                
#             # print(xa_phuong[code])
#     except Exception:
#         print("Khong ton tai {}".format(filename))
#         # break

with open('dataset.json', 'w') as outfile:
    json.dump(dataset, outfile)