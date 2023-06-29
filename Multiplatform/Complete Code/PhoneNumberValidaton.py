## Credit to Haider Imtiaz

# Fetch Phone Numbers
# pip install phonenumbers
import phonenumbers as ph
from phonenumbers import carrier, geocoder
# Parse Number
number =  ph.parse("+4407723090454")
print(number.country_code)
print(number.national_number)
# Get Carrier 
info = carrier.name_for_number(number, "en")
print(info)
# Get Region/Country
info = geocoder.description_for_number(number, "en")
print(info)
# Validate a Phone number
validation = ph.is_valid_number(number)
print(validation)