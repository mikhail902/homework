def filter_by_state(dicts: list, state="EXECUTED") -> list:
    """Функция, которая отбирает принятые операции"""

    new_dicts = []
    for i in dicts:
        if i["state"] == state:
            new_dicts.append(i)
    return new_dicts


def sort_by_date(date_list: list, method_of_sort=False) -> list:
    """Функция сортировки по дате"""

    sorted_date = sorted(date_list, key=lambda data: data["date"], reverse=method_of_sort)
    return sorted_date


d = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
sort_by_date(d, False)

f = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
filter_by_state(f, "EXECUTED")
