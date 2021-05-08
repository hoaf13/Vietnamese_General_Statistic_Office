import os 

data = []

listfiles = os.listdir('address_crawl/')
for filename in listfiles:
    f = open('address_crawl/' + filename, 'r')
    data.extend([l[:-1] for l in f])

def normalize_text(line):
    line = line.lower()
    line = line.replace('tx', 'thị xã ')
    line = line.replace('tt', 'thị trấn ')
    line = line.replace('tp.', 'thành phố ')
    line = line.replace('tp', 'thành phố ')
    line = line.replace('tn', 'tòa nhà')
    return line

def normalize_word(word):
    word = word.lower()
    word = word.strip()
    word = word.replace(',', '')
    word = word.replace('-', ' ')
    word = " ".join(word.split())
    return word

f = open('dataset_gen3.txt','w')
index = 0
for line in data:
    words = line.split(' - ')
    if len(words) == 4:
        index +=1
        line = normalize_text(line)
        words = line.split(' - ')
        content = "[" + words[0] + "]" + "(content)"
        ward = "[" + words[1] + "]" + "(ward)"
        district = "[" + words[2] + "]" + "(district)"
        text = normalize_word(content) + ' ' + normalize_word(ward) + ' ' + normalize_word(district) + ' ' + words[-1]
        print(text)
        f.write('- ' + text + '\n')
f.close()