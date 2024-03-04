# import datetime

# def get_days_except_sundays(year):
#     # Initialize an empty list to store the days
#     days_except_sundays = []

#     # Iterate through all the days in the given year
#     for month in range(1, 13):
#         for day in range(1, 32):
#             try:
#                 # Create a datetime object for the current day
#                 current_date = datetime.datetime(year, month, day)
                
#                 # Check if the day is not a Sunday (weekday 6)
#                 if current_date.weekday() != 6:
#                     days_except_sundays.append(current_date)
#             except ValueError:
#                 # Handle the case where the day is out of range for the month
#                 pass
    
#     return days_except_sundays

# # Define the year
# year = 2024

# # Get the list of days except Sundays in the given year
# days_list = get_days_except_sundays(year)

# # Print the list of days
# for day in days_list:
#     print(day.strftime("%Y-%m-%d"))
import datetime

def get_days_except_sundays(year):
    # Initialize an empty list to store the days
    days_except_sundays = []

    # Iterate through all the days in the given year
    for month in range(12, 0, -1):
        for day in range(1, 32):
            try:
                # Create a datetime object for the current day
                current_date = datetime.datetime(year, month, day)
                
                # Check if the day is not a Sunday (weekday 6)
                if current_date.weekday() != 6:
                    # Format the date as "Month Day, Year"
                    formatted_date = current_date.strftime("%B %d, %Y")
                    days_except_sundays.append(formatted_date)
            except ValueError:
                # Handle the case where the day is out of range for the month
                pass
    
    return days_except_sundays

# Define the year
year = 2024

# Get the list of days except Sundays in the given year
days_list = get_days_except_sundays(year)

# Print the list of days in descending order
for day in reversed(days_list):
    print(day)
