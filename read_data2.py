import random
import os 
import re


PREFIX = 'address_crawl/'
filenames = os.listdir(PREFIX)
data = []

def normalize_text(line):
    line = line.lower()
    line = line.replace('tx', 'thị xã ')
    line = line.replace('tt', 'thị trấn ')
    line = line.replace('tp.', 'thành phố ')
    line = line.replace('tp', 'thành phố ')
    line = line.replace('tn', 'tòa nhà')
    line = line.replace('(', ' ')
    line = line.replace(')', ' ')
    return line

def normalize_word(word):
    word = word.lower()
    word = word.strip()
    word = word.replace(',', '')
    word = word.replace('-', ' ')

    
    word = " ".join(word.split())
    return word

for filename in filenames:
    f = open(PREFIX + filename,'r')
    tmp = [line for line in f]
    tmp = random.choices(tmp, k=2000)
    data.extend([line[:-1] for line in tmp])

f = open('dataset_gen4.txt','w')

for line in data:
    words = line.split(' - ')
    if len(words) == 4:
        line = normalize_text(line)
        words = line.split(' - ')
        content = "[" + words[0] + "]" + "(content)"
        ward = "[" + words[1] + "]" + "(ward)"
        district = "[" + words[2] + "]" + "(district)"
        text = normalize_word(content) + ' ' + normalize_word(ward) + ' ' + normalize_word(district) + ' ' + words[-1]
        text = '- ' + text + '\n'
        f.write(text)
    else:
        # words = line.split(',')
        words = re.split(',|-',line)
        words = [word.lower() for word in words]
        ward_index = None
        district_index = None
        province_index = None
        for index,word in enumerate(words):
            if "huyện" in word or "quận" in word or "thành phố" in word and index != len(words) - 1:
                ward_index = index - 1
                district_index = index
                province_index = index + 1
                content = normalize_word(' '.join(words[:ward_index]))
                ward = normalize_word(words[ward_index])
                district = normalize_word(words[district_index])
                province = normalize_word(words[province_index])
                
                if content != '':
                    content = "[" + content + "]" + "(content)"
                if ward != "":
                    ward = "[" + ward + "]" + "(ward)"
                if district != '':
                    district = "[" + district + "]" + "(district)"

                text = content + ' ' + ward + ' ' + district + ' ' + province
                text = '- ' + text.strip() + '\n'
                f.write(text)
f.close()