"""
sipri.api
~~~~~~~~~~~~
A simple way to hit Stockholm International Peace Research Institute's (SIPRI) trade register API and return a CSV file.
:copyright: (c) 2021 by Robert S.
:license: MIT License, see LICENSE for more details.
:SIPRI Terms and Conditions: see https://www.sipri.org/about/terms-and-conditions
"""
import requests

def sipri_data(low_year='2020',high_year='2020',seller='',buyer='',armanent_category='any',buyers_or_sellers='',filetype='csv',include_open_deals='on',sum_deliveries='off'):
    r"""Sends a PUT request to SIPRI and returns the requested data.
    :param low_year:(optional) The start year (defaults to '2020').
    :param high_year:(optional) The end year (defaults to '2020').
    :param seller: (optional) The entity/country selling equipment (see readme for complete list of acceptable values).
    :param buyer: (optional) The entity/country buying equipment (see readme for complete list of acceptable values).
    :param armanent_category: (optional) The specific equipment category tracked by SIPRI (see readme for complete list of acceptable values).
    :param buyers_or_sellers: (optional) Sorts the data by sellers or buyers (this is important if you choose 'rtf' as a file type)
    :param filetype: (optional) accepted values are 'csv'(default value) or 'rtf'.
    :param include_open_deals: (optional) accepted values are 'on'(default value) or 'off'.
    :param sum_deliveries: (optional) accepted values are 'on' or 'off'(default value) this will sum all deliveries if 'on' is selected.
    :return: string of comma seperated data from SIPRI's database (if 'csv' selected as file type) or a string of a rtf response.
    Usage::
      >>> import sipri
      >>> data = sipri.sipri_data()
      >>> data
      <a string is returned>
    """
    params = {
        'low_year':low_year,
           'high_year':high_year,
           'seller_country_code':seller,
           'buyer_country_code':buyer,
           'armament_category_id':armanent_category,
           'buyers_or_sellers':buyers_or_sellers,
           'filetype':filetype,
           'include_open_deals':include_open_deals,
           'sum_deliveries':sum_deliveries,
           'Submit4':'Download'
    }

    return requests.post('https://armstrade.sipri.org/armstrade/html/export_trade_register.php', data=params).text