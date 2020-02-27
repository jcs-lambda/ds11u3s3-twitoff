#!/bin/bash

# populate twitoff with top 50 twitter handles (from wikipedia)

TWITOFF_HOST='http://127.0.0.1:5000/tweeters/'
[[ ${1} -eq "REMOTE" ]] && TWITOFF_HOST='https://twitoff-jcslambda.herokuapp.com/tweeters/'

while read HANDLE ; do
    URL=${TWITOFF_HOST}${HANDLE}
    echo ${URL}
    curl ${URL} > /dev/null
done <<EOF
BarackObama
justinbieber
katyperry
rihanna
taylorswift13
Cristiano
ladygaga
TheEllenShow
realDonaldTrump
YouTube
ArianaGrande
jtimberlake
KimKardashian
selenagomez
twitter
cnnbrk
britneyspears
narendramodi
shakira
jimmyfallon
BillGates
neymarjr
nytimes
KingJames
MileyCyrus
CNN
JLo
BrunoMars
Oprah
BBCBreaking
SrBachchan
iamsrk
NiallOfficial
BeingSalmanKhan
Drake
SportsCenter
KevinHart4real
instagram
wizkhalifa
NASA
espn
LilTunechi
Harry_Styles
akshaykumar
realmadrid
imVkohli
Louis_Tomlinson
LiamPayne
Pink
FCBarcelona
