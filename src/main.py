from typing import Union


def get_mask_card_number(card: Union[str, int]) -> str:
    """Функция скрытия карты"""

    for i in range(len(card)):
        if card[i].isdigit():
            mask_card = card[:i] + card[i:i + 4] + 8 * '*' + card[-4:]
            break
    return mask_card


def get_mask_account(number_card: Union[str, int]) -> str:
    """Функция номера послезних цифр карты"""
    mask_account = 2 * '*' + number_card[12] + number_card[13] + number_card[14] + number_card[15]
    return mask_account
