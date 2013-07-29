__author__ = 'peter'

from errbot import BotPlugin, botcmd, holder
import logging
from xmpp import Message, Node

class Spree(BotPlugin):
    min_err_version = '1.7.1'  # Optional, but recommended
    max_err_version = '1.7.1'  # Optional, but recommended

    def callback_connect(self):
        self.start_poller(5, self.chime, args={}, kwargs={})

    def chime(self):
        for jid in holder.bot.roster.getItems():
            self.bare_send(Message(to=jid, payload=[Node('monster',payload=['sullivan'])]))