from widget import mask_account_card, get_date
from __init__ import get_mask_card_number, get_mask_account

# inputting
number_card = input()
date = input()

print(get_mask_card_number(number_card))
print(get_mask_account(number_card))
print(get_date(date))

