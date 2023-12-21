from datetime import datetime
current_time = datetime.now()
print(current_time)
formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)