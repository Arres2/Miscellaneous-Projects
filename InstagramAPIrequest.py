import requests
import json

#pass post_id as string
# def request_post(post_id):
#     r = requests.get(f'https://graph.facebook.com/v9.0/instagram_oembed?url=https://www.instagram.com/p/{post_id}/&access_token=470646267675701|37405ab4946901e5131acf579a035927')
#     if r.status_code == 200:
#         post_html = r.json().get("html")
#         return print(post_html)
#     else:
#         return print(r.status_code)

# request_post("CLetrcBHbif")

# def get_posts():
#     r = requests.get("https://graph.instagram.com/me?fields=id,username&access_token=470646267675701|37405ab4946901e5131acf579a035927")
#     if r.status_code == 200:
#         post_html = r.json()
#         return print(post_html)
#     else:
#         return print(r.status_code)
    
# get_posts()

def getCreds():
    creds = dict()
    creds['access_token']= 
    creds['client_id'] = 
    creds['client_secret'] = 
    creds['graph_domain'] = 'https://graph.instagram.com/'
    creds['graph_version'] = 'v9.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version']
    creds['debug'] = 'no'

    return creds

def makeApiCall(url, endpointParams, debug= 'no'):
    data = requests.get(url, endpointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams,indent=4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

    if ('yes' == debug):
        displayApiCallData(response)

    return response

def displayApiCallData(response):
    print ("\nURL: ")
    print (response['url'])
    print ("\nEndopoint Params: ")
    print (response['endpoint_params_pretty'])
    print ("\nResponse: ")
    print (response['json_params_pretty'])