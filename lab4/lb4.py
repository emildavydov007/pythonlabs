import requests
import time

# ДЕКОРАТОР (ограничение частоты вызовов)

def rate_limiter(delay_seconds):
    def decorator(func):
        last_call_time = 0

        def wrapper(*args, **kwargs):
            nonlocal last_call_time
            current_time = time.time()

            if current_time - last_call_time < delay_seconds:
                return f"Ошибка: слишком частые вызовы. Подождите {round(delay_seconds - (current_time - last_call_time), 2)} сек."

            last_call_time = current_time
            return func(*args, **kwargs)

        return wrapper
    return decorator

# ЗАМЫКАНИЕ (работа с API)
def create_api_function(url):
    def get_data():
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                # для dogapi
                if "data" in data and len(data["data"]) > 0:
                    return data["data"][0]["attributes"]["body"]

                return data

            return f"Ошибка запроса: {response.status_code}"

        except Exception as e:
            return f"Исключение: {e}"

    return get_data



# СОЗДАНИЕ ФУНКЦИИ + ДЕКОРИРОВАНИЕ

dog_api = create_api_function("https://dogapi.dog/api/v2/facts")

# применяем декоратор
dog_api = rate_limiter(3)(dog_api)





if __name__ == "__main__":
    print("Первый вызов:")
    print(dog_api())

    time.sleep(3)

    print("\nВторой вызов:")
    print(dog_api())
