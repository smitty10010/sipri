"""
sipri.api
~~~~~~~~~~~~
A simple way to hit Stockholm International Peace Research Institute's (SIPRI) trade register API and return a CSV file.
:copyright: (c) 2021 by Robert S.
:license: MIT License, see LICENSE for more details.
:SIPRI Terms and Conditions: see https://www.sipri.org/about/terms-and-conditions
Usage:
      >>> import sipri
      >>> data = sipri.sipri_data()
      >>> data
      str
"""
from .api import sipri_data