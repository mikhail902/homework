def get_mask_card_number(card: str) -> str:
    """Функция скрытия карты"""
    mask_card = ""
    for i in range(len(card)):
        if card[i].isdigit():
            mask_card = card[:i] + card[i : i + 4] + 8 * "*" + card[-4:]
            break
    return mask_card


def get_mask_account(mask_account_card: str) -> str:
    """Функция номера аккаунта"""

    return 2 * "*" + mask_account_card[-4:]
