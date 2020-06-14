import os
import xmltodict
import collections


files = os.listdir()

for file in files:
    if file.endswith('.xml'):
        text = open(file, 'r', encoding='cp1251')
        xml = text.read()
        text.close()
        parsedxml = xmltodict.parse(xml)
        for ShortCut in parsedxml['ShortCuts']['ShortCut']:
            if isinstance(ShortCut, collections.OrderedDict) and ShortCut['@Action'] == 'Create':
                print(file[10:13], ShortCut['@Name'], ShortCut['TargetPath'], sep='\t')

# print(files)
