import phonenumbers
from phonenumbers import geocoder
number= input() # +91 7558407284
ch_no = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_no,"en"))
from phonenumbers import carrier
service_no=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(ch_no,"en"))