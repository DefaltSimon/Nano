__name__ = "DiscordieBot simple commands list"


'''
Adding commands:

Just add them with the help of a template:

"<yourtriggercommand>": "<whatYouWantToPrint>",
                                              ^ everywhere except the last line

The second can include <@{usr}> to mention the author.
Use \n anywhere for new line in the same message.
'''

things = {
    "!hello": "Hi, <@{usr}>",
    "!test": "<@{usr}> Ayy test works!",
    "!johncena": "<@{usr}> O_O https://www.youtube.com/watch?v=58mah_0Y8TU",
    "!allstar": "<@{usr}> https://www.youtube.com/watch?v=L_jWHffIx5E",
    "!game": "@everyone Does anyone want to play games?",
    "!ayy": "<@{usr}> Ayyyyy lmao!",
    "!moreayy": "<@{usr}> Ayyyyyyyyyy lmao! ( ͡° ͜ʖ ͡°) 👾 ",
    "!wot": "U wot <@{usr}>",
    "!synagoge": "DIE ALTEE-SYNAGOGE",
    "!thecakeisalie": "<@{usr}> : Rick roll'd https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "!who": "<@{usr}> Can't manipulate strings. Not yet. Soon."
    }
