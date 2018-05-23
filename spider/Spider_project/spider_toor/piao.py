import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup
import json
import xlrd


headers = {
    'Cookie': 'UM_distinctid=162d9a5b8aaf44-04544743912b3c-17347840-1fa400-162d9a5b8accb0; CNZZDATA1261750666=473823165-1524064969-%7C1524064969; JSESSIONID=0001h5Ich9Tk1i-q5SLwuiPTy83:-Q4IFUA'
}


async def query(session):
    url = 'http://c.abatour.com/dataData.action?_={}&iscenicid=1&preDays=0&nextDays=90'.format(
        time.time())
    async with session.get(url) as response:
        return await response.text()


async def index(session):
    url = 'http://b.jowong.com/provider/ticket/index.do'
    async with session.get(url, headers=headers) as response:
        return await response.text()


def get_bznote(text):
    soup = BeautifulSoup(text, 'lxml')
    bznote = soup.find('input', {'name': 'bznote'})['value']
    return bznote


async def chooseTourists(session, bznote):
    url = 'http://b.jowong.com/team/chooseTourists.do?_={}&bznote={}&prno=06001128&cpxh=0008&seqs='.format(
        int(time.time()), bznote)
    async with session.get(url, headers=headers) as response:
        return await response.text()


def get_t(text):
    soup = BeautifulSoup(text, 'lxml')
    res = soup.find(id='dataTeamList').find(
        'li', class_='item')
    if res:
        return res.find('label').text.strip()
    else:
        return None


async def ticketBooking(session, t, date):
    url = 'http://b.jowong.com/provider/ticket/ticketBooking.do'
    data = {
        'selectNo': '',
        'objpdno': "%7Bpd06001:%7Bpd:'06001',c:'%E4%B9%9D%E5%AF%A8%E6%B2%9F',d:'{date}',pr:%5B%7Bc:'0600112802',m:'%E5%85%A8%E4%BB%B7%E5%A5%97%E7%A5%A8',e:200,n:1,v:'&01&1&0008&0008&',u:'%E4%BD%8D',t:'{t}',r:'06001128'%7D%5D%7D%7D".format(date=date, t=t),
        'prno': '06001128&0600112802&200&01&1&0008&0008&06001&{date}&{t}'.format(date=date, t=t),
        'numb0600112802': '1',
    }
    async with session.post(url, data=data, headers=headers) as response:
        return await response.text()


async def ticketInfo(session, t):
    url = 'http://b.jowong.com/provider/ticket/ticketInfo.do'
    data = {
        'pcno': '0',
        'viewtype': '0',
        '06001ornm': '郑程',
        '06001orzj': '01',
        '06001orhm': ' 513001198604200210',
        '06001orph': '13378119780',
        'numb0600112802': '1',
        'note0600112802': str(t),
        'prnoValue': '06001128',
        'isdx': '1',
        'tdlx': '01',
        'tdbz': '01',
        'dxnumber': '13378119780',
        'couid': 'CHN',
        'prvcode': '0103',
        'gatprvcode': '0069',
        'note': '',
        'strnote': ''
    }
    # 解析excel 写入到 data
    ExcelFile=xlrd.open_workbook('1.xls')
    table = ExcelFile.sheets()[0]
    nrows = table.nrows
    t = ["name","type","id","phone"]
    z = []
    for i in range(nrows):
        if i == 0:
            continue
        z.append(dict(zip(t,table.row_values(i))))

    for x in z:
        data["06001ornm"] = x["name"]
        data["dxnumber"] = x["phone"]
        data["06001orph"] = x["phone"]
        data["06001orhm"] = x["id"]
        async with session.post(url, data=data, headers=headers) as response:
            return await response.text()


def get_token(text):
    soup = BeautifulSoup(text, 'lxml')
    token = soup.find('input', {'name': 'org.apache.struts.taglib.html.TOKEN'})
    if token:
        return token['value']
    else:
        return None


async def ticketSave(session, token):
    url = 'http://b.jowong.com/provider/ticket/ticketSave.do'
    data = {
        'org.apache.struts.taglib.html.TOKEN': token
    }
    async with session.post(url, data=data, headers=headers) as response:
        return await response.text()


def none(date):
    print('{}无票，监测时间{}'.format(date, time.ctime(time.time())))

async def main():
    async with aiohttp.ClientSession() as session:
        bznote = get_bznote(await index(session))
        t = get_t(await chooseTourists(session, bznote))
        if not t:
            print('没有旅客信息')
            return
        data = json.loads((await query(session))[5:-1])['dateList']
        dateList = ['2018-05-21']
        #for item in data:
        #    if item['numberList'][0]['number'] < 2:
        #        dateList.append(item['date'])
        while True:
            data = json.loads((await query(session))[5:-1])['dateList']
            for item in data:
                if item['date'] not in dateList:
                    continue
                if item['numberList'][0]['number'] == 0:
                    none(item['date'])
                    continue
                await ticketBooking(session, t, item['date'])
                token = get_token(await ticketInfo(session, t))
                if not token:
                    none(item['date'])
                    continue
                res = await ticketSave(session, token)
                if '订单保存失败，请与系统管理员联系' in res:
                    none(item['date'])
                    continue
                else:
                    print(item['date'] + '抢到')
                    return
            time.sleep(1)


async def test():
    date = '2018-05-26'
    async with aiohttp.ClientSession() as session:
        bznote = get_bznote(await index(session))
        t = get_t(await chooseTourists(session, bznote))
        if not t:
            print('没有旅客信息')
            return
        await ticketBooking(session, t, date)
        token = get_token(await ticketInfo(session, t))
        if not token:
            none(date)
        res = await ticketSave(session, token)
        if '订单保存失败，请与系统管理员联系' in res:
            none(date)
        else:
            print(res, date + '抢到')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
