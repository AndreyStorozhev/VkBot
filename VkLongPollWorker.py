from vk_api.longpoll import VkLongPoll, VkEventType
from Service import BotService

bot_service = BotService()


def work(vk_session):
    long_poll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text.lower() == "привет" or event.text == 'здорова' or event.text.lower() == 'хай':
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, random_id="", message='Я робот Джек, привет. \n'
                                                                                  'Знаю команды: (Пиши команду целиком) \n' +
                                                                                  '1. Скажи погоду \n' +
                                                                                  '2. Что посмотреть \n' +
                                                                                  '3. Расскажи о себе \n' +
                                                                                  '4. Хабр (скину умную ссылку с habr)')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, random_id="", message='Ого! как вас тут много! Я теряюсь')
            elif event.text.lower() == 'скажи погоду':
                vk.messages.send(user_id=event.user_id, random_id="",
                                 message='Погода в костроме: ' + bot_service.get_weather())
            elif event.text.lower() == 'что посмотреть':
                vk.messages.send(user_id=event.user_id, random_id="",
                                 message='Я пока не знаю много фильмов, но вот этот просто супер: ' + bot_service.get_movie())
            elif event.text.lower() == 'расскажи о себе':
                vk.messages.send(user_id=event.user_id, random_id="",
                                 message='Мой создатель https://vk.com/andreystorozhev , я написан на чистом Python 3.7.3')
            elif event.text.lower() == 'хабр':
                vk.messages.send(user_id=event.user_id, random_id="",
                                 message='Лови умную ссылку с хабра :) ' + bot_service.get_href_habr())
            else:
                vk.messages.send(user_id=event.user_id, random_id="",
                                 message='Не понимаю, я пока глупый( \n' + 'Начни просто с "привет"')
