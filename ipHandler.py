
# this file will handle getting the ip location using ipinfo
import ipinfo
from requests import get
import config


access_token = config.access_token
handler = ipinfo.getHandler(access_token)
ip_address = get('https://api.ipify.org').content.decode('utf8')
# print('ip: {0}'.format(ip_address))
details = handler.getDetails(ip_address)

def get_location():
    location = details.loc
    return location

def get_city():
    return details.city



