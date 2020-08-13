'''Populate TwitOff with users'''

import requests

URL = 'https://##YOUR_APP_NAME_HERE##.herokuapp.com/user'
# URL = 'http://127.0.0.1:5000/user'

USERNAMES = [
    'BarackObama','justinbieber','katyperry','rihanna','taylorswift13',
    'Cristiano','ladygaga','TheEllenShow','realDonaldTrump','YouTube',
    'ArianaGrande','jtimberlake','KimKardashian','selenagomez','twitter',
    'cnnbrk','britneyspears','narendramodi','shakira','jimmyfallon',
    'BillGates','neymarjr','nytimes','KingJames','MileyCyrus','CNN','JLo',
    'BrunoMars','Oprah','BBCBreaking','SrBachchan','iamsrk','NiallOfficial',
    'BeingSalmanKhan','Drake','SportsCenter','KevinHart4real','instagram',
    'wizkhalifa','NASA','espn','LilTunechi','Harry_Styles','akshaykumar',
    'realmadrid','imVkohli','Louis_Tomlinson','LiamPayne','Pink','FCBarcelona',
]

def populate_twitoff(url, usernames):
    '''POST to url for each name in usernames'''
    with requests.Session() as session:
        for username in usernames:
            print(username)
            r = session.post(url, data={'user_name':username})

if __name__ == '__main__':
    assert '##YOUR_APP_NAME_HERE##' not in URL, \
        'you must set the correct url for your deployed app'
    populate_twitoff(URL, USERNAMES)
