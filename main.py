from datetime import datetime, timedelta


users = [
    {"name": "Marly", "birthday": "23-03-2001"},
    {"name": "Rob", "birthday": "20-06-1982"},
    {"name": "Tony", "birthday": "10-06-1993"},
    {"name": "Jerry", "birthday": "15-06-1974"},
    {"name": "Tom", "birthday": "26-06-1975"},
    {"name": "Teylor", "birthday": "24-06-2005"},
    {"name": "Djohny", "birthday": "24-06-1984"},
    {"name": "Lusy", "birthday": "04-07-1999"},
    {"name": "Lary", "birthday": "25-06-1989"},
    {"name": "Tomas", "birthday": "06-02-1987"}
]


def get_birthdays_per_week(users):
    
    data = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
    }
    
    date_now = datetime.now()
    
    for i in users:
        birthday = datetime.strptime(i.get("birthday"), '%d-%m-%Y')
        other_birthday = birthday.replace(year=date_now.year)
        d = other_birthday.date() - birthday.date()
        years = str(d.days//365)
        diff = other_birthday.date() - date_now.date()
        
        if timedelta(0) <= diff <= timedelta(7):
            days = datetime.weekday(other_birthday)
            if days == 0 or days == 5 or days == 6:
                data['Monday'] = data['Monday'] + \
                    i['name'] + ' ' + years + ' ' + 'years old'
                data['Monday'] = data['Monday'] + ', '
            if other_birthday.weekday() == 1:
                data['Tuesday'] = data['Tuesday'] + \
                    i['name'] + ' ' + years + ' ' + 'years old'
                data['Tuesday'] = data['Tuesday'] + ', '
            if other_birthday.weekday() == 2:
                data['Wednesday'] = data['Wednesday'] + \
                    i['name'] + ' ' + years + ' ' + 'years old'
                data['Wednesday'] = data['Wednesday'] + ', '
            if other_birthday.weekday() == 3:
                data['Thursday'] = data['Thursday'] + \
                    i['name'] + ' ' + years + ' ' + 'years old'
                data['Thursday'] = data['Thursday'] + ', '
            if other_birthday.weekday() == 4:
                data['Friday'] = data['Friday'] + \
                    i['name'] + ' ' + years + ' ' + 'years old'
                data['Friday'] = data['Friday'] + ', '

    for k, v in data.items():
        if len(v) != 0:
            print(f'{k}: {v[:-2]}')



if __name__ == '__main__':
    get_birthdays_per_week(users)




# days_name = {
#     0: "Monday",
#     1: "Tuesday",
#     2: "Wednesday",
#     3: "Thursday",
#     4: "Friday",
#     5: "Saturday",
#     6: "Sunday"
# }


# def get_birthdays(users: list):

#     birth_in_year = {}
#     start_period = ((datetime.now() - timedelta(days=datetime.now().weekday()) + timedelta(days=5))).date()
#     end_period = start_period + timedelta(days=6)

#     for info in users:
#         birth = info.get("birthday")
#         name = info.get("name")

#         birthday = datetime.strptime(birth, "%Y-%m-%d").date()
#         year_now_date = birthday.replace(start_period.year)

#         if start_period <= year_now_date <= end_period:
#             day_of_week = days_name.get(year_now_date.weekday())
#             if year_now_date.weekday() in (5, 6):
#                 if birth_in_year.get("Monday"):
#                     birth_in_year["Monday"].append(name)
#                 else:
#                     birth_in_year["Monday"] = [name]
#             else:
#                 if birth_in_year.get(day_of_week):
#                     birth_in_year[day_of_week].append(name)
#                 else:
#                     birth_in_year[day_of_week] = [name]
#     birthdays = ""

#     for day_of_week, name in birth_in_year.items():
#         birthdays += f'{day_of_week}: {", ".join(name)} \n'

#     return birthdays


# if __name__ == "__main__":
#     print(get_birthdays(users))
