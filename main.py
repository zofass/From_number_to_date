user_input = int(input("Будь ласка, введіть число від 0 до 8640000: "))
def format_time(seconds):
    if 0 <= seconds < 8640000:
        days, remainder = divmod(seconds, 24 * 60 * 60)
        hours, remainder = divmod(remainder, 60 * 60)
        minutes, seconds = divmod(remainder, 60)

        days_word = "день" if days == 1 else "дні" if 2 <= days <= 4 else "днів"
        hours_str = str(hours).zfill(2)
        minutes_str = str(minutes).zfill(2)
        seconds_str = str(seconds).zfill(2)

        formatted_time = f"{days} {days_word}, {hours_str}:{minutes_str}:{seconds_str}"
        return formatted_time
    else:
        return "Невірне значення. Введіть числоу проміжку між 0 та 8639999"

result_time = format_time(user_input)
print(result_time)
