from typing import Union


def mask_account_card(card: Union[str, int]) -> str:
    """Функция скрытия карты"""

    for i in range(len(card)):
        if card[i].isdigit():
            mask_account_card = card[:i] + " " + 2 * "*" + card[-4:]
            break
    return mask_account_card


def get_date(date: Union[str, int]) -> str:
    """Функция преобразованияя даты"""

    arrayse_date = date[:10]
    result_date = arrayse_date.replace("-", ".")
    return result_date
