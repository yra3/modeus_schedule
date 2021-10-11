import requests
from datetime import datetime
from icalendar import Calendar, Event, vDatetime
from auth_info import auth_info


def auth_with_csrf_token():
    s = requests.Session()
    login_url = r"https://fs.utmn.ru/adfs/ls?SAMLRequest=lZJBT8MwDIXv%2FIoq9zVpNgZEa9E0hIQEEhqDAxdkUhcqNUmJ07GfT9ox0QMgkHJK%2FJ79PmdxvjNNskVPtbM5y1LBErTalbV9ydn95nJyys6LowWBaVq17MKrXeNbhxSSJRH6EGUrZ6kz6O%2FQb2uN9%2BvrnL2G0JLiHKIiNa7EjlLnX7h2xjjb37LkIrrUFsLQ%2BSCoKO2CsanvOJQV8YZYcum8xqF3zipoCFlydZGzp0pPp6WYi2x2NtNCZlrOT%2BRzdjyt9CkIMY1ldAtE9Ra%2FhEQdXlkKYEPOZFRNMhHPJpur2VwJmQpx%2FMiShwMS2SOJkCypAULOOm%2BVA6pJWTBIKmh1t7y5VrFStd4Fp13Dik9kQz%2F%2FdwM4UGXFTwx7F8kNBighAKeW98QmsXW54OOu%2Bxlkqz5XhuUAMe4r4C4kK2da8DX1KXEHOoxzyv8FVWPnVRNTrLEa2f059K9lWuneOl73a313vryNY6COyTYeLLXOhz2Cb%2Bcp9m8%2FASkO9MbfvPgA&RelayState=f3bc7858-d3e5-43d9-bb05-0c2689d7f1c2&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=ZtCSLSa9aMphFpoZmDvlgy6ISI9yWczRbL8XmXlsn1AbTaofDOYtVuiWeG9t7w%2B2dxOfJwV5U%2BrJsaSjrADzcOcwz0SBgM1m%2BBKQ%2BkeElQ82lNkJ5QoVsNyrePGU4CO8WU6PX26tUOQk163DhagOxfhkbWBibVmH09nEqswDy6McSsQliNl8u2YqXmA4Dwj%2Fp%2FkMr3x1ZGi5b%2FChA0NFVF%2FdZxcjH4hok59NDzttj3h6blTqJ0i2jKLBn3aAYII3VmNrvHU7RakjGMD7IgIN6sw3QrDIGrcIMQ09dpAxZn7eMzLCEw28zA5Y4ogHlbIaDUMZv7Zgi76zzwh4HEuPDA%3D%3D"
    url = 'https://utmn.modeus.org/'
    r = s.get(login_url)
    csrf_token = r.cookies['csrftoken']

    data = {
        'login': '',
        'password': '',
        'csrfmiddlewaretoken': csrf_token
    }

    d = s.post(login_url, data=data, headers=dict(Referer=login_url))
    dd = s.get(url)
    print(d.status_code)
    print(dd.text)


def request_schedule():
    # modeus_auth = tuple(auth_info.values())
    url = r"https://fs.utmn.ru/adfs/ls?SAMLRequest=lZJBT8MwDIXv%2FIoq9zVpNgZEa9E0hIQEEhqDAxdkUhcqNUmJ07GfT9ox0QMgkHJK%2FJ79PmdxvjNNskVPtbM5y1LBErTalbV9ydn95nJyys6LowWBaVq17MKrXeNbhxSSJRH6EGUrZ6kz6O%2FQb2uN9%2BvrnL2G0JLiHKIiNa7EjlLnX7h2xjjb37LkIrrUFsLQ%2BSCoKO2CsanvOJQV8YZYcum8xqF3zipoCFlydZGzp0pPp6WYi2x2NtNCZlrOT%2BRzdjyt9CkIMY1ldAtE9Ra%2FhEQdXlkKYEPOZFRNMhHPJpur2VwJmQpx%2FMiShwMS2SOJkCypAULOOm%2BVA6pJWTBIKmh1t7y5VrFStd4Fp13Dik9kQz%2F%2FdwM4UGXFTwx7F8kNBighAKeW98QmsXW54OOu%2Bxlkqz5XhuUAMe4r4C4kK2da8DX1KXEHOoxzyv8FVWPnVRNTrLEa2f059K9lWuneOl73a313vryNY6COyTYeLLXOhz2Cb%2Bcp9m8%2FASkO9MbfvPgA&RelayState=f3bc7858-d3e5-43d9-bb05-0c2689d7f1c2&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=ZtCSLSa9aMphFpoZmDvlgy6ISI9yWczRbL8XmXlsn1AbTaofDOYtVuiWeG9t7w%2B2dxOfJwV5U%2BrJsaSjrADzcOcwz0SBgM1m%2BBKQ%2BkeElQ82lNkJ5QoVsNyrePGU4CO8WU6PX26tUOQk163DhagOxfhkbWBibVmH09nEqswDy6McSsQliNl8u2YqXmA4Dwj%2Fp%2FkMr3x1ZGi5b%2FChA0NFVF%2FdZxcjH4hok59NDzttj3h6blTqJ0i2jKLBn3aAYII3VmNrvHU7RakjGMD7IgIN6sw3QrDIGrcIMQ09dpAxZn7eMzLCEw28zA5Y4ogHlbIaDUMZv7Zgi76zzwh4HEuPDA%3D%3D"
    # url = r"https://utmn.modeus.org/schedule-calendar"
    # r = requests.get(url, auth=modeus_auth)

    with requests.Session() as s:
        auth_url = url
        headers = {
            'Login': auth_info['Login'],
            'Password': auth_info['Password'],
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': 'https://utmn.modeus.org/',
            'X-Requested-With': 'XMLHttpRequest',
        }
        r = s.post(auth_url, headers)
        print(r.status_code)
        r = s.get('https://utmn.modeus.org/')
        print(r.text)


def display(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()


def open_ics_file():
    schedule_filename = '11-17:10:2021.ics'  # TODO: add find filename method
    with open(schedule_filename, 'r', encoding='utf-8') as f:
        row_text = f.read()
        cleared_text = row_text.replace(u'\ufeff', '')  # erase unicode "Byte Order Mark"
    return cleared_text


def get_list_from_file(filename: str):
    with open(f'./{filename}', 'r', encoding='utf-8') as f:
        online_list = [row.strip() for row in f.readlines()]
    return online_list


def main():
    calendar_text = open_ics_file()
    week_calendar = Calendar.from_ical(calendar_text)
    online_subjects = get_list_from_file('online_pairs.txt')
    ignored_subjects = get_list_from_file('ignored_pairs.txt')
    calendar_dates = {}
    week_calendar.subcomponents = [x for x in week_calendar.subcomponents
                                   if x['CATEGORIES'][1].cats[0] not in ignored_subjects]
    for ev in week_calendar.subcomponents:
        # subject = ev['CATEGORIES'][1].cats[0]
        # pair_type = ev['CATEGORIES'][0].cats[0]
        event_datetime = ev['DTSTART'].dt
        # print(subject)
        # print(pair_type)
        # print(event_datetime)
        event_date = event_datetime.date()
        event_time = event_datetime.time()
        if event_date in calendar_dates:
            if event_time < calendar_dates[event_date]:
                calendar_dates[event_date] = event_time

    print(week_calendar.subcomponents)


if __name__ == "__main__":
    main()