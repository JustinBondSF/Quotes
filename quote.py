import requests
from tkinter import *
from bs4 import BeautifulSoup
import PySimpleGUI as sg
from random import randint
# seed random number generator
i = randint(0, 25)
url = "http://brainyquote.com/topics/"
topic = "inspirational"
num = 1
page = '-' + "quotes" + "_" + str(num)
r = requests.get(url + topic + page)
menu_def = [
    '&Next',
    '&Previous',
    '&Topic',
    'E&xit', ]


soup = BeautifulSoup(r.content, "html.parser")

quotesraw = soup.find_all('a', attrs={"class": "b-qt"})
quotes = [quotes.text for quotes in quotesraw]

authorsraw = soup.find_all('a', attrs={"class": "bq-aut"})
authors = [authors.text for authors in authorsraw]

sg.theme('Dark Purple 6')  # please make your windows colorful


layout = [
    [sg.Text(quotes[i],
             key='quote',
             justification='left',
             font=('Times New Roman', [22], 'italic'),
             pad=(5, 10),
             size=(60, 4),
             right_click_menu=menu_def
             )
     ],
    [sg.Text(authors[i],
             key='author',
             justification='right',
             font=('Helvetica', [16], 'bold italic'),
             pad=[(0, 5), (5, 0)],
             size=(80, 2),
             right_click_menu=menu_def,
             )
     ],
    [sg.Button('Previous'), sg.Button('Next'), sg.Button('Exit')],
]

window = sg.Window(None, layout,
                   auto_size_buttons=False,
                   no_titlebar=True,
                   grab_anywhere=True,
                   keep_on_top=True,
                   alpha_channel=.75,
                   right_click_menu=[menu_def],
                   finalize=True
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
            quotes = [quote.text for quote in quotesraw]
            window['quote'].update([quotes[i].str])

            authors = [author.text for author in authorsraw]
            window['author'].update(
                [authors[i].str])

            window.refresh

        except IndexError:
            i = 0
            num += 1
            quotes = [quote.text for quote in quotesraw]
            window['quote'].update([quotes[i]])

            authors = [author.text for author in authorsraw]
            window['author'].update([authors[i]])

            window.refresh

    elif event == 'Next':
        try:
            i += 1
            quotes = [quote.text for quote in quotesraw]
            window['quote'].update([quotes[i]])

            authors = [author.text for author in authorsraw]
            window['author'].update([authors[i]])

            window.refresh

        except IndexError:
            i = 0
            num += 1

            quotes = [quote.text for quote in quotesraw]
            window['quote'].update([quotes[i]])

            authors = [author.text for author in authorsraw]
            window['author'].update([authors[i]])

            window.refresh

    elif event == 'right_click':
        window['right'].RightClickMenu()

window.close()
del window
