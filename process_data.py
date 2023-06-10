from common import *

def get_all_industries():
    """
    Gets a list of all industries from data/keywords.json
    rtype: list
    """
    with open('data/keywords.json', encoding='utf-8') as f:
        keywords_json = json.load(f)

    industries = list(keywords_json.keys())

    return industries

def get_county(location):
    """
    Creates a hashtag for a COUNTY
    rtype: #str | None
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
    rtype: #str | None
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

    # if not industry:
        # return None
        # Industry is required in the form.

    with open('data/hashtags.json', encoding='utf-8') as f:
        hashtags_json = json.load(f)
    
    industry_data = hashtags_json.get(industry, {})
    industry_list = [[hashtag, uses] for hashtag, uses in industry_data.items()]
    industry_list = get_top_10_hashtags(industry_list)

    return industry_list

def get_business_name_hashtag(business_name):
    """
    Creates a hashtag for a BUSINESS NAME
    rtype: #str | None
    """

    if not business_name:
        return None

    business_name = business_name.lower().replace(' ', '').replace("'", '').replace('#', '')
    hashtag = '#{}'.format(business_name) if business_name else None

    return hashtag

def process_caption(caption):
    """
    Gets the top 10 hashtags for an INDUSTRY for each word in a CAPTION
    rtype: list - [(hashtag, uses), (hashtag, uses)] | None
    Note: There will be a lot of hashtags
    """
    # Now supports multi-word hashtags!

    if not caption:
        return None
    
    hashtag_list = []

    caption_list = caption.lower()
    caption_list = caption_list.replace("'", "").replace('"', '').replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    caption_list = caption_list.split()

    keyword_processor = KeywordProcessor()
    
    with open('data/keywords.json', encoding='utf-8') as f:
        keywords_json = json.load(f)

    keyword_processor.add_keywords_from_dict(keywords_json)
    # {'clean_name': ['list of unclean names']}

    industries = keyword_processor.extract_keywords(caption)
    # ['industryA', 'industryB', etc.]

    if not industries:
        return None

    for industry in industries:
        industry_list = get_industry_list(industry)
        hashtag_list.extend(industry_list)

    return hashtag_list
 
           
def process_data(location, industry, business_name, caption):
    """
    Processes all of the inputted data. Returns a list of top 10 hashtags.
    rtype: list
    """

    # Getting all hashtags from all functions. 'None' instances are handled later.
    industry_list = get_industry_list(industry)
    business_name_hashtag = get_business_name_hashtag(business_name)
    city_hashtag = get_city(location)
    county_hashtag = get_county(location)
    caption_hashtags = process_caption(caption)

    all_hashtags = []
    
    # if industry_list: - Industry is required in the form.
    all_hashtags.extend(industry_list)
    
    if caption_hashtags:
        all_hashtags.extend(caption_hashtags)

    # Removing duplicate hashtags.
    all_hashtags = list(set(all_hashtags))

    # Getting top 7 hashtags.
    sorted_hashtags = sorted(all_hashtags, key=lambda x: x[1], reverse=True)
    top_hashtags = [hashtag[0] for hashtag in sorted_hashtags[:8]]

    # Adding County, City, and Business name hashtags.
    if business_name_hashtag and business_name_hashtag not in top_hashtags:
        top_hashtags.pop(-1)
        top_hashtags.append(business_name_hashtag)
    
    if county_hashtag:
        top_hashtags.append(county_hashtag)

    if city_hashtag:
        top_hashtags.append(city_hashtag)

    return top_hashtags
    
