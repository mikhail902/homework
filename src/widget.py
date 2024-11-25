from masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция ввода карты"""
    mask_card = get_mask_card_number(card)
    mask_account = get_mask_account(card)
    return f"{mask_card} \naccount: {mask_account}"


def get_date(date: str) -> str:
    """Функция преобразованияя даты"""
    final_date=''
    result_date = date.split("-")
    for i in range(3):
        final_date = result_date[:3]
    return ".".join(final_date)
