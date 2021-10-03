import requests
import data_entry as DE
import xml.etree.ElementTree as ET

base_url = 'https://www.parlament.gv.at/PAKT/RGES/filter.psp?view=RSS&jsMode=&xdocumentUri=&filterJq=&view=&GP=XXVII&RGES=ALLE&SUCH=&listeId=103&FBEZ=FP_003'

data_list = []


def parse_xml(xml):
    root = ET.fromstring(xml)
    for child in root[0]:
        if child.tag == 'item':
            new_entry = DE.DataEntry()
            # title of the proposal
            new_entry.title = child[0].text.strip()
            # date of the proposal
            new_entry.pub_date = child[1].text.strip()
            # URL to the governmental website
            new_entry.link = child[2].text.strip()
            info = child[4].text.strip()
            string_to_search = 'Beschlossen im Nationalrat , Dafür:'
            string_found = info.partition(string_to_search)[2][:24]
            new_entry.info = string_found.strip()
            new_entry.process_info()
            data_list.append(new_entry)


def get_response():
    try:
        request = requests.get(base_url, headers={'User-agent': 'yourbot'})
        string_xml = request.content

    except:
        print("Something went wrong! Check your URL")
        string_xml = ''

    return string_xml


def party_agrees(party):
    score = 0
    for entry in data_list:
        if not entry.info:
            continue
        if party not in entry.disagreeing_parties:
            print("-------------------------------------------------------------------------------------------------------")
            entry.print_entry()
            score +=1
    print(f'{party} agreed with {score} proposals!')


def party_disagrees(party):
    score = 0
    for entry in data_list:
        if not entry.info:
            continue
        if party in entry.disagreeing_parties:
            print("-------------------------------------------------------------------------------------------------------")
            entry.print_entry()
            score += 1
    print(f'{party} disagreed with {score} proposals!')


if __name__ == '__main__':
    text = get_response()
    parse_xml(text)
    for entry in data_list:
        if entry.info:
            #print("-------------------------------------------------------------------------------------------------------")
            #entry.print_entry()
            #entry.print_disagreeing_parties()
            party_disagrees('F')
