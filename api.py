import requests

def Main() :
#    nsx = input("Enter NSX-Manager IP -> ")
    nsx = '10.161.135.141'
    url = 'https://' + nsx + '/api/v1/upgrade/upgrade-units/aggregate-info'
    print("HOST UPGRADE UNITS : ")
    r = GetResponse(url)
 
def GetResponse(url):
    response = requests.get(url, auth=('admin', 'Admin!23Admin'), verify=False)
    if response.status_code != 200:
            print("-----ERROR----")
            exit()
    r = response.json()
    Page(r["results"])
    try:
        cursor = r["cursor"]
        next_page = url + '?cursor=' + cursor
        res = GetResponse(next_page)
    except:
        pass
        
def Page(llist):
    for result in llist :
        if result['type'] != 'HOST':
            continue
        print('\tTYPE: ' + result['type'] + '\tDisplay_Name: ' + result['display_name'] + '\tID: ' + result['id'])
        data = result['metadata']
        print('\t' + data[1]['key'] + ": " + data[1]['value'] + '\t' + data[2]['key'] +': ' + data[2]['value'] + '\t' + data[3]['key'] +': ' + data[3]['value'])
        print("\tGroup_Name: " + result['group']['display_name'] + "\tGroup_ID: " + result['group']['id'])
        print("\tUPGRADE_Status : " + result['status'] + "\tPercentage_Complete : " + str(result['percent_complete']) + "\n")

Main()
