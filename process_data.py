from common import *

def get_county(location):
    """
    Creates a hashtag for a COUNTY
    rtype: #str
    """
    
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&components=country:US&key={google_maps_api_key}'
    response = requests.get(url).json()

    if response['status'] == 'OK':
        # Get the first result
        result = response['results'][0]

        # Find the county in the address components
        for component in result['address_components']:
            if 'administrative_area_level_2' in component['types']:
                county_raw = component['long_name'].lower()
                county = county_raw.replace(' ', '')
                return f'#{county}'

    return None

def get_city(location):
    """
    Creates a hashtag for a CITY
    rtype: #str
    """
    
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&components=country:US&key={google_maps_api_key}'
    response = requests.get(url).json()

    if response['status'] == 'OK':
        # Get the first result
        result = response['results'][0]

        # Find the city in the address components
        for component in result['address_components']:
            if 'locality' in component['types']:
                city_raw = component['long_name'].lower()
                city = city_raw.replace(' ', '')
                return f'#{city}'

    return None

def get_top_10_hashtags(list):
    """
    Gets the top 10 hashtags with their uses from a list
    rtype: list - [(hashtag, uses), (hashtag, uses)]
    """
    
    sorted_list = sorted(list, key=lambda x: x[1], reverse=True)
    top_10_hashtags = [(hashtag[0], hashtag[1]) for hashtag in sorted_list[:10]]
    
    return top_10_hashtags

def get_industry_list(industry):  
    """
    Gets the top 10 hashtags for an INDUSTRY
    rtype: list - [(hashtag, uses), (hashtag, uses)]
    """

    with open('data/hashtags.json', encoding='utf-8') as f:
        hashtags_json = json.load(f)
    
    industry_data = hashtags_json.get(industry, {})
    industry_list = [[hashtag, uses] for hashtag, uses in industry_data.items()]
    industry_list = get_top_10_hashtags(industry_list)

    return industry_list

def get_business_name_hashtag(business_name):
    """
    Creates a hashtag for a BUSINESS NAME
    rtype: #str
    
    """

    business_name = business_name.lower().replace(' ', '').replace("'", '').replace('#', '')
    hashtag = '#{}'.format(business_name)

    return hashtag

def process_caption(caption):
    """
    Gets the top 10 hashtags for an INDUSTRY for each word in a CAPTION
    rtype: list - [(hashtag, uses), (hashtag, uses)]
    Note: There will be a lot of hashtags
    """

    with open('data/keywords.json', encoding='utf-8') as f:
        keywords_json = json.load(f)

    caption_list = caption.lower()
    caption_list = caption_list.replace("'", "").replace('"', '').replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    caption_list = caption_list.split()
    hashtag_list = []

    for word in caption_list:
        for industry, value in keywords_json.items():
            if word in value:
                industry_list = get_industry_list(industry)
                hashtag_list.extend(industry_list)
                break
            else:
                continue

    return hashtag_list
        
def process_data(location, industry, business_name, caption):
    industry_list = get_industry_list(industry)
    business_name_hashtag = get_business_name_hashtag(business_name)
    location_hashtags = [get_city(location), get_county(location)]
    caption_hashtags = process_caption(caption)

    all_hashtags = []
    all_hashtags.extend(industry_list)
    all_hashtags.extend(caption_hashtags)

    # Removing duplicate hashtags
    all_hashtags = list(set(all_hashtags))

    # Getting top 7 hashtags
    sorted_hashtags = sorted(all_hashtags, key=lambda x: x[1], reverse=True)
    top_hashtags = [hashtag[0] for hashtag in sorted_hashtags[:7]]

    # Adding County, City, and Business name hashtags.
    top_hashtags.append(business_name_hashtag)
    top_hashtags.extend(location_hashtags)

    return top_hashtags
    
