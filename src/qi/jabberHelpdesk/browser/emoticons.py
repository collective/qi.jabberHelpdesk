import re
emoticons = { ':)' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_smile.png" alt=":)" title="Smile" />'
            , ':(' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_sad.png" alt=":(" title="Sad" />'
            , '8-)' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_cool.png" alt="8)" title="Cool" />'
            , ':D' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_lol.png" alt=":D" title="Big grin" />'
            , ':|' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_skeptic.png" alt=":|" title="Skeptic" />'
            , ':o' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_surprised.png" alt=":o" title="Surprised" />'
            , ':P' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_tongue.png" alt=":P" title="Tongue-in-cheek" />'
            , ';)' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_wink.png" alt=";)" title="Wink" />'
            , ':-)' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_smile.png" alt=":)" title="Smile" />'
            , ':-(' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_sad.png" alt=":(" title="Sad" />'
            , ':-D' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_lol.png" alt=":D" title="Big grin" />'
            , ':-|' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_skeptic.png" alt=":|" title="Skeptic" />'
            , ':-o' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_surprised.png" alt=":o" title="Surprised" />'
            , ':-P' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_tongue.png" alt=":P" title="Tongue-in-cheek" />'
            , ';-)' : '<img src="++resource++qi.jabberHelpdesk.smileys/smiley_wink.png" alt=";)" title="Wink" />'
            }
regex = re.compile("(%s)(?!\")" % "|".join(map(re.escape, emoticons.keys())))

def replaceEmoticons(text):
    """
    """
    return regex.sub(lambda mo, d=emoticons: d[mo.string[mo.start():mo.end()]], text)
    
    
    
    