from func import *
from requests.exceptions import MissingSchema
from keep_alive import keep_alive
import anvil.server, os

anvil.server.connect(os.getenv('ID'))

@anvil.server.callable
def send(link, msg:str, author:str=None, avatar:str=None):
    if ',' in link:
            link = link.replace('\n', '').replace(' ', '').split(',')
    hook = Hook(link)
    global clr
    try:
        hook.send_msg(msg, username=author, avatar_url=avatar)
        return True
    except MissingSchema:
        return False

keep_alive()
anvil.server.wait_forever()