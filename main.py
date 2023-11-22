user_input = int(input("Please enter number of seconds (from 0 to 8640000): "))
def format_time(seconds):
    if 0 <= seconds < 8640000:
        days, remainder = divmod(seconds, 24 * 60 * 60)
        hours, remainder = divmod(remainder, 60 * 60)
        minutes, seconds = divmod(remainder, 60)

        days_word = "day" if days == 1 else "days"
        hours_str = str(hours).zfill(2)
        minutes_str = str(minutes).zfill(2)
        seconds_str = str(seconds).zfill(2)

        formatted_time = f"{days} {days_word}, {hours_str}:{minutes_str}:{seconds_str}"
        return formatted_time
    else:
        return "Invalid value. Enter a number between 0 and 8639999"

result_time = format_time(user_input)
print(result_time)
