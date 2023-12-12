from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

import datetime
import pytz

from mailings.models import Mailing, LogMailing
from mailings.services import send_mail

tz = 'Europe/Moscow'
utc = pytz.UTC

def my_background_task(obj_id):
    obj = Mailing.objects.get(id=obj_id)
    logs = LogMailing.objects.get(id=obj_id)
    try:
        cur_time = datetime.datetime.now().replace(tzinfo=utc)

        if cur_time >= obj.start.replace(tzinfo=utc) and cur_time <= obj.stop.replace(tzinfo=utc):
            obj.status = 'active'

            obj.save()

            send_mail(_to_mail=obj.owner.email,
                      _message=obj.message_body,
                      _subject=obj.message_title)


        elif cur_time > obj.stop.replace(tzinfo=utc):
            obj.status = 'finish'
            obj.save()
        else:
            obj.status = 'ready'
            obj.save()


        logs.response = '200'
        logs.date_try = cur_time
        logs.status_try = 'ok'
        logs.save()



    except Exception as ex:
        print(ex)

        logs.date_try = cur_time
        logs.status_try = 'bad'
        logs.response = '400'
        logs.save()



def schedule_mailings():
    scheduler = BackgroundScheduler()
    objects = Mailing.objects.all()


    for obj in objects:
        job_id = f'j_{obj.id}'

        if obj.period == 'daily':
            trigger = CronTrigger(hour=obj.start.hour,
                                  minute=obj.start.minute,
                                  day="*")
        elif obj.periods == 'weekly':
            trigger = CronTrigger(hour=obj.start.hour,
                                  minute=obj.start.minute,
                                  day_of_week=obj.start.weekday())
        elif obj.periods == 'monthly':
            trigger = CronTrigger(hour=obj.start.hour,
                                  minute=obj.start.minute,
                                  day=obj.start.day)
        else:
            print(f"Invalid period {obj.period} for mailing with id {obj.id}")
            continue

        scheduler.add_job(my_background_task,
                          trigger=trigger,
                          args=[obj.id],
                          id=job_id)

    scheduler.start()




