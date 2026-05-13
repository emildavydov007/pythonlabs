def get_multiplier(room_type):
    if room_type == "Комната":
        return 1.0
    elif room_type == "Квартира":
        return 1.2
    elif room_type == "Дом":
        return 1.5
    return 1.0