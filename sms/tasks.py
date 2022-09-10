from asyncio.log import logger
from .helper import SendSMS
from celery import shared_task


@shared_task()
def send_sms_to_user(phone_number=998971122202):
    '''
        Task vazisi userga sms xabar yuborish
    '''
    configuration = SendSMS() # classdan uzgarmas oldik

    code = configuration.generate_one_time_sms() # 4talik code generate qilish

    result = configuration.send_sms(
        phone_number,
        code,
    ) #sms send qilish uchun class methodini chaqirdik!
    return True
