from bs4 import BeautifulSoup as bs
import logging
import requests

# CONSTANTS

base_url = 'https://www.99acres.com/search/property/rent/residential-all/'
base_domain = 'https://www.99acres.com'
city_codes = {
    'Hyd' : '269'
}
### End of Constants

def match_class(target):                                                        
    def do_match(tag):                                                          
        classes = tag.get('class', [])                                          
        return all(c in classes for c in target)                                
    return do_match  


def search(params):
    
    city = params['city']
    locality = params['locality']
    
    base_args = {}

    # Static arguments
    base_args['search_type'] = 'QS'
    base_args['refSection'] = 'GNB'
    base_args['search_location'] = 'HP'
    base_args['strEntityMap'] = 'IiI%3D'
    base_args['refine_results'] = 'Y' 
    base_args['Refine_Localities'] = 'Refine%20Localities'
    base_args['action'] = '%2Fdo%2Fquicksearch%2Fsearch'
    base_args['lstAcn'] = 'HP_R'
    base_args['lstAcnId'] = '0' 
    base_args['src'] = 'CLUSTER'
    base_args['isvoicesearch'] = 'N' 

    base_args['preference'] = 'R' 
    base_args['selected_tab'] = '4'
    base_args['city'] = city_codes[city]
    base_args['res_com'] = 'R'
    base_args['property_type'] = 'R' 
    
    base_args['keyword'] = locality
    
    base_args['searchform']  = '1'
    base_args['price_min'] = 'null' 
    base_args['price_max'] = 'null'

    headers = {}
    headers['Host'] = 'www.99acres.com'
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'
    headers['Accept'] = 'text/css,*/*;q=0.1'
    headers['Accept-Language'] = 'en-US,en;q=0.5'
    headers['Accept-Encoding'] = 'gzip, deflate, br'
    headers['Connection'] = 'keep-alive'
    
    #The request
    web_resp = requests.get(base_url + locality, params = base_args, headers=headers)
    
    # Get complete DOM
    soup = bs(web_resp.text,'html.parser')
    # Search all the classes that contain results on the page
    res_list = soup.find_all(match_class(["pageComponent", "srpTuple__srpTupleBox", "srp"]))

    response = []
    for res in res_list:
        curr_rec = {}
        curr_rec['title'] = res.h2.text
        curr_rec['link'] = base_domain + res.a.get('href')
        response.append(curr_rec)
    
    #response['status'] = '201'
    return response

if __name__ == "__main__":
    param = {}
    param['locality'] = 'Nallagandla'
    param['city'] =  'Hyd'
    print(search(param))