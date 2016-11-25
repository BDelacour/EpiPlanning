from getpass import getpass
import requests
import json

class EpiPlanning:
    def __init__(self):
        form_data = {
            'login': raw_input("Enter your login : "),
            'password': getpass("Enter your password : ")
        }
        self.session = requests.session()
        self.session.post('https://intra.epitech.eu/', form_data)

    def get_planning(self, outfile='planning.json', date_from='1999-08-29', date_to='2099-08-28'):
        url = 'https://intra.epitech.eu/planning/load?format=json&start=%s&end=%s' % (date_from, date_to)
        print 'Retrieving data from %s to %s on Epitech\'s intranet' % (date_from, date_to)
        response = self.session.get(url)
        jsonresponse = json.loads(response.text)
        num = 0
        data = []
        for activity in jsonresponse:
            if activity[u'module_registered'] is True:
                name = activity[u'acti_title']
                date = activity[u'start']
                room = None
                if activity[u'room'] and activity[u'room'].has_key(u'code'):
                    room = activity[u'room'][u'code']
                appointment = None
                if activity[u'rdv_group_registered']:
                    appointment = activity[u'rdv_group_registered']
                elif activity[u'rdv_indiv_registered']:
                    appointment = activity[u'rdv_indiv_registered']
                module = activity[u'titlemodule']
                registered = activity[u'event_registered'] is not False
                num += 1
                item = {
                    'Name': name,
                    'Activity_date': date,
                    'Appointment_date': appointment,
                    'Room': room,
                    'Module': module,
                    'Registered': registered
                }
                data.append(item)
        with open(outfile, 'w') as fd:
            json.dump(data, fd)
        print 'Wrote %d activites to %s.' % (num, outfile)

if __name__ == '__main__':
    planner = EpiPlanning()
    try:
        planner.get_planning()
    except KeyboardInterrupt:
        exit('Interrupted by keyboard')
