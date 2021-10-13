import collections
import os
from datetime import datetime, timedelta

from icalendar import Calendar


def read_ics_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        row_text = f.read()
        cleared_text = row_text.replace(u'\ufeff', '')  # erase unicode "Byte Order Mark"
    return cleared_text


def read_file_lines(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        online_list = [row.strip() for row in f.readlines()]
    return online_list


def is_equals_dates(d1, d2):
    return d1.day == d2.day and d2.month == d1.month and d1.year == d2.year


def display_sleep_and_fall_up_times():
    root_dir_name = os.path.dirname(__file__)
    schedule_dir = os.path.join(root_dir_name, "schedule_ics_files")
    # print(os.listdir(schedule_dir))
    schedule_filename = os.path.join(schedule_dir, os.listdir(schedule_dir)[0])
    calendar_text = read_ics_file(schedule_filename)  # TODO: add find filename method
    week_calendar = Calendar.from_ical(calendar_text)
    ignored_subjects_filename = os.path.join(root_dir_name, 'ignored_pairs.txt')
    ignored_subjects = read_file_lines(ignored_subjects_filename)
    calendar_dates = {}
    week_calendar.subcomponents = [x for x in week_calendar.subcomponents
                                   if x['CATEGORIES'][1].cats[0] not in ignored_subjects]
    for event in week_calendar.subcomponents:
        is_online = event['LOCATION'] == 'Microsoft Teams'
        event_datetime = event['DTSTART'].dt
        event_date = event_datetime.date()
        event_time = event_datetime
        if is_online:
            event_time += timedelta(hours=2)
        is_have_not_that_date = event_date not in calendar_dates
        is_it_best_time = is_have_not_that_date or event_time < calendar_dates[event_date]
        if is_it_best_time:
            calendar_dates[event_date] = event_time
    sorted_dates = collections.OrderedDict(sorted(calendar_dates.items()))
    today = datetime.now()
    for date, event_time in sorted_dates.items():
        wake_up_time = event_time - timedelta(hours=2)
        fall_asleep_time = wake_up_time - timedelta(hours=8)
        if today.day >= date.day and today.month >= date.month and today.month >= date.month:
            continue
        if is_equals_dates(today, date):
            if today.hour < fall_asleep_time.hour:
                print(fall_asleep_time.strftime('сегодня ложись в %H:%M'))
            if today.hour < wake_up_time.hour:
                print(date.strftime('сегодня вставай в ') + wake_up_time.strftime('%H:%M'))
        elif is_equals_dates(today + timedelta(days=1), date):
            print(fall_asleep_time.strftime('завтра ложись в %H:%M'))
            print(date.strftime('завтра вставай в ') + wake_up_time.strftime('%H:%M'))
        else:
            print(fall_asleep_time.strftime('%d ложись в %H:%M'))
            print(date.strftime('%d вставай в ') + wake_up_time.strftime('%H:%M'))


if __name__ == "__main__":
    display_sleep_and_fall_up_times()
