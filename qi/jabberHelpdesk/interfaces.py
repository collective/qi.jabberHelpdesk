# -*- coding: utf-8 -*-
import re
from zope.interface import Interface
from zope.interface import Attribute
from zope import schema
from qi.jabberHelpdesk import HelpdeskMessageFactory as _

email_constraint = re.compile("^[a-zA-Z][\w\.-]*[a-zA-Z0-9]@[a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]\.[a-zA-Z][a-zA-Z\.]*[a-zA-Z]$").match

class IHelpdesk(Interface):
    """
    Interface for helpdesk
    """
    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Name of the helpdesk"),
        required=True
    )
    
    description = schema.Text(
        title=_(u"Description"),
        description=_(u"A short summary of the helpdesk"),
        required=True
    )
    botJid = schema.ASCIILine(
        title=_(u"Bot's JID"),
        description=_(u"The Jabber ID of the bot assigned to this helpdesk"),
        constraint = email_constraint,
        required=True
    )
    botPassword = schema.Password(
        title=_(u"Bot's password"),
        description=_(u"The bot's password."),
        default=None,
        required=False)
    persistent = schema.Bool(
        title=_(u"Persistent bot"),
        description = _(u"Specifies whether the bot remains loaded " \
                         "even if nobody is using it"),
        default = False,
    )
class IHelpdeskAgents(Interface):
    """
    """
    agentJids = schema.List(
        title = _(u"Agents IDs"),
        description = _(u"The jabber IDs of auhorized agents, "\
                        "typically of the form userID@jabberserver"),
        value_type=schema.ASCIILine(
        title=_(u"Agent's jabber ID"),
        constraint=email_constraint)
    )

class IChatRequest(Interface):
    """Interface describing a chat request
    """
    name = schema.TextLine(title=_(u"Name"),
                           description=_(u"Your full name."),
                           required=True)
    
    subject = schema.Text(title=_(u"Subject"),
                          description=_(u"What you would like to discuss."),
                          required=False,
                          )

class IHelpdeskSettings(Interface):
    """
    Helpdesk xmlrpc server settings
    """
    
    xmlrpc_host = Attribute("Helpdesk XMLRPC server")
    xmlrpc_port = Attribute("Helpdesk XMLRPC server port ")

class IMessageHandler(Interface):
    """
    Message handler utility interface
    """
    
    def userLogin(botID,user,name,subject):
        """
        """
    def userLogout(botID,user):
        """
        """
    def sendUserMessage(botID,user,message):
        """
        """
    def getUserMessages(botID,user):
        """
        """
    def getAliveAgents(botID,passHash):
        """
        """
    def getAvailableAgents(botID,passHash):
        """
        """
    def getHelpdeskAgents(botID,passHash):
        """
        """
    def getAgentAvatarB64(botID):
        """
        """
    def getAgentVCard(botID,userID):
        """
        """
    def loadBot(botID,botPass,persistent):
        """
        """
    def addAgent(botID,botPass,passHash):
        """
        """
    def removeAgent(botID,botPass,passHash):
        """
        """