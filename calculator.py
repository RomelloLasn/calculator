import datetime

start_times = []
end_times = []

num_days = int(input('kirjuta, mitu päeva sa töötasid:'))

for i in range(num_days):
    start_time_str = input(f"Enter the start time for day {i + 1} (HH:MM): ")
    end_time_str = input(f"Enter the end time for day {i + 1} (HH:MM): ")

    start_time = datetime.datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.datetime.strptime(end_time_str, "%H:%M")

    start_times.append(start_time)
    end_times.append(end_time)

total_hours = datetime.timedelta()

for start_time, end_time in zip(start_times, end_times):
    duration = end_time - start_time
    total_hours += duration


print(f"tunde kokku: {total_hours}")
