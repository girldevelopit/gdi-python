phone_number = '1-800-867-5309'

# Split the phone number string at each hyphen
phone_number_parts = phone_number.split('-')
# Should store ['1', '800', '867', '5309']

# Join the parts using a period
period_version = '.'.join(phone_number_parts)
# Should store '1.800.867.5309'

# Join the parts using a space
space_version = ' '.join(phone_number_parts)
# Should store '1 800 867 5309'

