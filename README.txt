qi.jabberHelpdesk
=================

Overview
--------

qi.jabberHelpdesk is a real-time helpdesk product for plone. With it you can create helpdesks as content objects. Clients access the helpdesks through the web, whereas helpdesk agents connect to the helpdesk server using their jabber accounts. A helpdesk can be linked to many jabber accounts and whenever a client asks for support, one is chosen randomly among the available agents. qi.jabberHelpdesk also supports:

 - file transfers
 - url links and email addresses
 - smileys

In order to run qi.jabberHelpdesk to your own site you need either:

 - A free account on the `chatblox.com <http://chatblox.com/>`_ site in which case you don't need your own server, or 
 - To run a helpdesk server (You will need three modules qi.xmpp.botfarm, qi.xmpp.client, qi.xmpp.admin all found on pypi). Please read their documentation for installation details.

Installation
------------

Installing with buildout
------------------------
        
If you are using `buildout <http://pypi.python.org/pypi/zc.buildout/>`_ to manage your instance installing qi.jabberHelpdesk is very simple, just add qi.jabberHelpdesk in the *eggs* section and register it in the *zcml* sections. 


Installing without buildout
---------------------------

If you don't use buildout put it in INSTANCE/lib/python and add a file named qi.jabberHelpdesk-configure.zcml in INSTANCE/etc/package-includes with the following line::

    <include package="qi.jabberHelpdesk" file="configure.zcml" />

Usage
=====
Follow the following steps in order to create a helpdesk in your site:
 - Add a helpdesk. If you don't use the helpdesk of your chatblox.com account you'll need to create a bot on your own jabber server that the helpdesk will use.
 - Add the jabber ids of the agents to the helpdesk.
 - The owners of the jabber ids should accept the bot as a contact.
 - You are ready to go!
