from vk_api import VkApi
from VkLongPollWorker import work

vk_session = VkApi(token='your group key')

work(vk_session)
