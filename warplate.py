import lineX
from lineX import *
from akad.ttypes import *
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
from gtts import gTTS
from googletrans import Translator
#========================================================================
_session = requests.session()
botStart = time.time()
sett = codecs.open("set.json","r","utf-8")
set = json.load(sett)
plates = codecs.open("template.json","r","utf-8")
plate = json.load(plates)
settingsOpen = codecs.open("PrankBots.json","r","utf-8")
PrankBots = json.load(settingsOpen)
settingsOpen = codecs.open("Abouts.json","r","utf-8")
Abouts = json.load(settingsOpen)
#========================================================================
print("\n               [SB]")
me = LINE("gunawanmatasia21@gmail.com","gunawanyunus1981")
#print("\n               [Kicker 1]")
#kk1 = LINE("verdubbe@kerupukmlempem.ml","435crot")
#print("\n               [Kicker 2]")
#kk2 = LINE("verdubbe@wtdmugimlyfgto13b.ml","435crot")
#print("\n               [Kicker 3]")
#kk3 = LINE("verdubbe@5ddgrmk3f2dxcoqa3.gq","435crot")
#print("\n               [Kicker 4]")
#kk4 = LINE("forschte@vutdrenaf56aq9zj68.ml","435crot")
#print("\n               [Kicker 5]")
#kk5 = LINE("verdubbe@ubdeexu2ozqnoykoqn8.tk","435crot")
#print("\n               [Kicker JS]")
#kk6 = LINE("s.o.ci.ety.b.ant.en@gmail.com","Nanditendo999")
#print("\n               [AntiJS]")
#jss = LINE("sarcoblast@2p7u8ukr6pksiu.ml","435crot")

print("\n=================================================================")
print("SUKSES LOGIN BOT")
print("ɪɴᴇxʙᴏᴛs.ʟɪɴᴇ ᴠᴇʀ.8.14.2")
print("=================================================================")
print("\n=================================================================")
print("SUKSES LOGIN BOT")
print("ɪɴᴇxʙᴏᴛs.ʟɪɴᴇ ᴠᴇʀ.8.14.2")
print("=================================================================")
meProfile = me.getProfile()
meSettings = me.getSettings()
#kk1Profile = kk1.getProfile()
#kk2Profile = kk2.getProfile()
#kk3Profile = kk3.getProfile()
#kk4Profile = kk4.getProfile()
#kk5Profile = kk5.getProfile()
#kk6Profile = kk6.getProfile()
#jssProfile = jss.getProfile()
meM = meProfile.mid
#kk1Rank = kk1Profile.mid
#kk2Rank = kk2Profile.mid
#kk3Rank = kk3Profile.mid
#kk4Rank = kk4Profile.mid
#kk5Rank = kk5Profile.mid
#kk6Rank = kk6Profile.mid
#jssRank = jssProfile.mid
oepoll = OEPoll(me)
call = me
Owner = PrankBots["u41805525e29aed7480aa1f1fff83009f"]
Stiles = "┣✯͜͡❂"
BotWar = [meM] #[,kk1Rank,kk2Rank,kk3Rank,kk4Rank,kk5Rank,kk6Rank,jssRank]
allrepositories = [me] #[,kk1,kk2,kk3,kk4,kk5,kk6,jss]
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectGroup = []
ghost = []
msg_dict = {}
msg_dict1 = {}
respontags1 = {
    "Auto_text": "нα∂ιя\n✍Semoga Yang tag aku✍\n\n1 Di mudahkan rezekinya\n2 Di beri umur panjang\n3 Dan sehat sellalu\n﷽⪃⪄⫹⫺⫷⫸⫹⫺⪃⪄﷽"
}
res = {
    'num':{},
    'us':{},
    'au':{},
}
Sid={
    "Tar":{},
    "Red":{},
    "Reason":{}
}
mid = me.getProfile().mid
PrankBots["myProfile"]["displayName"] = meProfile.displayName
PrankBots["myProfile"]["statusMessage"] = meProfile.statusMessage
cont = me.getContact(meM)
PrankBots["myProfile"]["pictureStatus"] = meProfile.pictureStatus
apikey_com = "ua5b1fd053f5a6951349b912a8a7b6755"
Extr = me.getContact(apikey_com).displayName
all_Square = ["ua5b1fd053f5a6951349b912a8a7b6755"]
for busht in allrepositories:
    for anding in all_Square:
        try:
            busht.findAndAddContactsByMid(anding)
        except:pass
    for botKickers in BotWar:
        try:
            busht.findAndAddContactsByMid(botKickers)
        except:pass
#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]
def backupData():
    try:
        backup = PrankBots
        f = codecs.open('PrankBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = Abouts
        f = codecs.open('Abouts.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = set
        f = codecs.open('set.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = template
        f = codecs.open("template.json","r","utf-8")
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        ErrorX(error)
        return False
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@PrankBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def Run_Xp():
    print ("RESTART")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
Devert = "Hampura kang\nsaya "+cont.displayName+"\nNyontek Botmu bang"
def Run_Xx():
    print ("BOT KEMBALI AKTIF")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
mulai = time.time()
def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(meM).statusMessage if me.getContact(meM).statusMessage != '' else 'Kesepian jandanya cuy |ID LINE|\ndenjaka_inex', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(meM).displayName,}
    return me.sendMessage(to, me.getContact(meM).displayName, contentMetadata, 19)
def Musik1(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+kk1.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': kk1.getContact(meM).statusMessage if kk1.getContact(meM).statusMessage != '' else 'Kontol rewok balaa |ID LINE|\ndenjaka_inex', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': kk1.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  kk1.getContact(meM).displayName,}
    kk1.sendMessage(to, kk1.getContact(meM).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+kk2.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': kk2.getContact(meM).statusMessage if kk2.getContact(meM).statusMessage != '' else 'creator By meMots |ID LINE|\ndenjaka_inex', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': kk2.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  kk2.getContact(meM).displayName,}
    kk2.sendMessage(to, kk2.getContact(meM).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+kk3.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': kk3.getContact(meM).statusMessage if kk3.getContact(meM).statusMessage != '' else 'Nyari perawan |ID LINE|\ndenjaka_inex', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': kk3.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  kk3.getContact(meM).displayName,}
    kk3.sendMessage(to, kk3.getContact(meM).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+kk4.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': kk4.getContact(meM).statusMessage if kk4.getContact(meM).statusMessage != '' else 'Mancing mania |ID LINE|\ndenjaka_inex', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': kk4.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  kk4.getContact(meM).displayName,}
    kk4.sendMessage(to, kk4.getContact(meM).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+kk5.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': kk5.getContact(meM).statusMessage if kk5.getContact(meM).statusMessage != '' else 'Mujaer Memek Anyep |ID LINE|\ndenjaka_inex', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': kk5.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  kk5.getContact(meM).displayName,}
    kk5.sendMessage(to, kk5.getContact(meM).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+kk6.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': kk6.getContact(meM).statusMessage if kk6.getContact(meM).statusMessage != '' else 'Nyari janda kuy |ID LINE|\ndenjaka_inex', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': kk6.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  kk6.getContact(meM).displayName,}
    kk6.sendMessage(to, kk6.getContact(meM).displayName, contentMetadata, 19)
def Musik2(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(kk1Rank).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(kk1Rank).statusMessage if me.getContact(kk1Rank).statusMessage != '' else 'Denjaka tukang nyari janda desahhh', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(kk1Rank).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(kk1Rank).displayName,}
    me.sendMessage(to, me.getContact(kk1Rank).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(kk2Rank).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(kk2Rank).statusMessage if me.getContact(kk2Rank).statusMessage != '' else 'Denjaka tukang nyari janda kembang songler', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(kk2Rank).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(kk2Rank).displayName,}
    me.sendMessage(to, me.getContact(kk2Rank).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(kk3Rank).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(kk3Rank).statusMessage if me.getContact(kk3Rank).statusMessage != '' else 'Denjaka tukang nyari janda aduhaay', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(kk3Rank).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(kk3Rank).displayName,}
    me.sendMessage(to, me.getContact(kk3Rank).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(kk4Rank).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(kk4Rank).statusMessage if me.getContact(kk4Rank).statusMessage != '' else 'Denjaka tukang nyari janda kesepian', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(kk4Rank).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(kk4Rank).displayName,}
    me.sendMessage(to, me.getContact(kk4Rank).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(kk5Rank).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(kk5Rank).statusMessage if me.getContact(kk5Rank).statusMessage != '' else 'Denjaka tukang nyari janda montook', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(kk5Rank).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(kk5Rank).displayName,}
    me.sendMessage(to, me.getContact(kk5Rank).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(kk6Rank).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(kk6Rank).statusMessage if me.getContact(kk6Rank).statusMessage != '' else 'Denjaka tukang nyari janda bahenooll', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(kk6Rank).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(kk6Rank).displayName,}
    me.sendMessage(to, me.getContact(kk6Rank).displayName, contentMetadata, 19)
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(jssRank).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(jssRank).statusMessage if me.getContact(jssRank).statusMessage != '' else 'Denjaka tukang nyari janda semoook', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(jssRank).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(jssRank).displayName,}
    me.sendMessage(to, me.getContact(jssRank).displayName, contentMetadata, 19)
def ErrorX(text):
    me.log("data: " + str(text))
    time_ = datetime.now()
    with open("Data.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    client.sendMessage(to, '', contentMetadata, 7)
def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        contact = me.getContact(mid)
        Np = me.getContact(mid).pictureStatus
        path = "http://dl.profile.line.naver.jp/"+ Np
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = ""
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        #me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
        warnanya1 = random.choice(warna1)
        try:
          poto = "https://os.line.naver.jp/os/p/{}".format(str(path)),
        except:
          poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
        data = {
            "type": "flex",
            "altText": "{} MEMBAGIKAN SEMBAKO ".format(meProfile.displayName),
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#333300",
               },
               "body": {
                 "backgroundColor": "#333333",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#333333",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "🅃🄰🄶🅁🄴🅂🄿🄾🄽",
                   "weight": "bold",
                   "color": warnanya1,
                   "size": "md"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url":  "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=b6faa883755d778161424e0b22ac5dbf&oe=5CDAA4F5",
               "size": "full",
               "aspectRatio": "3:4",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/~denjaka_inex"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": str(text),
                               "wrap": True,
                               "color": warnanya1,
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": warnanya1,
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD MY LINE",
                            "uri": "https://line.me/ti/p/"+me.getUserTicket().id
                            }													
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
        me.sendFlex(to, data)
    except Exception as error:
        ErrorX(error)
        me.sendMessage(to, "Error\n\n" + str(error))
extras = Extr+"\n"
def RunTheRun(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,7,25)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = me.getAllContactIds()
        gid = me.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        h = me.getContact(meM)
        me.reissueUserTicket()
        My_Id = "http://line.me/ti/p/"+me.getUserTicket().id
        text += mention+"WAKTU : "+datetime.strftime(timeNow,'%H:%M:%S')+" INDONESIA\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND: "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nINEX_TEAM. ʟɪɴᴇ ᴠᴇʀ.8.14.2\n\nTANGGAL : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nTIME RUN : \n • "+bot+"\n\nMY TOKEN : "+str(me.authToken)+"\n\nMY MID : "+h.mid+"\n\nMY ID LINE : "+My_Id
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        me.sendMessage(to, "Error :\n" + str(error))
warKey = """╔━━═══[HELPWAR]═══━━╗
╚━━═════════════━━╝
╭━═[ 🇮🇩XTC_IΠΣX🇮🇩]═━
✯͜͡❂ʀᴇsᴛᴀʀᴛ
✯͜͡❂sᴘᴇᴇᴅ
✯͜͡❂ʀᴜɴᴛɪᴍᴇ
✯͜͡❂sᴛᴀᴛᴜs
✯͜͡❂ᴀʙᴏᴜᴛ
✯͜͡❂ᴍʏᴍɪᴅ
✯͜͡❂ᴍʏᴘɪᴄᴛ
✯͜͡❂ᴍʏᴠɪᴅ
✯͜͡❂ᴍʏᴄᴏᴠᴇʀ
✯͜͡❂ᴜᴘᴅᴀᴛᴇ ᴘɪᴄᴛ
✯͜͡❂ɢᴇᴛᴄᴏɴᴛᴀᴄᴛ 「@」
✯͜͡❂ɢᴇᴛᴍɪᴅ 「@」
✯͜͡❂ɢᴇᴛɴᴀᴍᴇ 「@」
✯͜͡❂ɢᴇᴛʙɪᴏ 「@」
✯͜͡❂ɢᴇᴛᴘɪᴄᴛ 「@」
✯͜͡❂ɢᴇᴛᴠɪᴅ 「@」
✯͜͡❂ɢᴇᴛᴄᴏᴠᴇʀ 「@」
✯͜͡❂ᴍʏᴄᴏᴘʏ 「@」
✯͜͡❂ᴍʏʙᴀᴄᴋᴜᴘ
✯͜͡❂ᴍʏɢʀᴏᴜᴘ
✯͜͡❂ᴍʏғʀɪᴇɴᴅ
✯͜͡❂ᴀᴜᴛᴏᴀᴅᴅ on/off
✯͜͡❂ᴀᴜᴛᴏᴊᴏɪɴ on/off
✯͜͡❂ᴀᴜᴛᴏʟᴇᴀᴠᴇ on/off
✯͜͡❂ᴀᴜᴛᴏʀᴇᴀᴅ on/off
✯͜͡❂ʙᴏᴛ ᴍᴜᴛᴇ
╔━━═════════════━━╗
╚━━═══[ INEXBOT]═══━━╝"""
helpBot = """╔━━═══[HELP BOTS]═══━━╗
╚━━══════════════━━╝
━═͜͡❂_MY BOT_❂͜͡═━
━═͜͡❂_PING_❂͜͡═━
━═͜͡❂ BOT1NAME: /BOT7NAME:  ❂͜͡═━
━═͜͡❂ BOT1UP/ BOT7UP ❂͜͡═━
━═͜͡❂ SP ❂͜͡═━
━═͜͡❂ MASUK ❂͜͡═━
━═͜͡❂ KELUAR ❂͜͡═━
━═͜͡❂ G JOIN/GHOST BYE ❂͜͡═━
━═͜͡❂ CROT @ ❂͜͡═━
━═͜͡❂ CIPOK @ ❂͜͡═━
━═͜͡❂ PING ❂͜͡═━
━═͜͡❂ GAS ❂͜͡═━
╔━━═════════════━━╗
╚━━═══[INEXBOT ]═══━━╝""" 
def SqL_R(text):
    R_SQL = text.lower()
    if PrankBots["key"] == True:
        if R_SQL.startswith(PrankBots["text"]):
            PrankBotsData = R_SQL.replace(PrankBots["text"],"")
        else:
            PrankBotsData = "Undefined command"
    else:
        PrankBotsData = text.lower()
    return PrankBotsData
def serviceX(rank):
    global groupParam
    opps1 = rank.param1
    opps2 = rank.param2
    opps3 = rank.param3
    try:
        if rank.type == 0:
            return
        if rank.type == 19 or rank.type == 32:
            if meM in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk1.inviteIntoGroup(opps1,[opps3])
                        kk1.kickoutFromGroup(opps1,[opps2])
                        me.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk2.inviteIntoGroup(opps1,[opps3])
                            kk2.kickoutFromGroup(opps1,[opps2])
                            me.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk3.inviteIntoGroup(opps1,[opps3])
                                kk3.kickoutFromGroup(opps1,[opps2])
                                me.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk4.inviteIntoGroup(opps1,[opps3])
                                    kk4.kickoutFromGroup(opps1,[opps2])
                                    me.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk5.inviteIntoGroup(opps1,[opps3])
                                        kk5.kickoutFromGroup(opps1,[opps2])
                                        me.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            kk6.inviteIntoGroup(opps1,[opps3])
                                            kk6.kickoutFromGroup(opps1,[opps2])
                                            me.acceptGroupInvitation(opps1)
                                        except:
                                            try:
                                                jss.acceptGroupInvitation(opps1)
                                                print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                                                jss.kickoutFromGroup(opps1,[opps2])
                                                P = jss.getGroup(opps1)
                                                P.preventedJoinByTicket = False
                                                jss.updateGroup(P)
                                                Ti = jss.reissueGroupTicket(opps1)
                                                me.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk1.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk2.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk3.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk4.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk5.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk6.acceptGroupInvitationByTicket(opps1,Ti)
                                                jss.leaveGroup(opps1)
                                                kk1.findAndAddContactsByMid(jssRank)
                                                kk1.inviteIntoGroup(opps1,[jssRank])
                                                Ti = kk1.reissueGroupTicket(opps1)
                                            except:pass
            if kk1Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk2.inviteIntoGroup(opps1,[opps3])
                        kk2.kickoutFromGroup(opps1,[opps2])
                        kk1.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk3.inviteIntoGroup(opps1,[opps3])
                            kk3.kickoutFromGroup(opps1,[opps2])
                            kk1.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk4.inviteIntoGroup(opps1,[opps3])
                                kk4.kickoutFromGroup(opps1,[opps2])
                                kk1.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk5.inviteIntoGroup(opps1,[opps3])
                                    kk5.kickoutFromGroup(opps1,[opps2])
                                    kk1.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk6.inviteIntoGroup(opps1,[opps3])
                                        kk6.kickoutFromGroup(opps1,[opps2])
                                        kk1.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            me.inviteIntoGroup(opps1,[opps3])
                                            me.kickoutFromGroup(opps1,[opps2])
                                            kk1.acceptGroupInvitation(opps1)
                                        except:
                                            try:
                                                jss.acceptGroupInvitation(opps1)
                                                print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                                                jss.kickoutFromGroup(opps1,[opps2])
                                                P = jss.getGroup(opps1)
                                                P.preventedJoinByTicket = False
                                                jss.updateGroup(P)
                                                Ti = jss.reissueGroupTicket(opps1)
                                                me.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk1.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk2.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk3.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk4.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk5.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk6.acceptGroupInvitationByTicket(opps1,Ti)
                                                jss.leaveGroup(opps1)
                                                kk2.findAndAddContactsByMid(jssRank)
                                                kk2.inviteIntoGroup(opps1,[jssRank])
                                                Ti = kk2.reissueGroupTicket(opps1)
                                            except:pass
            if kk2Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk3.inviteIntoGroup(opps1,[opps3])
                        kk3.kickoutFromGroup(opps1,[opps2])
                        kk2.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk4.inviteIntoGroup(opps1,[opps3])
                            kk4.kickoutFromGroup(opps1,[opps2])
                            kk2.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk5.inviteIntoGroup(opps1,[opps3])
                                kk5.kickoutFromGroup(opps1,[opps2])
                                kk2.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk6.inviteIntoGroup(opps1,[opps3])
                                    kk6.kickoutFromGroup(opps1,[opps2])
                                    kk2.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        me.inviteIntoGroup(opps1,[opps3])
                                        me.kickoutFromGroup(opps1,[opps2])
                                        kk2.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            kk1.inviteIntoGroup(opps1,[opps3])
                                            kk1.kickoutFromGroup(opps1,[opps2])
                                            kk2.acceptGroupInvitation(opps1)
                                        except:
                                            try:
                                                jss.acceptGroupInvitation(opps1)
                                                print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                                                jss.kickoutFromGroup(opps1,[opps2])
                                                P = jss.getGroup(opps1)
                                                P.preventedJoinByTicket = False
                                                jss.updateGroup(P)
                                                Ti = jss.reissueGroupTicket(opps1)
                                                me.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk1.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk2.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk3.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk4.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk5.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk6.acceptGroupInvitationByTicket(opps1,Ti)
                                                jss.leaveGroup(opps1)
                                                kk3.findAndAddContactsByMid(jssRank)
                                                kk3.inviteIntoGroup(opps1,[jssRank])
                                                Ti = kk3.reissueGroupTicket(opps1)
                                            except:pass
            if kk3Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk4.inviteIntoGroup(opps1,[opps3])
                        kk4.kickoutFromGroup(opps1,[opps2])
                        kk3.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk5.inviteIntoGroup(opps1,[opps3])
                            kk5.kickoutFromGroup(opps1,[opps2])
                            kk3.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk6.inviteIntoGroup(opps1,[opps3])
                                kk6.kickoutFromGroup(opps1,[opps2])
                                kk3.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    me.inviteIntoGroup(opps1,[opps3])
                                    me.kickoutFromGroup(opps1,[opps2])
                                    kk3.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk1.inviteIntoGroup(opps1,[opps3])
                                        kk1.kickoutFromGroup(opps1,[opps2])
                                        kk3.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            kk2.inviteIntoGroup(opps1,[opps3])
                                            kk2.kickoutFromGroup(opps1,[opps2])
                                            kk3.acceptGroupInvitation(opps1)
                                        except:
                                            try:
                                                jss.acceptGroupInvitation(opps1)
                                                print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                                                jss.kickoutFromGroup(opps1,[opps2])
                                                P = jss.getGroup(opps1)
                                                P.preventedJoinByTicket = False
                                                jss.updateGroup(P)
                                                Ti = jss.reissueGroupTicket(opps1)
                                                me.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk1.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk2.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk3.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk4.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk5.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk6.acceptGroupInvitationByTicket(opps1,Ti)
                                                jss.leaveGroup(opps1)
                                                kk4.findAndAddContactsByMid(jssRank)
                                                kk4.inviteIntoGroup(opps1,[jssRank])
                                                Ti = kk4.reissueGroupTicket(opps1)
                                            except:pass
            if kk4Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk5.inviteIntoGroup(opps1,[opps3])
                        kk5.kickoutFromGroup(opps1,[opps2])
                        kk4.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk6.inviteIntoGroup(opps1,[opps3])
                            kk6.kickoutFromGroup(opps1,[opps2])
                            kk4.acceptGroupInvitation(opps1)
                        except:
                            try:
                                me.inviteIntoGroup(opps1,[opps3])
                                me.kickoutFromGroup(opps1,[opps2])
                                kk4.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk1.inviteIntoGroup(opps1,[opps3])
                                    kk1.kickoutFromGroup(opps1,[opps2])
                                    kk4.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk2.inviteIntoGroup(opps1,[opps3])
                                        kk2.kickoutFromGroup(opps1,[opps2])
                                        kk4.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            kk3.inviteIntoGroup(opps1,[opps3])
                                            kk3.kickoutFromGroup(opps1,[opps2])
                                            kk4.acceptGroupInvitation(opps1)
                                        except:
                                            try:
                                                jss.acceptGroupInvitation(opps1)
                                                print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                                                jss.kickoutFromGroup(opps1,[opps2])
                                                P = jss.getGroup(opps1)
                                                P.preventedJoinByTicket = False
                                                jss.updateGroup(P)
                                                Ti = jss.reissueGroupTicket(opps1)
                                                me.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk1.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk2.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk3.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk4.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk5.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk6.acceptGroupInvitationByTicket(opps1,Ti)
                                                jss.leaveGroup(opps1)
                                                kk5.findAndAddContactsByMid(jssRank)
                                                kk5.inviteIntoGroup(opps1,[jssRank])
                                                Ti = kk5.reissueGroupTicket(opps1)
                                            except:pass
            if kk5Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk6.inviteIntoGroup(opps1,[opps3])
                        kk6.kickoutFromGroup(opps1,[opps2])
                        kk5.acceptGroupInvitation(opps1)
                    except:
                        try:
                            me.inviteIntoGroup(opps1,[opps3])
                            me.kickoutFromGroup(opps1,[opps2])
                            kk5.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk1.inviteIntoGroup(opps1,[opps3])
                                kk1.kickoutFromGroup(opps1,[opps2])
                                kk5.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk2.inviteIntoGroup(opps1,[opps3])
                                    kk2.kickoutFromGroup(opps1,[opps2])
                                    kk5.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk3.inviteIntoGroup(opps1,[opps3])
                                        kk3.kickoutFromGroup(opps1,[opps2])
                                        kk5.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            kk4.inviteIntoGroup(opps1,[opps3])
                                            kk4.kickoutFromGroup(opps1,[opps2])
                                            kk5.acceptGroupInvitation(opps1)
                                        except:
                                            try:
                                                jss.acceptGroupInvitation(opps1)
                                                print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                                                jss.kickoutFromGroup(opps1,[opps2])
                                                P = jss.getGroup(opps1)
                                                P.preventedJoinByTicket = False
                                                jss.updateGroup(P)
                                                Ti = jss.reissueGroupTicket(opps1)
                                                me.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk1.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk2.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk3.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk4.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk5.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk6.acceptGroupInvitationByTicket(opps1,Ti)
                                                jss.leaveGroup(opps1)
                                                kk6.findAndAddContactsByMid(jssRank)
                                                kk6.inviteIntoGroup(opps1,[jssRank])
                                                Ti = kk6.reissueGroupTicket(opps1)
                                            except:pass
            if kk6Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        me.inviteIntoGroup(opps1,[opps3])
                        me.kickoutFromGroup(opps1,[opps2])
                        kk6.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk1.inviteIntoGroup(opps1,[opps3])
                            kk1.kickoutFromGroup(opps1,[opps2])
                            kk6.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk2.inviteIntoGroup(opps1,[opps3])
                                kk2.kickoutFromGroup(opps1,[opps2])
                                kk6.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk3.inviteIntoGroup(opps1,[opps3])
                                    kk3.kickoutFromGroup(opps1,[opps2])
                                    kk6.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk4.inviteIntoGroup(opps1,[opps3])
                                        kk4.kickoutFromGroup(opps1,[opps2])
                                        kk6.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            kk5.inviteIntoGroup(opps1,[opps3])
                                            kk5.kickoutFromGroup(opps1,[opps2])
                                            kk6.acceptGroupInvitation(opps1)
                                        except:
                                            try:
                                                jss.acceptGroupInvitation(opps1)
                                                print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                                                jss.kickoutFromGroup(opps1,[opps2])
                                                P = jss.getGroup(opps1)
                                                P.preventedJoinByTicket = False
                                                jss.updateGroup(P)
                                                Ti = jss.reissueGroupTicket(opps1)
                                                me.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk1.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk2.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk3.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk4.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk5.acceptGroupInvitationByTicket(opps1,Ti)
                                                kk6.acceptGroupInvitationByTicket(opps1,Ti)
                                                jss.leaveGroup(opps1)
                                                me.findAndAddContactsByMid(jssRank)
                                                me.inviteIntoGroup(opps1,[jssRank])
                                                Ti = me.reissueGroupTicket(opps1)
                                            except:pass

                    PrankBots["blacklist"] = True
                    try:
                        kk1.inviteIntoGroup(opps1,[opps3])
                        kk1.kickoutFromGroup(opps1,[opps2])
                    except:
                        try:
                            kk2.inviteIntoGroup(opps1,[opps3])
                            kk2.kickoutFromGroup(opps1,[opps2])
                        except:
                            try:
                                kk3.inviteIntoGroup(opps1,[opps3])
                                kk3.kickoutFromGroup(opps1,[opps2])
                            except:
                                try:
                                    kk4.inviteIntoGroup(opps1,[opps3])
                                    kk4.kickoutFromGroup(opps1,[opps2])
                                except:
                                    try:
                                        kk5.inviteIntoGroup(opps1,[opps3])
                                        kk5.kickoutFromGroup(opps1,[opps2])
                                    except:
                                        try:
                                            kk6.inviteIntoGroup(opps1,[opps3])
                                            kk6.kickoutFromGroup(opps1,[opps2])
                                        except:
                                            try:
                                                me.inviteIntoGroup(opps1,[opps3])
                                                me.kickoutFromGroup(opps1,[opps2])
                                            except:pass
        if rank.type == 17:
            if opps2 in PrankBots["blacklist"]:
                try:
                    kk1.kickoutFromGroup(opps1,[opps2])
                except:
                    try:
                        kk2.kickoutFromGroup(opps1,[opps2])
                    except:
                        try:
                            kk3.kickoutFromGroup(opps1,[opps2])
                        except:
                            try:
                                kk4.kickoutFromGroup(opps1,[opps2])
                            except:
                                try:
                                    kk5.kickoutFromGroup(opps1,[opps2])
                                except:
                                    try:
                                        kk6.kickoutFromGroup(opps1,[opps2])
                                    except:
                                        try:
                                            jss.kickoutFromGroup(opps1,[opps2])
                                        except:pass
            else:pass
        if rank.type == 13:
            if opps3 in PrankBots["blacklist"]:
                try:
                    kk5.cancelGroupInvitation(opps1,[opps3])
                except:
                    try:
                        kk4.cancelGroupInvitation(opps1,[opps3])
                    except:
                        try:
                            kk3.cancelGroupInvitation(opps1,[opps3])
                        except:
                            try:
                                kk2.cancelGroupInvitation(opps1,[opps3])
                            except:
                                try:
                                    kk1.cancelGroupInvitation(opps1,[opps3])
                                except:pass
            else:pass
        if rank.type == 32:
            if opps3 in jssRank:
              if opps2 not in BotWar and opps2 not in Owner and opps2 not in meM:
                  PrankBots["blacklist"][opps2] = True
                  try:
                      if opps3 not in PrankBots["blacklist"]:
                          kk1.kickoutFromGroup(opps1,[opps2])
                          kk1.inviteIntoGroup(opps1,[jssRank])
                          kk1.sendMessage(opps1, "Diih,, \njangan d cancle cuk...\nItu AntiJS..")
                  except:
                      try:
                          if opps3 not in PrankBots["blacklist"]:
                              kk2.kickoutFromGroup(opps1,[opps2])
                              kk2.inviteIntoGroup(opps1,[jssRank])
                              kk2.sendMessage(opps1, "Diih,, \njangan d cancle cuk...\nItu AntiJS..")
                      except:
                          try:
                              if opps3 not in PrankBots["blacklist"]:
                                  kk3.kickoutFromGroup(opps1,[opps2])
                                  kk3.inviteIntoGroup(opps1,[jssRank])
                                  kk3.sendMessage(opps1, "Diih,, \njangan d cancle cuk...\nItu AntiJS..")
                          except:
                              try:
                                  if opps3 not in PrankBots["blacklist"]:
                                      kk4.kickoutFromGroup(opps1,[opps2])
                                      kk4.inviteIntoGroup(opps1,[jssRank])
                                      kk4.sendMessage(opps1, "Diih,, \njangan d cancle cuk...\nItu AntiJS..")
                              except:
                                  try:
                                      if opps3 not in PrankBots["blacklist"]:
                                          kk5.kickoutFromGroup(opps1,[opps2])
                                          kk5.inviteIntoGroup(opps1,[jssRank])
                                          kk5.sendMessage(opps1, "Diih,, \njangan d cancle cuk...\nItu AntiJS..")
                                  except:
                                      try:
                                          if opps3 not in PrankBots["blacklist"]:
                                              kk6.kickoutFromGroup(opps1,[opps2])
                                              kk6.inviteIntoGroup(opps1,[jssRank])
                                              kk6.sendMessage(opps1, "Diih,, \njangan d cancle cuk...\nItu AntiJS..")
                                      except:
                                          try:
                                              if opps3 not in PrankBots["blacklist"]:
                                                  me.kickoutFromGroup(opps1,[opps2])
                                                  me.inviteIntoGroup(opps1,[jssRank])
                                                  me.sendMessage(opps1, "Diih,, \njangan d cancle cuk...\nItu AntiJS..")
                                                  P = me.getGroup(opps1)
                                                  P.preventedJoinByTicket = False
                                                  me.updateGroup(P)
                                                  Ti = me.reissueGroupTicket(opps1)
                                                  kk1.acceptGroupInvitationByTicket(opps1,Ti)
                                                  kk2.acceptGroupInvitationByTicket(opps1,Ti)
                                                  kk3.acceptGroupInvitationByTicket(opps1,Ti)
                                                  kk4.acceptGroupInvitationByTicket(opps1,Ti)
                                                  kk5.acceptGroupInvitationByTicket(opps1,Ti)
                                                  kk6.acceptGroupInvitationByTicket(opps1,Ti)
                                                  me.findAndAddContactsByMid(jssRank)
                                                  me.inviteIntoGroup(opps1,[jssRank])
                                                  Ti = me.reissueGroupTicket(opps1)
                                          except:
                                              pass
              return
        if rank.type == 26 or rank.type == 25:
            msg = rank.message
            Id = msg.id
            R = msg.to
            D = msg._from
            Proses_message = msg.text
            if Proses_message == "Active" or Proses_message == "active":
                if D in Owner or D in meM:
                    PrankBots["bot"] = True
                    me.sendMessage(R,"Bot active")
                    me.sendMessage(R,"Already Ok "+me.getContact(D).displayName)
                    PrankBots["Conection"] = R
                    Run_Xx()
                    
            if Proses_message == "Non active" or Proses_message == "non active":
                print ("NOTIF BOT NON ACTIVE")
                if D in Owner or D in meM:
                    PrankBots["bot"] = False
                    me.sendMessage(R,"Bot Non Active")
                    me.sendMessage(R,"Ok I'am Turn down "+me.getContact(D).displayName)
                
        if rank.type == 25 or rank.type == 26:
          if PrankBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Id = msg.id
            R = msg.to
            D = msg._from
            Gr = opps1
            OperPrankBotsData = PrankBots["text"].title()
            if PrankBots["key"] == False:
                 OperPrankBotsData = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if D != me.profile.mid:
                        to = D
                    else:
                        to = R
                if msg.toType == 1:
                    to = R
                if msg.toType == 2:
                    to = R
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        PrankBotsData = SqL_R(text)
                        if PrankBotsData == Abouts["1"]:
                          if D in Owner or D in meM:
                            Res= extras+"╔━━═══════════════━━╗\n┣✯͜͡❂ 丨几乇乂乃ㄖㄒ丂\n╚━━═══════════════━━╝\n╔━━═══════════════━━╗\n"
                            Res+= Stiles+"1. "+OperPrankBotsData+Abouts["1"]+"\n"
                            Res+= Stiles+"2. "+OperPrankBotsData+Abouts["2"]+"\n"
                            Res+= Stiles+"3. "+OperPrankBotsData+Abouts["3"]+"\n"
                            Res+= Stiles+"4. "+OperPrankBotsData+Abouts["4"]+"\n"
                            Res+= Stiles+"5. "+OperPrankBotsData+Abouts["5"]+"\n"
                            Res+= Stiles+"6. "+OperPrankBotsData+Abouts["6"]+"\n"
                            Res+= Stiles+"7. "+OperPrankBotsData+Abouts["7"]+"\n"
                            Res+= Stiles+"8. "+OperPrankBotsData+Abouts["8"]+" *porn\n"
                            Res+= Stiles+"9. "+OperPrankBotsData+Abouts["9"]+" *judul\n"
                            Res+= Stiles+"10. "+OperPrankBotsData+Abouts["10"]+" *tags\n"
                            Res+= Stiles+"11. "+OperPrankBotsData+Abouts["11"]+"\n"
                            Res+= Stiles+"12. "+OperPrankBotsData+Abouts["12"]+" *txt/txt/txt\n"
                            Res+= Stiles+"13. "+OperPrankBotsData+Abouts["13"]+" *text\n"
                            Res+= Stiles+"14. "+OperPrankBotsData+Abouts["14"]+"\n"
                            Res+= Stiles+"15. "+OperPrankBotsData+Abouts["15"]+"\n"
                            Res+= Stiles+"16. "+OperPrankBotsData+Abouts["16"]+"\n"
                            Res+= Stiles+"17. "+OperPrankBotsData+Abouts["17"]+"\n"
                            Res+= Stiles+"18. "+OperPrankBotsData+Abouts["18"]+"\n"
                            Res+= Stiles+"19. "+OperPrankBotsData+Abouts["19"]+" *tags\n"
                            Res+= Stiles+"20. "+OperPrankBotsData+Abouts["20"]+" *tags\n"
                            Res+= Stiles+"21. "+OperPrankBotsData+Abouts["21"]+" *tags\n"
                            Res+= Stiles+"22. "+OperPrankBotsData+Abouts["22"]+" *tags\n"
                            Res+= Stiles+"23. "+OperPrankBotsData+Abouts["23"]+" *tags\n"
                            Res+= Stiles+"24. "+OperPrankBotsData+Abouts["24"]+" *tags\n"
                            Res+= Stiles+"25. "+OperPrankBotsData+Abouts["25"]+" *text\n"
                            Res+= Stiles+"26. "+OperPrankBotsData+Abouts["26"]+" *01-02-1995\n"
                            Res+= Stiles+"27. "+OperPrankBotsData+Abouts["27"]+" *id ig\n"
                            Res+= Stiles+"28. "+OperPrankBotsData+Abouts["28"]+" *id smule\n"
                            Res+= Stiles+"29. "+OperPrankBotsData+Abouts["29"]+"\n"
                            Res+= Stiles+"30. "+OperPrankBotsData+Abouts["30"]+" *text\n"
                            Res+= Stiles+"31. "+OperPrankBotsData+Abouts["31"]+" *text\n"
                            Res+= Stiles+"32. "+OperPrankBotsData+Abouts["32"]+"\n"
                            Res+= Stiles+"33. "+OperPrankBotsData+Abouts["33"]+" *text\n"
                            Res+= Stiles+"34. "+OperPrankBotsData+Abouts["34"]+"\n"
                            Res+= Stiles+"35. "+OperPrankBotsData+Abouts["35"]+"\n"
                            Res+= Stiles+"36. "+OperPrankBotsData+Abouts["36"]+"\n"
                            Res+= Stiles+"37. "+OperPrankBotsData+Abouts["37"]+"\n"
                            Res+= Stiles+"38. "+OperPrankBotsData+Abouts["38"]+"\n"
                            Res+= Stiles+"39. "+OperPrankBotsData+Abouts["39"]+"\n"
                            Res+= Stiles+"40. "+OperPrankBotsData+Abouts["40"]+"\n"
                            Res+= Stiles+"41. "+OperPrankBotsData+Abouts["41"]+"\n"
                            Res+= Stiles+"42. "+OperPrankBotsData+Abouts["42"]+"\n"
                            Res+= Stiles+"43. "+OperPrankBotsData+Abouts["43"]+"\n"
                            Res+= Stiles+"44. "+OperPrankBotsData+Abouts["44"]+"\n"
                            Res+= Stiles+"45. "+OperPrankBotsData+Abouts["45"]+"\n"
                            Res+= Stiles+"46. "+OperPrankBotsData+Abouts["46"]+"\n"
                            Res+= Stiles+"47. "+OperPrankBotsData+Abouts["47"]+"\n"
                            Res+= Stiles+"48. "+OperPrankBotsData+Abouts["48"]+"\n"
                            Res+= Stiles+"49. "+OperPrankBotsData+Abouts["49"]+"\n"
                            Res+= Stiles+"50. "+OperPrankBotsData+Abouts["50"]+"\n"
                            Res+= Stiles+"51. "+OperPrankBotsData+Abouts["51"]+"\n"
                            Res+= Stiles+"52. "+OperPrankBotsData+Abouts["52"]+"\n"
                            Res+= Stiles+"53. "+OperPrankBotsData+Abouts["53"]+"\n"
                            Res+= Stiles+"54. "+OperPrankBotsData+Abouts["54"]+"\n"
                            Res+= Stiles+"55. "+OperPrankBotsData+Abouts["55"]+"\n"
                            Res+= Stiles+"56. "+OperPrankBotsData+Abouts["56"]+"\n"
                            Res+= Stiles+"57. "+OperPrankBotsData+Abouts["57"]+"\n"
                            Res+= Stiles+"58. "+OperPrankBotsData+Abouts["58"]+"\n"
                            Res+= Stiles+"59. "+OperPrankBotsData+Abouts["59"]+"\n"
                            Res+= Stiles+"60. "+OperPrankBotsData+Abouts["60"]+"\n"
                            Res+= Stiles+"61. "+OperPrankBotsData+Abouts["61"]+"\n"
                            Res+= Stiles+"62. "+OperPrankBotsData+Abouts["62"]+"\n"
                            Res+= Stiles+"63. "+OperPrankBotsData+Abouts["63"]+"\n"
                            Res+= Stiles+"64. "+OperPrankBotsData+Abouts["64"]+"\n"
                            Res+= Stiles+"65. "+OperPrankBotsData+Abouts["65"]+"\n"
                            Res+= Stiles+"66. "+OperPrankBotsData+Abouts["66"]+"\n"
                            Res+= Stiles+"67. "+OperPrankBotsData+Abouts["67"]+"\n"
                            Res+= Stiles+"68. "+OperPrankBotsData+Abouts["68"]+"\n"
                            Res+= Stiles+"69. "+OperPrankBotsData+Abouts["69"]+"\n"
                            Res+= Stiles+"70. "+OperPrankBotsData+Abouts["70"]+"\n"
                            Res+= Stiles+"71. "+OperPrankBotsData+Abouts["71"]+"\n"
                            Res+= Stiles+"72. "+OperPrankBotsData+Abouts["72"]+"\n╚━━═══════════════━━╝\n\n"
                            Res+= "╔━━━━━━━━━━━━━━━━━╗\n┣━━━━━━━━━━━━━━━━━━\n┣🅾  STATUS  🅾\n┣━━━━━━━━━━━━━━━━━━\n┣━━━━━━━━━━━━━━━━━━\n"
                            if PrankBots["Add"] == True: Res+= Stiles+" autoadd->『on』\n"
                            else: Res+= Stiles+" autoadd->『off』\n"
                            if PrankBots["Shared"] == True: Res+= Stiles+" shared->『on』\n"
                            else: Res+= Stiles+" shared->『off』\n"
                            if PrankBots["Join"] == True: Res+= Stiles+" autojoin->『on』\n"
                            else: Res+= Stiles+" autojoin->『off』\n"
                            if PrankBots["Read"] == True: Res+= Stiles+" autoread->『on』\n"
                            else: Res+= Stiles+" autoread->『off』\n"
                            if PrankBots["Unsend"] == True: Res+= Stiles+" unsend->『on』\n"
                            else: Res+= Stiles+" unsend->『off』\n"
                            if PrankBots["Wc"] == True: Res+= Stiles+" welcome->『on』\n"
                            else: Res+= Stiles+" welcome->『off』\n"
                            if PrankBots["Respon"] == True: Res+= Stiles+" respon->『on』\n"
                            else: Res+= Stiles+" respon->『off』\n"
                            Res+= "┣━━━━━━━━━━━━━━━━━━\n"
                            Res+= "┣━━━━━━━━━━━━━━━━━━\n"+Stiles+meProfile.displayName+"\n"
                            me.sendMessage(R, str(Res)+Stiles+ "ADD my LINE\n╚━━═══════════════━━╝\n   https://line.me/ti/p/~denjaka_inex")
                        if PrankBotsData == Abouts["2"]:
                          if D in Owner or D in meM:
                            try:
                                h = me.getContact(msg._from)
                                me.reissueUserTicket()
                                Musik(R)
                            except:Musik(R)
                            data = {
                             "type": "flex",
                             "altText": "{} Membagikan kutang".format(str(h.displayName)),
                             "contents": {
                              "type": "bubble",
                              "styles": {
                                "header": {
                                  "backgroundColor": "#333300",
                                },
                                "body": {
                                  "backgroundColor": "#333333",
                                  "separator": True,
                                  "separatorColor": "#ffffff"
                                },
                                "footer": {
                                  "backgroundColor": "#333333",
                                  "separator": True
                                }
                              },
                              "header": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "  ɪɴᴅᴏɴᴇsɪᴀ_ᴡᴀʀs",
                                    "weight": "bold",
                                    "color": "#00ffff",
                                    "size": "xxl"
                                  }
                                ]
                              },
                              "hero": {
                                "type": "image",
                                "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/~denjaka_inex"
                                }
                              },
                              "body": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "md",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/~denjaka_inex"
                                },
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "🅸🅽🅴🆇🅱🅾🆃🆂",
                                    "size": "md",
                                    "color": "#00ffff"
                                  },
                                  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "sm",
                                    "contents": [
                                      {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                          {
                                            "type": "icon",
                                            "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                            "size": "5xl"
                                          },
                                          {
                                            "type": "text",
                                            "text": "Name : ",
                                            "weight": "bold",
                                            "color": "#008B8B",
                                            "margin": "sm",
                                            "flex": 0
                                          },
                                          {
                                            "type": "text",
                                            "text": h.displayName,
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                          }
                                        ]
                                      },
                                      {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                          {
                                            "type": "icon",
                                            "url": "https://z-m-scontent.fcgk3-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/52427967_2326064874084289_579878214831177728_o.jpg?_nc_cat=107&efg=eyJpIjoibyJ9&_nc_eui2=AeFEtf_my03tw7bLy7duknN8C_ofKGrLNvSnsbK6vezlyCteVLjGJZYC9Gwoh3fTmSPhRQs-xosP2j1ETI4AHqVhRwGLG-jKP5RZRlJFyGiI709TqLL_T-4lrMTYld56z-4&_nc_ad=z-m&_nc_cid=1101&_nc_zor=9&_nc_ht=z-m-scontent.fcgk3-1.fna&oh=727cfbeb9f1791b3c35dc3aae5d603fa&oe=5CEE0431",
                                            "size": "5xl"
                                          },
                                          {
                                            "type": "text",
                                            "text": "TEAM :",
                                            "margin": "sm",
                                            "color": "#008B8B",
                                            "weight": "bold",
                                            "flex": 0
                                          },
                                          {
                                            "type": "text",
                                            "text": "INEXBOTS",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                          }
                                        ]
                                      }
                                    ]
                                  },
                                  {
                                    "type": "text",
                                    "text": "Thanks to Allah AWT\nThanks To Acil-PrankBots\nAnd My Inex Team",
                                    "wrap": True,
                                    "color": "#aaaaaa",
                                    "size": "xxs"
                                  }
                                ]
                              },
                              "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "spacer",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "button",
                                    "style": "primary",
                                    "color": "#10CF08",
                                    "action": {
                                      "type": "uri",
                                      "label": "MY CONATCT",
                                      "uri": "https://line.me/ti/p/"+me.getUserTicket().id
                                    }
                                  }
                                ]
                              }
                             }
                            }
                            me.sendFlex(R, data)
                        if PrankBotsData == Abouts["3"]:
                          if D in Owner or D in meM:
                            me.reissueUserTicket()
                            My_Id = me.profile.displayName + "My id Line: http://line.me/ti/p/" + me.getUserTicket().id
                            me.sendMessage(R,My_Id)
                        if PrankBotsData == Abouts["4"]:
                          if D in Owner or D in meM:
                            me.leaveGroup(R)
                        if PrankBotsData == Abouts["5"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            cu = me.getProfileCoverURL(D)          
                            path = str(cu)
                            me.sendImageWithURL(R, path)
                        if PrankBotsData == Abouts["6"]:
                          if D in Owner or D in meM:
                            result = requests.get("http://jadwalnonton.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "_______CINEMA______\nType : Movie List Today\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            me.sendMessage(R, str(hasil))
                        if PrankBotsData == Abouts["7"]:
                          if D in Owner or D in meM:
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get('http://api-1cak.herokuapp.com/random')
                                data = r.text
                                data = json.loads(data)
                                img = data["img"]
                                me.sendMessage(R,"━═| Daftar cakcak |═━\n━═| Title: %s\n━═| Link: %s\n━═| Id: %s\n━═| Votes: %s\n━═| NSFW: %s\n━═| [ Finish ] |═━" %(str(data["title"].replace('FACEBOOK Comments', ' ')), str(data["url"]), str(data["id"]), str(data["votes"]), str(data["nsfw"])))
                        if PrankBotsData.startswith(Abouts["8"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            kata = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                try:
                                    r = web.get("https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search={}".format(urllib.parse.quote(kata)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "━═Bokep inimah"
                                    no = 1
                                    anu = data["videos"]
                                    if len(anu) >= 20:
                                        for s in range(20):
                                            hmm = anu[s]
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    else:
                                        for s in anu:
                                            hmm = s
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    me.sendMessage(R, str(ret_))
                                except:
                                    me.sendMessage(R, "Tidak ditemukan")
                        if PrankBotsData.startswith(Abouts["9"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            title = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get("http://www.omdbapi.com/?t="+title+"&y=&plot=full&apikey=4bdd1d70")
                                data=r.text
                                data=json.loads(data)
                                hasil = "╭━━═════[ Hasil pencarian film]"
                                hasil += "\nInformasi ━═| " +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                                hasil += "\nPlot ━═| " +str(data["Plot"])
                                hasil += "\nDirector ━═| " +str(data["Director"])
                                hasil += "\nActors ━═| " +str(data["Actors"])
                                hasil += "\nRelease ━═| " +str(data["Released"])
                                hasil += "\nGenre ━═| " +str(data["Genre"])
                                hasil += "\nTimer ━═| " +str(data["Runtime"])
                                img = data["Poster"]
                                me.sendImageWithURL(R,img)
                                me.sendMessage(R,hasil)
                        if PrankBotsData.startswith(Abouts["10"]):
                          if D in Owner or D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = me.getContact(key1)
                            me.findAndAddContactsByMid(key1)
                            me.sendMessage(R, "teman di tambahkan")
                        if PrankBotsData == Abouts["11"]:
                          if D in Owner or D in meM:
                            me.sendMessage(R, "Selesai.!!")
                            PrankBots["Conection"] = R
                            Run_Xp()
                        if PrankBotsData.startswith(Abouts["12"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            txt = teks.split("/")
                            bag1 = txt[0]
                            bag2 = txt[1]
                            bag3 = txt[2]
                            angka = ["1","2","3","4","5"]
                            latar = random.choice(angka)
                            nomor = ["1","2","3","4"]
                            background = random.choice(nomor)
                            url = "https://ari-api.herokuapp.com/retro?bg="+latar+"&txt="+background+"&text1="+bag1+"&text2="+bag2+"&text3="+bag3
                            me.sendImageWithURL(R, url)
                        if PrankBotsData.startswith(Abouts["13"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            url = "https://ari-api.herokuapp.com/led?text="+teks+"&sign=PB"
                            me.sendImageWithURL(R, url)
                        if PrankBotsData == Abouts["14"]:
                          if D in Owner or D in meM:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            me.sendMessage(R, "━━━━━╦RUNTIME BOTS╦━━━━━\n ┣━╦[ {}".format(str(runtime)))
                        if PrankBotsData == Abouts["15"]:
                          if D in Owner or D in meM:
                            start = time.time()
                            me.sendMessage(R, "gooo...")
                            elapsed_time = time.time() - start
                            warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                            warnanya1 = random.choice(warna1)
                            data = {
                                "type": "flex",
                                "altText": "LARIIII YANG KUENCENG WOY..",
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": str(elapsed_time),
                                                "wrap": True,
                                                "color": warnanya1,
                                                "align": "center"
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [{
                                           "type": "spacer",
                                            "size": "sm",
                                        }],
                                        "flex": 0
                                    }
                                }
                            }
                            me.sendFlex(R, data)
                        if PrankBotsData == Abouts["16"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendMessage(R,h.mid)
                        if PrankBotsData == Abouts["17"]:
                          if D in Owner or D in meM:
                            contact = me.getContact(D)
                            cover = me.getProfileCoverURL(D)
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : {}".format(contact.displayName)
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            me.sendMessage(R, str(result))
                            try:
                              poto = "https://os.line.naver.jp/os/p/{}".format(D)
                            except:
                              poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                            dax = {
                              "type": "template",
                              "altText": "MENCRET BAE",
                              "template": {
                                "type": "image_carousel",
                                "columns": [
                                  {
                                    "imageUrl": poto,
                                    "layout": "horizontal",
                                    "action": {
                                      "type": "uri",
                                      "label": "PROFILE",
                                      "uri": poto,
                                      "area": {
                                        "x": 447,
                                        "y": 356,
                                        "width": 1040,
                                        "height": 1040
                                      }
                                    }
                                  },
                                  {
                                    "imageUrl": cover,
                                    "layout": "horizontal",
                                    "action": {
                                      "type": "uri",
                                      "label": "COVER",
                                      "uri": cover,
                                      "area": {
                                        "x": 447,
                                        "y": 356,
                                        "width": 1040,
                                        "height": 1040
                                      }
                                    }
                                  },
                                  {
                                    "imageUrl": "https://qr-official.line.me/L/"+me.getUserTicket().id+".png",
                                    "layout": "horizontal",
                                    "action": {
                                      "type": "uri",
                                      "label": "CONTACT QR",
                                      "uri": "https://line.me/ti/p/"+me.getUserTicket().id,
                                      "area": {
                                        "x": 447,
                                        "y": 356,
                                        "width": 1040,
                                        "height": 1040
                                      }
                                    }
                                  }
                                ]
                              }
                            }
                            me.sendFlex(R, dax)
                        if PrankBotsData == Abouts["18"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendVideoWithURL(R,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                        if PrankBotsData.startswith(Abouts["19"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                me.sendMessage(R, str(ret_))
                        if PrankBotsData.startswith(Abouts["20"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus
                                    me.sendImageWithURL(R, str(path))
                        if PrankBotsData.startswith(Abouts["21"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus + "/vp"
                                    me.sendVideoWithURL(R, str(path))
                        if PrankBotsData.startswith(Abouts["22"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Namanya\n{}".format(str(contact.displayName)))
                        if PrankBotsData.startswith(Abouts["23"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Status kontak\n\n{}".format(str(contact.statusMessage)))
                        if PrankBotsData.startswith(Abouts["24"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    mi_d = contact.mid
                                    me.sendContact(R, mi_d)
                        if PrankBotsData.startswith(Abouts["25"]):
                          if D in Owner or D in meM:
                            me.sendMessage(R, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                me.sendMessage(R, str(ret_))
                        if PrankBotsData.startswith(Abouts["26"]):
                          if D in Owner or D in meM:
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━═════[INEXBOTS]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                        if PrankBotsData.startswith(Abouts["27"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(PrankBots["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                me.sendImageWithURL(R, text1[0])
                                me.sendMessage(R, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")
                        if PrankBotsData.startswith(Abouts["28"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            me.sendMessage(R, "ini id smulenya kak\n" + smule)
                        if PrankBotsData == Abouts["29"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                members = [mem.mid for mem in group.members]
                                me.acquireGroupCallRoute(R)
                                me.inviteIntoGroupCall(R, contactIds=members)
                                me.sendMessage(R, "Berhasil")
                        if PrankBotsData.startswith(Abouts["30"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'id'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("hasil.mp3")
                            me.sendAudio(R,"hasil.mp3")
                        if PrankBotsData.startswith(Abouts["31"]):
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                X = me.getGroup(R)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                me.updateGroup(X)
                        if PrankBotsData == Abouts["32"]:
                          if D in Owner or D in meM:
                            me.removeAllMessages(opps2)
                            me.sendMessage(R, "Chat deleted")
                        if PrankBotsData.startswith(Abouts["33"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            pesan = text.replace(sep[0] + " ","")
                            saya = me.getGroupIdsJoined()
                            for group in saya:
                                #me.sendMessage(group,str(pesan))
                                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                warnanya1 = random.choice(warna1)
                                data = {
                                    "type": "flex",
                                    "altText": "{} JANDAKU KETIKUNG ".format(meProfile.displayName),
                                    "contents": {
                                     "type": "bubble",
                                     "styles": {
                                       "header": {
                                         "backgroundColor": "#333300",
                                       },
                                       "body": {
                                         "backgroundColor": "#333333",
                                         "separator": True,
                                         "separatorColor": "#ffffff"
                                       },
                                       "footer": {
                                         "backgroundColor": "#333333",
                                         "separator": True
                                       }
                                     },
                                     "header": {
                                       "type": "box",
                                       "layout": "horizontal",
                                       "contents": [
                                         {
                                           "type": "text",
                                           "text": "🄱🅁🄾🄰🄳🄲🄰🅂🅃",
                                           "weight": "bold",
                                           "color": warnanya1,
                                           "size": "xxl"
                                         }
                                       ]
                                     },
                                     "hero": {
                                       "type": "image",
                                       "url": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51835843_2326067974083979_5266191763927728128_o.jpg?_nc_cat=108&efg=eyJpIjoiYiJ9&_nc_eui2=AeFDU4lcYDFco8MPKFdjadDZwGM-OaoU1OpdoEy5tbG_pgtK7-Qi0FKAnO5XYb0n84IH8UT1COwUMMZQtL6MZqzsB5nU9xrCFuWJwMS292zLew&_nc_ht=scontent.fcgk8-1.fna&oh=f61bcac07ab57951b99ce7dae80d6fe1&oe=5D215241",
                                       "size": "full",
                                       "aspectRatio": "3:4",
                                       "aspectMode": "cover",
                                       "action": {
                                         "type": "uri",
                                         "uri": "https://line.me/ti/p/~denjaka_inex"
                                       }
                                     },
                                         "type": "bubble",
                                         "body": {
                                             "type": "box",
                                             "layout": "horizontal",
                                             "contents": [
                                                 {
                                                     "type": "text",
                                                     "text": str(text),
                                                     "wrap": True,
                                                     "color": warnanya1,
                                                     "align": "center"
                                                 }
                                             ]
                                         },
                                         "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [{
                                                "type": "button",
                                                "style": "primary",
                                                "color": warnanya1,
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ADD MY LINE",
                                                    "uri": "https://line.me/ti/p/"+me.getUserTicket().id
                                                    }													
                                                },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }],
                                            "flex": 0
                                        }
                                    }
                                }
                                me.sendFlex(group, data)
                        if PrankBotsData == Abouts["34"]:
                          if D in Owner or D in meM:
                            groups = me.groups
                            ret_ = "╭━━━━━══[ Group List ]══━━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = me.getGroup(gid)
                                ret_ += "\n {}. {}  Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]══━━━━━".format(str(len(groups)))
                            warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                            warnanya1 = random.choice(warna1)
                            data = {
                                "type": "flex",
                                "altText": "{} JANDAKU DI CULIK ".format(meProfile.displayName),
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": str(ret_),
                                                "wrap": True,
                                                "color": "#47E1E5",
                                                "align": "center"
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [{
                                            "type": "button",
                                            "style": "link",
                                            "height": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "ADD MY LINE",
                                                "uri": "Http://line.me/ti/p/~denjaka_inex"
                                                }													
                                            },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }],
                                        "flex": 0
                                    }
                                }
                            }
                            me.sendFlex(R, data)
                        if PrankBotsData == Abouts["35"]:
                          if D in Owner or D in meM:
                            contactlist = me.getAllContactIds()
                            kontak = me.getContacts(contactlist)
                            num=1
                            msgs="╭━━━━━══[ Friend List ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Friend Result ]══━━━━━\nTotal : %i" % len(kontak)
                            me.sendMessage(R, msgs)
                        if PrankBotsData == Abouts["36"]:
                          if D in Owner or D in meM:
                            blockedlist = me.getBlockedContactIds()
                            kontak = me.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━━══[ Friend Block ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Block Result ]══━━━━━\nBlock Total : %i" % len(kontak)
                            me.sendMessage(R, msgs)
                        if PrankBotsData == Abouts["37"]:
                          if D in Owner or D in meM:
                            me.sendMessage(R, "━━━━══[Pembuat Grup]══━━━━")
                            group = me.getGroup(R)
                            GS = group.creator.mid
                            me.sendContact(R, GS)
                            me.sendMessage(R, "━━━━══━━╩━━══━━━━")
                        if PrankBotsData == Abouts["38"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                    warnanya1 = random.choice(warna1)
                                    data = {
                                        "type": "flex",
                                        "altText": "{} JANDA KEPELESET ".format(meProfile.displayName),
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": str(ret_),
                                                        "wrap": True,
                                                        "color": warnanya1,
                                                        "align": "center"
                                                    }
                                                ]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                "contents": [{
                                                    "type": "button",
                                                    "style": "link",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "ADD MY LINE",
                                                        "uri": "Http://line.me/ti/p/~denjaka_inex"
                                                        }													
                                                    },
                                                {
                                                    "type": "spacer",
                                                    "size": "sm",
                                                }],
                                                "flex": 0
                                            }
                                        }
                                    }
                                    me.sendFlex(R, data)
                        if PrankBotsData == Abouts["39"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        me.sendMessage(R, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                        warnanya1 = random.choice(warna1)
                                        data = {
                                            "type": "flex",
                                            "altText": "{} PENDUSTA ".format(meProfile.displayName),
                                            "contents": {
                                                "type": "bubble",
                                                "body": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": str(ret_),
                                                            "wrap": True,
                                                            "color": warnanya1,
                                                            "align": "center"
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [{
                                                        "type": "button",
                                                        "style": "link",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "ADD MY LINE",
                                                            "uri": "Http://line.me/ti/p/~denjaka_inex"
                                                            }													
                                                        },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }],
                                                    "flex": 0
                                                }
                                            }
                                        }
                                        me.sendFlex(R, data)
                        if PrankBotsData == Abouts["40"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                group = me.getGroup(R)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "SUDAH PUSKUN ORANGNYA"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://me.me/R/ti/g/{}".format(str(me.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭━━══[ Group Info ]══━━"
                                ret_ += "\n Nama Group : {}".format(str(group.name))
                                ret_ += "\nID Group : {}".format(group.id)
                                ret_ += "\n Pembuat : {}".format(str(gCreator))
                                ret_ += "\n Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n Jumlah Pending : {}".format(gPending)
                                ret_ += "\n═━━━Kode Qr/Link━━━═"
                                ret_ += "\n Group Ticket : {}".format(gTicket)
                                ret_ += "\n Group Qr : {}".format(gQr)
                                ret_ += "\n╰━━══[ INEXBOT]══━━"
                                me.sendImageWithURL(R, path)
                                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                warnanya1 = random.choice(warna1)
                                data = {
                                    "type": "flex",
                                    "altText": "{} MEMBAGIKAN SEMBAKO ".format(meProfile.displayName),
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": str(ret_),
                                                    "wrap": True,
                                                    "color": warnanya1,
                                                    "align": "center"
                                                }
                                            ]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [{
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "color": "#10CF08",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ADD MY LINE",
                                                    "uri": "Http://line.me/ti/p/~denjaka_inex"
                                                    }													
                                                },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }],
                                            "flex": 0
                                        }
                                    }
                                }
                                me.sendFlex(R, data)
                        if PrankBotsData == Abouts["41"]:
                          if D in Owner or D in meM:
                            group = me.getGroup(R)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            me.sendImageWithURL(R, path)
                        if PrankBotsData == Abouts["42"]:
                          if D in Owner or D in meM:
                            gid = me.getGroup(R)
                            me.sendMessage(R, "Name group\n" + gid.name)
                        if PrankBotsData == Abouts["43"]:
                          if D in Owner or D in meM:
                            gid = me.getGroup(R)
                            me.sendMessage(R,gid.id)
                        if PrankBotsData == Abouts["44"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    ticket = me.reissueGroupTicket(R)
                                    me.sendMessage(R, "https://me.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "https://me.me/R/ti/g/{}".format(str(ticket)))
                        if PrankBotsData == Abouts["45"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    me.sendMessage(R, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil membuka Qr")
                        if PrankBotsData == Abouts["46"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == True:
                                    me.sendMessage(R, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil menutup Qr")
                        if PrankBotsData == Abouts["47"]:
                          if D in Owner or D in meM:
                            PrankBots["Add"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["48"]:
                          if D in Owner or D in meM:
                            PrankBots["Add"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["49"]:
                          if D in Owner or D in meM:
                            PrankBots["Join"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["50"]:
                          if D in Owner or D in meM:
                            PrankBots["Join"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["51"]:
                          if D in Owner or D in meM:
                            PrankBots["Read"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["52"]:
                          if D in Owner or D in meM:
                            PrankBots["Read"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["53"]:
                          if PrankBots["Unsend"] == True:
                            if D in Owner or D in meM:
                              PrankBots["Unsend"] = True
                              me.sendMessage(R, "Already Unsend on")
                        if PrankBotsData == Abouts["54"]:
                          if PrankBots["Unsend"] == False:
                            if D in Owner or D in meM:
                              PrankBots["Unsend"] = False
                              me.sendMessage(R, "Already Unsend off")
                        if PrankBotsData == Abouts["55"]:
                          if D in Owner or D in meM:
                            PrankBots["Wc"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["56"]:
                          if D in Owner or D in meM:
                            PrankBots["Wc"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["57"]:
                          if D in Owner or D in meM:
                            PrankBots["Shared"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["58"]:
                          if D in Owner or D in meM:
                            PrankBots["Shared"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["59"]:
                          if D in Owner or D in meM:
                            PrankBots["Respon"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["60"]:
                          if D in Owner or D in meM:
                            PrankBots["Respon"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["70"]:
                          if D in Owner or D in meM:
                            PrankBots["Respontag"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["71"]:
                          if D in Owner or D in meM:
                            PrankBots["Respontag"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["61"]:
                          if D in Owner or D in meM:
                                try:
                                    del Sid['Red'][R]
                                    del Sid['Reason'][R]
                                    del Sid['Tar'][R]
                                except:
                                    pass
                                Sid['Red'][R] = Id
                                Sid['Reason'][R] = ""
                                Sid['Tar'][R]=True
                                me.sendMessage(R, "inex")
                        if PrankBotsData == Abouts["62"]:
                          if D in Owner or D in meM:
                            if R in Sid['Red']:
                                Sid['Tar'][R]=False
                                me.sendMessage(R, "Daftar yang terlihat\n"+Sid['Reason'][msg.to])
                                me.sendMessage(R, "Already off")
                            else:
                                me.sendMessage(R, "aktifkan dulu coy sidernya")
                        if PrankBotsData == Abouts["63"]:
                         if D in Owner or D in meM:
                          group = me.getGroup(R)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          ket_ = "╔━━══[ Member List ]══━━╗"
                          no = 0 + 1
                          for mem in group.members:
                            ket_ += "\n {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                          ket_ += "\n╚━━══[ Total {} member]══━━╝".format(str(len(group.members)))
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "╔━━═══════════════━━╗\n┣✯͜͡❂ MENTION MEMBER\n╚━━═══════════════━━╝\n╔━━═══════════════━━╗"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n┣✯͜͡❂ @!".format(str(no))
                                  ret_ += "\n┣━━═══════════════━━╝\n┣✯͜͡❂ TOTAL {} MEMBER\n╚━━═══════════════━━╝".format(str(len(dataMid)))
                                  sendMeention(R, ret_, dataMid)
                                  warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                  warnanya1 = random.choice(warna1)
                                  data = {
                                      "type": "flex",
                                      "altText": "{} MEMBAGIKAN SEMPAK BOLONG ".format(meProfile.displayName),
                                      "contents": {
                                          "type": "bubble",
                                          "body": {
                                              "type": "box",
                                              "layout": "horizontal",
                                              "contents": [
                                                {
                                                    "type": "text",
                                                    "text": str(ket_),
                                                    "wrap": True,
                                                    "color": warnanya1,
                                                    "align": "center"
                                                }
                                            ]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [{
                                                "type": "button",
                                                "style": "primary",
                                                "height": "sm",
                                                "color": "#C82EF8",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ADD MY LINE",
                                                    "uri": "Http://line.me/ti/p/~denjaka_inex"
                                                    }													
                                                },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }],
                                            "flex": 0
                                          }
                                      }
                                  }
                                  me.sendFlex(R, data)
                          except Exception as Ewe:
                              print(Ewe)
                        if PrankBotsData == Abouts["64"]:
                          if D in Owner or D in meM:
                            try:
                                PrankBots["Shared"] = True
                                PrankBots["Add"] = True
                                PrankBots["Join"] = True
                                PrankBots["Wc"] = True
                                PrankBots["Read"] = True
                                PrankBots["Unsend"] = True
                            except:me.sendMessage(R,"SETTING ALL IN ONLINE")
                        if PrankBotsData == Abouts["65"]:
                          if D in Owner or D in meM:
                            try:
                                PrankBots["Shared"] = False
                                PrankBots["Add"] = False
                                PrankBots["Join"] = False
                                PrankBots["Wc"] = False
                                PrankBots["Read"] = False
                                PrankBots["Unsend"] = False
                            except:me.sendMessage(R,"SETTING ALL IN OFFLINE")
                        if PrankBotsData == Abouts["66"]:
                          if D in Owner or D in meM:
                            RunTheRun(R, D, "[_______[RESULT]______]\n")
                            """
                            BOT WAR
                            VERSION : INEXBOTS
                            REVISION : VPS
                            """
                        if PrankBotsData == Abouts["67"]:
                          if D in Owner or D in meM:
                            me.sendFlex(R, plate["pricelist"])
                        if PrankBotsData == Abouts["68"]:
                          if D in Owner or D in meM:
                            me.sendFlex(R, plate["listapp1"])
                            me.sendFlex(R, plate["listapp2"])
                        if PrankBotsData == Abouts["69"]:
                          if D in Owner or D in meM:
                            me.sendFlex(R, plate["help"])
                        if PrankBotsData.startswith("pictlab "):
                          separate = text.split(" ")
                          teks = text.replace(separate[0] + " ","")
                          url1 = "https://memegen.link/buzz/"+teks+".jpg"
                          url2 = "https://memegen.link/joker/"+teks+".jpg"
                          url3 = "https://memegen.link/cbg/"+teks+".jpg"
                          url4 = "https://memegen.link/fry/"+teks+".jpg"
                          url5 = "https://memegen.link/yuno/"+teks+".jpg"
                          url6 = "https://memegen.link/fa/"+teks+".jpg"
                          url7 = "https://memegen.link/iw/"+teks+".jpg"
                          url8 = "https://memegen.link/blb/"+teks+".jpg"
                          url9 = "https://memegen.link/doge/"+teks+".jpg"
                          url10 = "https://memegen.link/firsttry/"+teks+".jpg"
                          data = {
                            "type": "template",
                            "altText": "SendgifPicture",
                            "template": {
                              "type": "image_carousel",
                              "columns": [
                                {
                                  "imageUrl": url1,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url2,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url3,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url4,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url5,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url6,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url7,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url8,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url9,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                },
                                {
                                  "imageUrl": url10,
                                  "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~denjaka_inex",
                                    "area": {
                                      "x": 447,
                                      "y": 356,
                                      "width": 1040,
                                      "height": 1040
                                    }
                                  }
                                }
                              ]
                            }
                          }
                          me.sendFlex(R, data)
        if rank.type == 25:
          """
          BOT WAR
          VERSION : INEXBOTS
          REVISION : VPS
          """
          if PrankBots["bot"] == True:
            war = rank.message
            Warstart = war.text
            Id = war.id
            R = war.to
            D = war._from
            if Warstart == "Helpwar" or Warstart == "helpwar":
                #me.sendMessage(R, str(warKey))
                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                warnanya1 = random.choice(warna1)
                data = {
                    "type": "flex",
                    "altText": " JANGAN BUNUH AKU ",
                    "contents": {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": str(warKey),
                                    "wrap": True,
                                    "color": warnanya1,
                                    "align": "center"
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [{
                                "type": "button",
                                "style": "primary",
                                "height": "sm",
                                "color": "#10CF08",
                                "action": {
                                    "type": "uri",
                                    "label": "CLICK HERE",
                                    "uri": "http://line.me/ti/p/~denjaka_inex"
                                    }													
                                },
                            {
                                "type": "spacer",
                                "size": "sm",
                            }],
                             "flex": 0
                        }
                    }
                }
                me.sendFlex(R, data)
            if Warstart == "Helpbot" or Warstart == "helpbot":
                #me.sendMessage(R, str(helpBot))
                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                warnanya1 = random.choice(warna1)
                data = {
                    "type": "flex",
                    "altText": " JANGAN BUNUH AKU ",
                    "contents": {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": str(helpBot),
                                    "wrap": True,
                                    "color": warnanya1,
                                    "align": "center"
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [{
                                "type": "button",
                                "style": "primary",
                                "height": "sm",
                                "color": "#10CF08",
                                "action": {
                                    "type": "uri",
                                    "label": "CLICK HERE",
                                    "uri": "http://line.me/ti/p/~denjaka_inex"
                                    }													
                                },
                            {
                                "type": "spacer",
                                "size": "sm",
                            }],
                             "flex": 0
                        }
                    }
                }
                me.sendFlex(R, data)
            if Warstart == "My bot" or Warstart == "mybot":
              if D in Owner or D in meM:
                try:
                    Musik2(R)
                except:Musik2(R)
            if Warstart == "Pro on":
              if D in Owner or D in meM:
                if R in PrankBots["PROTECT"]:
                    me.sendMessage(R,"Sudah on")
                    kk1.sendMessage(R,"Sudah on")
                    kk2.sendMessage(R,"Sudah on")
                    kk3.sendMessage(R,"Sudah on")
                    kk4.sendMessage(R,"Sudah on")
                    kk5.sendMessage(R,"Sudah on")
                else:
                    PrankBots["PROTECT"][R] = True
                    me.sendMessage(R,"Already on..")
                    kk1.sendMessage(R,"Already on..")
                    kk2.sendMessage(R,"Already on")
                    kk3.sendMessage(R,"Already on")
                    kk4.sendMessage(R,"Already on")
                    kk5.sendMessage(R,"Already on")                    
            if Warstart == "Pro off":
              if D in Owner or D in meM:
                if R in PrankBots["PROTECT"]:
                    me.sendMessage(R,"Already off")
                    kk1.sendMessage(R,"Already off")
                    kk2.sendMessage(R,"Already off")
                    kk3.sendMessage(R,"Already off")
                    kk4.sendMessage(R,"Already off")
                    kk5.sendMessage(R,"Already off")
                    del PrankBots["PROTECT"][R]
                else:
                    me.sendMessage(R,"Belum di protect")
                    kk1.sendMessage(R,"ok siap di protect")
                    kk2.sendMessage(R,"ok siap di protect")
                    kk3.sendMessage(R,"ok siap di protect")
                    kk4.sendMessage(R,"ok siap di protect")
                    kk5.sendMessage(R,"ok siap di protect")
            if Warstart == "Banlist":
                if D in Owner or D in meM:
                    thanks = ""
                    a = 0
                    Ban = PrankBots["blacklist"]
                    for Crott in Ban:
                        a = a + 1
                        end = '\n'
                        thanks += "\n┣|" + str(a) + ". " +me.getContact(Crott).displayName
                    me.sendMessage(R, "━━━━━[daftar blacklist]━━━━━━"+thanks+"\n┣━━━━★ɪɴᴇxʙᴏᴛs★━━━━━\nTOTAL ADA %s BLACKLIST" %(str(len(PrankBots["blacklist"]))))
            if Warstart == "Delban":
                if D in Owner or D in meM:
                    PrankBots["blacklist"] = {}
                    me.sendMessage(R, "delete blacklist success.!!")
                    kk1.sendMessage(R, "success.!!")
                    kk2.sendMessage(R, "success.!!")
                    kk3.sendMessage(R, "success.!!")
                    kk4.sendMessage(R, "success.!!")
                    kk5.sendMessage(R, "success.!!")
                    kk6.sendMessage(R, "success.!!")
            if Warstart == "Memberpict":
              kontak = me.getGroup(R)
              group = kontak.members
              picall = []
              for ids in group:
                if len(picall) >= 400:
                  pass
                else:
                  picall.append({
                    "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                    "action": {
                      "type": "uri",
                      "uri": "http://line.me/ti/p/~denjaka_inex"
                      }
                    }
                  )
              k = len(picall)//10
              for aa in range(k+1):
                data = {
                  "type": "template",
                  "altText": "{} Membagikan janda geratis".format(meProfile.displayName),
                  "template": {
                    "type": "image_carousel",
                    "columns": picall[aa*10 : (aa+1)*10]
                  }
                }
                me.sendFlex(R, data)
            if Warstart == "r1 cek" or Warstart == "R1 cek":
                if D in Owner or D in meM:
                    me.sendMessage(R,"Autorespon anda:\n\n"+respontags["Auto_text"])
            if Warstart.startswith("R1 set: "):
                if D in Owner or D in meM:
                    respontags["Auto_text"] = msg.text.replace("R1 set: ","")
                    me.sendMessage(R,"Autorespon di ubah menjadi: "+respontags["Auto_text"])
            if Warstart == "Clearban" or Warstart == "Dellban":
                me.sendMessage(R, "Berhasil menghapus {} user blacklist".format(str(len(PrankBots["blacklist"]))))
                PrankBots["blacklist"] = {}
            if Warstart == "Ping" or Warstart == "Respon":
                try:
                    Musik1(R)
                except:Musik1(R)
                #kk1.sendMessage(to, None, contentMetadata={"STKID":"52002759","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                #kk2.sendMessage(to, None, contentMetadata={"STKID":"52114146","STKPKGID":"11539","STKVER":"1"}, contentType=7)
                #kk3.sendMessage(to, None, contentMetadata={"STKID":"52002752","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                #kk4.sendMessage(to, None, contentMetadata={"STKID":"52002739","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                #kk5.sendMessage(to, None, contentMetadata={"STKID":"52002734","STKPKGID":"11537","STKVER":"1"}, contentType=7)
            if Warstart == "Kibar" or Warstart == "kibar":
                kk1.sendMessage(R, "ASSALAMUALAIKUM \nHALLOOO!!! \nSORRY ROOM KALIAN \nKEBANYAKAN ANU\nINEXTEAM DATANG\nMAU SAPU ROOM GJ\nNO COMEND \nNO BAPER \nNO BACOT \nNO DESAH \nNO SPONSOR \nNO HATTERS\nROOM OKEP \nROOM JUDI\nROOM GAJELAS\nSIAP KAMI BANTAII \n\n\n\nFUCK YOU...\nKENAPE LU PADA DIEM\nTANGKIS SU JANGAN CUMA NYIMAK\n\n\nDASAR ROOM PEA KAGAK JELAS\nSORRY BOS!!!\nGC LU MAU GUA SITA...!!!\n\n\n SALAM DARI KAMI\n🅸🅽🅴🆇🅱🅾🆃🆂\n\nHADIR DI ROOM ANDA\n\nRATA GAK RATA YANG PENTING KIBAR \nRATA KAMI SENANG\nGAKRATA TUNGGU KEDATANGAN KAMI LAGI\n\n\n   SLAM KILERR\n🅸🅽🅴🆇🅱🅾🆃🆂 \n\n\nCREATOR\n\n\nhttps://line.me/R/ti/p/%40bvb1195k\nhttp://line.me/ti/p/~denjaka_inex")
                kk1.sendMessage(R, kk1Profile.displayName)
                kk1.sendContact(R,kk1Rank)
                kk2.sendMessage(R, kk2Profile.displayName)
                kk2.sendContact(R,kk2Rank)
                kk3.sendMessage(R, kk3Profile.displayName)
                kk3.sendContact(R,kk3Rank)
                kk4.sendMessage(R, kk4Profile.displayName)
                kk4.sendContact(R,kk4Rank)
                kk5.sendMessage(R, kk5Profile.displayName)
                kk5.sendContact(R,kk5Rank)
                kk6.sendMessage(R, kk6Profile.displayName)
                kk6.sendContact(R,kk6Rank)
                jss.sendMessage(R, jssProfile.displayName)
                jss.sendContact(R,jssRank)
                kk1.sendMessage(R, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                kk6.sendMessage(R, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                me.sendMessage(R, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                me.sendMessage(R, "Bakar roomnya")
            if Warstart == "Sp" or Warstart == "sp":
                start = time.time()
                me.sendMessage(R, "Ngacirrrr wooyyy...")
                tes = time.time() - start
                me.sendMessage(R, "{}".format(str(tes)))
                start = time.time()
                kk1.sendMessage(R, "......")
                tes = time.time() - start
                kk1.sendMessage(R, "{}".format(str(tes)))
                start = time.time()
                kk2.sendMessage(R, "......")
                tes = time.time() - start
                kk2.sendMessage(R, "{}".format(str(tes)))
                start = time.time()
                kk3.sendMessage(R, "......")
                tes = time.time() - start
                kk3.sendMessage(R, "{}".format(str(tes)))
                start = time.time()
                kk4.sendMessage(R, "......")
                tes = time.time() - start
                kk4.sendMessage(R, "{}".format(str(tes)))
                start = time.time()
                kk5.sendMessage(R, "......")
                tes = time.time() - start
                kk5.sendMessage(R, "{}".format(str(tes)))
                start = time.time()
                kk6.sendMessage(R, "......")
                tes = time.time() - start
                kk6.sendMessage(R, "{}".format(str(tes)))
            if Warstart == "." or Warstart == "Masuk":
                try:
                    me.inviteIntoGroup(R, [kk1Rank,kk2Rank,kk3Rank,kk4Rank,kk5Rank,kk6Rank,jssRank])
                    kk1.acceptGroupInvitation(R)
                    kk2.acceptGroupInvitation(R)
                    kk3.acceptGroupInvitation(R)
                    kk4.acceptGroupInvitation(R)
                    kk5.acceptGroupInvitation(R)
                    kk6.acceptGroupInvitation(R)
                except:
                    try:
                        gg = me.getGroup(R)
                        gg.preventedJoinByTicket = False
                        me.updateGroup(gg)
                        grup = me.reissueGroupTicket(R)
                        kk1.acceptGroupInvitationByTicket(R, grup)
                        kk2.acceptGroupInvitationByTicket(R, grup)
                        kk3.acceptGroupInvitationByTicket(R, grup)
                        kk4.acceptGroupInvitationByTicket(R, grup)
                        kk5.acceptGroupInvitationByTicket(R, grup)
                        kk6.acceptGroupInvitationByTicket(R, grup)
                        gg.preventedJoinByTicket = True
                        me.updateGroup(gg)
                        kk5.inviteIntoGroup(R, [jssRank])
                    except:me.sendMessage(R, "BOT HARUS GANTI TOKEN")
            if Warstart == ".." or Warstart == "Stay":
                try:
                    me.inviteIntoGroup(R, [jssRank])
                except:
                    try:
                        gg = me.getGroup(R)
                        gg.preventedJoinByTicket = False
                        me.updateGroup(gg)
                        grup = me.reissueGroupTicket(R)
                        kk1.acceptGroupInvitationByTicket(R, grup)
                        kk1.inviteIntoGroup(R, [jssRank])
                        gg.preventedJoinByTicket = True
                        me.updateGroup(gg)
                        kk1.leaveGroup(R)
                    except:me.sendMessage(R, "BOT HARUS GANTI TOKEN")
            if Warstart == "G join" or Warstart == "Ghost in":
                try:
                    me.inviteIntoGroup(R, [jssRank])
                    jss.acceptGroupInvitation(R)
                except:
                    try:
                        gg = me.getGroup(R)
                        gg.preventedJoinByTicket = False
                        me.updateGroup(gg)
                        grup = me.reissueGroupTicket(R)
                        jss.acceptGroupInvitationByTicket(R, grup)
                        gg.preventedJoinByTicket = True
                        me.updateGroup(gg)
                    except:me.sendMessage(R, "BOT HARUS GANTI TOKEN")
            if Warstart == "Gas" or Warstart == "Hajar":
                try:
                    me.inviteIntoGroup(R, [kk1Rank,kk2Rank,kk3Rank,kk4Rank,kk5Rank,kk6Rank,jssRank])
                    kk1.acceptGroupInvitation(R)
                    kk2.acceptGroupInvitation(R)
                    kk3.acceptGroupInvitation(R)
                    kk4.acceptGroupInvitation(R)
                    kk5.acceptGroupInvitation(R)
                    kk6.acceptGroupInvitation(R)
                    jss.acceptGroupInvitation(R)
                except:
                    try:
                        gg = me.getGroup(R)
                        gg.preventedJoinByTicket = False
                        me.updateGroup(gg)
                        grup = me.reissueGroupTicket(R)
                        kk1.acceptGroupInvitationByTicket(R, grup)
                        kk1.sendContact(R,kk1Rank)
                        kk2.acceptGroupInvitationByTicket(R, grup)
                        kk2.sendContact(R,kk2Rank)
                        kk3.acceptGroupInvitationByTicket(R, grup)
                        kk3.sendContact(R,kk3Rank)
                        kk4.acceptGroupInvitationByTicket(R, grup)
                        kk4.sendContact(R,kk4Rank)
                        kk5.acceptGroupInvitationByTicket(R, grup)
                        kk5.sendContact(R,kk5Rank)
                        kk6.acceptGroupInvitationByTicket(R, grup)
                        kk6.sendContact(R,kk6Rank)
                        jss.acceptGroupInvitationByTicket(R, grup)
                        jss.sendContact(R,jssRank)
                        me.sendMessage(R, "Kibar")
                    except:
                        pass
            if Warstart == "G bye" or Warstart == "Ghost bye":
                try:
                    jss.leaveGroup(R)
                    gg = me.getGroup(R)
                    gg.preventedJoinByTicket = True
                    me.updateGroup(gg)
                    me.inviteIntoGroup(R, [jssRank])
                except:me.sendMessage(R, "SB LIMIT INVITE")
            if Warstart == "," or Warstart == "Keluar":
                try:
                    kk1.leaveGroup(R)
                    kk2.leaveGroup(R)
                    kk3.leaveGroup(R)
                    kk4.leaveGroup(R)
                    kk5.leaveGroup(R)
                    kk6.leaveGroup(R)
                    me.cancelGroupInvitation(R,[jssRank])
                except:me.sendMessage(R, None, contentMetadata={"STKID":"52002752","STKPKGID":"11537","STKVER":"1"}, contentType=7)
            if Warstart.startswith("Crot ") or Warstart.startswith("crot "):
              if D in Owner or D in meM:
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                  names = re.findall(r'@(\w+)', text)
                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                  mentionees = mention['MENTIONEES']
                  lists = []
                  for mention in mentionees:
                      if mention["M"] not in lists:
                          lists.append(mention["M"])
                  for ls in lists:
                      try:
                          berak = [kk1,kk2,kk3,kk4,kk5,kk6,jss]
                          berakin = random.choice(berak)
                          berakin.kickoutFromGroup(to,[ls])
                          print (to,[ls])
                      except:
                          pass
            if Warstart.startswith("Cipok ") or Warstart.startswith("cipok "):
              if D in Owner or D in meM:
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target not in BotWar:
                            try:
                                G = me.getGroup(R)
                                G.preventedJoinByTicket = False
                                me.updateGroup(G)
                                invsend = 0
                                Ticket = me.reissueGroupTicket(R)
                                jss.acceptGroupInvitationByTicket(R,Ticket)
                                jss.sendMessage(R,"Jangan macem-macem luh nyeet...")
                                jss.kickoutFromGroup(R, [target])
                                jss.leaveGroup(R)
                                me.inviteIntoGroup(R, [jssRank])
                                gg.preventedJoinByTicket = True
                                me.updateGroup(gg)
                            except:
                                pass
            if Warstart.startswith("Hajar") or Warstart.startswith("hajar"):
              if D in Owner or D in meM:
                  if msg.toType == 2:
                      print ("ok")
                      _name = msg.text.replace("Hajar","")
                      gs = me.getGroup(R)
                      gs = kk1.getGroup(R)
                      gs = kk2.getGroup(R)
                      gs = kk4.getGroup(R)
                      gs = kk4.getGroup(R)
                      gs = kk5.getGroup(R)
                      gs = kk6.getGroup(R)
                      gs = jss.getGroup(R)
                      targets = []
                      for g in gs.members:
                          if _name in g.displayName:
                              targets.append(g.mid)
                      if targets == []:
                          me.sendMessage(R,"Not Found")
                      else:
                          for target in targets:
                              if target not in Owner or target not in BotWar or target not in meM:
                                  try:
                                      klist=[me,kk1,kk2,kk3,kk4,kk5,kk6,jss]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(R,[target])
                                      print (R,[g.mid])
                                  except:
                                     pass
                          else:
                              me.sendMessage(R,"Member kosong.!!")

        if rank.type == 26:
          if PrankBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Id = msg.id
            R = msg.to
            D = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = D
                if msg.toType == 2:
                    to = R
                if PrankBots["Read"] == True:
                    me.sendChatChecked(R, Id)
                if msg.contentType == 0:
                    if text is None:
                        return
                if msg.contentType == 16:
                        if PrankBots["Shared"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = me.getContact(D)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://me.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://me.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                                traceback.print_tb(error.__traceback__)
                if msg.contentType == 0 and D not in meM and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if meM in mention["M"]:
                                if PrankBots["Respon"] == True:
                                    contact = me.getContact(D)
                                    path = "http://dl.profile.line.naver.jp/"+ contact.pictureStatus
                                    sendMention1(R, D, "\n",respontags1["Auto_text"])
                                break
        if rank.type == 13:
            print ("NOTIFIED MEMBER OR SELF JOIN GROUP")
            Gr = opps1
            if PrankBots["Join"] == True:
                me.acceptGroupInvitation(Gr)
            else:
                pass
        if rank.type == 5:
            print ("NOTIFIED ADD CONTACT SELF")
            if PrankBots["Add"] == True:
                me.findAndAddContactsByMid(opps1)
            sendMention(opps1, opps1, "Thanks For add Me ","")
            #====================================
#====================================
        if rank.type == 15:
            Gr = opps1
            Cj = opps2
            print ("NOTIFIED CONTACT MEMBER LEAVE TO GROUP")
            if PrankBots["Wc"] == True:
              if Cj in BotWar:
                pass
              else:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Good bye : {}".format(dia.displayName)
                ms += "In group : {}".format(Gc.name)
                mt = "Why your leave in group {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendMessage(dia,mt)
                me.sendContact(Gr,dia)
        if rank.type == 17:
            Gr = opps1
            Cj = opps2
            print ("NOTIFIED CONTACT MEMBER JOIN TO GROUP")
            if PrankBots["Wc"] == True:
              if Cj in BotWar:
                pass
              else:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Welcome : {}".format(dia.displayName)+" In group : {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendContact(Gr,dia)
        if rank.type == 65:
            print ("UNSEND MESSAGE UNSENDER FROM MY SELF")
            if PrankBots["Unsend"] == True:
                try:
                    at = opps1
                    msg_id = opps2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = me.getGroup(at)
                                ryan = me.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ɢᴀᴍʙᴀʀ ᴅɪʜᴀᴘᴜs  」\n• ❂➣ ᴘᴇɴɢɪʀɪᴍ : "
                                ret_ = "• ❂➣ ɴᴀᴍᴀ ɢʀᴜᴘ: {}".format(str(ginfo.name))
                                ret_ += "\n• ❂➣ ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nINEXBOTS"
                                ret_ += "\nCreator:\nline.me/ti/p/~denjaka_inex" 
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                me.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                me.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = me.getGroup(at)
                                ryan = me.getContact(msg_dict[msg_id]["from"])
                                ret_ =  " 「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs  」\n"
                                ret_ += "❂ ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n❂ ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n❂ ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n❂➣ᴘᴇsᴀɴɴʏᴀ : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n❂ TEAM :INEXBOTS ❂"
                                ret_ += "\nCreator:\nline.me/ti/p/~denjaka_inex" 
                                me.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
        if rank.type == 65:
            if PrankBots["Unsend"] == True:
                try:
                    at = opps1
                    msg_id = opps2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = me.getGroup(at)
                                ryan = me.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 STICKER DIHAPUS」\n"
                                ret_ += "➣ PENGIRIM : {}".format(str(ryan.displayName))
                                ret_ += "\n• NAMA GROUP : {}".format(str(ginfo.name))
                                ret_ += "\n• WAKTU MENGIRIM : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n❂ INEXBOTS ❂"
                                ret_ += "\nCreator:  line.me/ti/p/~denjaka_inex" 
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                me.sendMessage(at, str(ret_))
                                me.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if rank.type == 55:
            Gr = opps1
            try:
                if Sid['Tar'][Gr]==True: #cctv.cyduk
                        if Gr in Sid['Red']:   #cctv.poin
                            Name = me.getContact(opps2).displayName
                            Np = me.getContact(opps2).pictureStatus
                            #path = "http://dl.profile.line.naver.jp/"+ contact.pictureStatus 
                            if Name in Sid['Reason'][Gr]:  #cctv.reason
                                pass
                            else:
                                Sid['Reason'][Gr] += "\n||[ " + Name + " ]||"
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[0] + " " + "\nNah jangan ngintip mulu . . .\nGabung Chat yux ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[1] + " " + "\nJangan ngintip.. . . .\nMasuk  ayox... ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    me.sendMessage(Gr, "hallo.. " + " " + Name + " " + "\nJangan ngintip aja\nMasuk gabung chat ya... ")
                                    me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
    except Exception as error:
        ErrorX(error)
        if rank.type == 59:
            print(rank)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for rank in ops: 
          serviceX(rank)
          oepoll.setRevision(rank.revision)
    except Exception as e:
        me.log("RESPONSE: " + str(e))
