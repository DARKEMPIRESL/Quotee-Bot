from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to search quotes on different topics and great people any time you want. To know how to use me press 'How to Use' below.

By @ImDark_Empire
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π Search a Quote π", switch_inline_query_current_chat="")],
        [InlineKeyboardButton(text="ποΈ Return Home ποΈ", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("π Search a Quote π", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton("How to Use β", callback_data="help"),
            InlineKeyboardButton("βΎοΈ About βΎοΈ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://t.me/SLBotOfficial/28")],
        [InlineKeyboardButton("π¬ Support Group π¬", url="https://t.me/trtechguide")],
    ]

    # Help Message
    HELP = """
**π Inline Mode π**
 
**1) Search Quotes**
Just pass the topic/name on which you wanna search quotes.
Example : `@dark_Quotee_Bot Albert Einstein`

**2) Quote of the Day**
To get 'Quote of the Day' pass `#q` or `#qod`. You will get that for 5 different topics.
Example : `@dark_Quotee_Bot #qod`

**3) Random Quote**
To get a single random quote pass `#r` or `#random`.
Example : `@dark_Quotee_Bot #random`

**4) A Single Quote**
By default, when you will use 1st option, you will get 20-30 quotes. But if you want only 1 random quote of that topic, use `#1` in end.
Example : `@dark_Quotee_Bot Sushant Singh Rajput #1`

More features in development. Keep track by joining @SLBotOfficial.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @SLBotOfficial which provides quotes from brainyquotes.com using Python.

Source Code : [Click Here](https://github.com/DARKEMPIRESL/dark_Quotee_Bot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @ImDark_Empire
    """