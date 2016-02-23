f = open("Desktop/Birthday.csv", 'r+')
a = f.read().split('\n')
del a[-1]
f.close()
o = open("cal.ics", "w+")
print>>o, "BEGIN:VCALENDAR\n\
PRODID:-//Google Inc//Google Calendar 70.9054//EN\n\
VERSION:2.0\n\
CALSCALE:GREGORIAN\n\
METHOD:PUBLISH\n\
X-WR-CALNAME:Birthday\n\
X-WR-TIMEZONE:Asia/Calcutta\n"
for i in a:
  b = i.split(',')[1].split('/')
  c = "%4d"%int(b[2])+ "%02d"%int(b[0])+"%02d"%int(b[1])
  print>>o, "BEGIN:VEVENT\n\
DTSTART;VALUE=DATE:%s\n\
DTEND;VALUE=DATE:%s\n\
DTSTAMP:20160220T093252Z\n\
X-GOOGLE-CALENDAR-CONTENT-DISPLAY:chip\n\
X-GOOGLE-CALENDAR-CONTENT-ICON:https://calendar.google.com/googlecalendar/images/cake.gif\n\
RRULE:FREQ=YEARLY\n\
SUMMARY: %s\'s Birthday\n\
BEGIN:VALARM\n\
TRIGGER:-PT120M\n\
ACTION: DISPLAY\n\
DESCRIPTION: %s\'s Birthday Reminder\n\
End: VALARM\n\
END:VEVENT"%(c,int(c)+1, i.split(',')[0], i.split(',')[0])
print>>o, "END:VCALENDAR"
o.close()

