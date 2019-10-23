from vk_api import VkApi
from VkLongPollWorker import work

vk_session = VkApi(token="911ed824c7f2923ac55f9b599af4ac3f1c525019a277415af74416931fa33003fa2aae60a5c7c10c15420")

work(vk_session)
