from __init__ import get_mask_account, get_mask_card_number
from widget import get_date

# inputting
number_card = input()
date = input()

# write
print(get_mask_card_number(number_card))
print(get_mask_account(number_card))
print(get_date(date))
