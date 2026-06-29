day = input("Enter the day: ").strip().upper()
attendees = int(input("Enter the attendees: "))

def classify_success_of_party(day, attendees):
    weekdays = ['MON', 'TUE', 'WED', 'THU']
    weekends = ['FRI', 'SAT', 'SUN']

    if day not in weekdays and day not in weekends:
        return "Invalid day"

    if day in weekdays:
        if 700 <= attendees <= 1000:
            return "Successful"
        else:
            return "Unsuccessful"

    if day in weekends:
        if attendees >= 1500:
            return "Successful"
        else:
            return "Unsuccessful"

print(classify_success_of_party(day, attendees)) 