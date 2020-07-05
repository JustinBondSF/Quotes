import re
from random import randint

import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

i = randint(0, 25)
url = "http://brainyquote.com/topics/"
topic = "coding"
num = 1
page = '-' + "quotes" + "_" + str(num)
r = requests.get(url + topic + page)
right_click_menu = ['&Menu', [
                    '&Next',
                    '&Previous',
                    '&Topic',
                    'E&xit', ]]

soup = BeautifulSoup(r.content, "html.parser")

quotesraw = soup.find_all('a', attrs={"class": "b-qt"})
quotes = [quotes.text for quotes in quotesraw]
quote = quotes[i]

authorsraw = soup.find_all('a', attrs={"class": "bq-aut"})
authors = [authors.text for authors in authorsraw]
author = authors[i]


# CurrentQuote = {quotes[i].strip: authors[i].strip}
# print(CurrentQuote)
sg.theme('Dark Purple 6')  # please make your windows colorful


layout = [
    [sg.Text(quotes[i],
             key='quote',
             justification='left',
             font=('Times New Roman', [22], 'italic'),
             pad=(5, 10),
             size=(60, 4),

             )
     ],
    [sg.Text(authors[i],
             key='author',
             justification='right',
             font=('Helvetica', [16], 'bold italic'),
             pad=[(0, 5), (5, 0)],
             size=(80, 2),

             )
     ],
    [sg.Button('Previous'), sg.Button('Next'), sg.Button('Exit')],
]

window = sg.Window("", layout,
                   auto_size_buttons=False,
                   no_titlebar=True,
                   grab_anywhere=True,
                   keep_on_top=True,
                   alpha_channel=.75,
                   right_click_menu=right_click_menu
                   )

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        break
    # try to change the "author" and "quote" element to the appropriate indices, except go to the *next* page(even if we ran out of *Previous* indices), index 0, if the index is out of range
    if event == 'Previous':
        try:
            i -= 1

            quote = quotes[i]
            author = authors[i]

            window['quote'].update(quote)
            window['author'].update(author)

            window.refresh

        except IndexError:
            i = 0
            num += 1

            quote = quotes[i]
            author = authors[i]

            window['quote'].update(quote)
            window['author'].update(author)

            window.refresh

    elif event == 'Next':
        try:
            i += 1

            quote = quotes[i]
            author = authors[i]

            window['quote'].update(quote)
            window['author'].update(author)

            window.refresh

        except IndexError:
            i = 0
            num += 1

            quote = quotes[i]
            author = authors[i]

            window['quote'].update(quote)
            window['author'].update(author)

            window.refresh
window.close()
del window
