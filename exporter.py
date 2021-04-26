import moment
import requests
import json
import time


def instruction_time_calculator(time):
    time = moment.date(str(time * 1000)).format("YYYYMMDDTHHmmss")
    return time


# If the certificate check fails, download a new cert chain from the website.
def fetch_calendar(userid, hash, start, end, id):
    url = f'https://selfservice.campus-dual.de/room/json?userid={userid}&hash={hash}&start={start}&end={end}&_={id}'
    try:
        data_stream = requests.get(url, verify='selfservice-campus-dual-cert-chain.pem')
    except:
        print('Request went wrong!')
        return 0
    content = json.loads(data_stream.content.decode())
    return content


def build_ics_file(data):
    uid = 0
    with open('ba-calendar.ics', 'w') as ics:
        ics.write(
            'BEGIN:VCALENDAR' + '\n' +
            'VERSION:2.0' + '\n' +
            'X-WR-CALNAME:' + 'BA-Kalender' + '\n' +
            'X-WR-RELCALID: BA-Export' + '\n'
        )
        for entry in data:
            ics.write(
                'BEGIN:VEVENT' + '\n' +
                'UID:' + str(uid) + '\n' +
                'ORGANIZER;CN=' + entry['instructor'] + '\n' +
                'SUMMARY:' + entry['title'] + entry['instructor'] + '\n' +
                'DTSTART:' + instruction_time_calculator(entry['start']) + '\n' +
                'DESCRIPTION:' + entry['instructor'] + ' - ' + entry['description'] + ' - ' + entry['remarks'] + '\n' +
                'DTEND:' + instruction_time_calculator(entry['end']) + '\n' +
                'LOCATION:' + entry['room'] + '\n' +
                'END:VEVENT' + '\n'
            )
            uid += 1
        ics.write('END:VCALENDAR')


if __name__ == '__main__':
    """
     Before you execute the script, enter your userid from Campus Dual and your Hash, that can be found within the 
     source of the website */
    """
    # Change these values.
    userid = 'userid'
    hashcode = 'hash'

    # Change these values only when desired.
    starttime = '0'
    stoptime = int(time.time())
    trailing_id = '0'

    content_data = fetch_calendar(userid, hashcode, starttime, stoptime, trailing_id)
    if content_data is not None:
        build_ics_file(content_data)
    else:
        print('Empty dataset.')
