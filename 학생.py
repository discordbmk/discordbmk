import discord
import asyncio
import os
import pytz
import datetime
import openpyxl
import random

from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():

    print(client.user.name)
    print('ready')
    game = discord.Game('공부')
    ch = client.get_channel(875051214188998766)
    await ch.send("```학생 봇 실행됨.```")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    #자신 글에는 반응 안함
    if message.author == client.user:
        return

    #if message.author.id == 789530448346480640 or message.author.id == 873224043359260682:
    #    await message.delete()
    #    return

    #a는 받은 대화
    a = message.content

    # 대화 기록
    all = client.get_channel(875962193835876352)
    await all.send(f"=======\n{datetime.datetime.utcnow()}에 {message.author}님께서 채널 < {message.channel.name} > ```" + a + "``` 위와 같이 말씀 하셨습니다.\n=======")

    #a 길이 및 역할 그리고 동아리 가입 알림 채널 id
    n = len(a)
    k = client.get_channel(875796315437662259)

    #케피 글 삭제

    #서재민 발설 시 자동 삭제
    for i in range(0, n):
        if a[i] == "서" and a[i + 1] == "재" and a[i + 2] == "민" or a[i] == "재" and a[i + 1] == "민":
            await message.delete()
            return

    #선도부 id 변수
    sun = [842684781225050173, 875777083547197512, 875648611604635648, 789530448346480640]
    sun_n = 4

    if message.channel.id == 875777083547197512 and message.content == "!동아리":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f"동아리", description="", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00000)

        embed.add_field(name=f"<1>", value="자신이 원하는 동아리를 관리자에게 이유와 함께 제시하여 추가할 수 있습니다.", inline=False)
        embed.add_field(name=f"<2>", value="동아리 가입신청은 관리자 또는 그 동아리의 관리자(부장)에게 직접적으로 먼저 말하고 명령어를 입력후 가입할 수 있습니다.", inline=False)
        embed.add_field(name=f"<3>", value="동아리에 필요한건을 관리자가 어느정도 도움을 드릴 수 있습니다.", inline=False)
        embed.add_field(name=f"<4>", value="동아리 내에서의 모든 활동은 자유입니다.", inline=False)
        embed.add_field(name=f"<5>", value="동아리 활동중 동아리 주제와 관련없는 행동을 할때는 동아리 조원의 2/3이 찬성해야 합니다.", inline=False)

        await message.channel.send(embed=embed)

    if message.channel.id == 875777083547197512 and message.content == ":동아리":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f"동아리", description="", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00000)

        embed.add_field(name=f"선도부", value="스스로 서버의 규칙을 준수하고 학생들의 깨끗한 채팅문화를 적극적으로 선도한다.", inline=False)

        await message.channel.send(embed=embed)


    #선도부 명령어
    if message.content == "!선도부 가입":
        sund = 0
        for i in range(0, sun_n):
            if message.author.id == sun[i]:
                if message.content == "!선도부 가입" and message.channel.id == 875777083547197512:
                    await message.channel.send("잠시만 기다려 주십시오.")
                    await asyncio.sleep(5)
                    sund = 1
                    c = await message.author.create_dm()
                    await c.send("========\n안녕하세요. 저희 서버의 선도부에 가입해주셔서 진심으로 감사합니다.\n 선도부 생활 또는 다른 동아리 활동을 하면서 필요한 물품등은 관리자가 가능할 경우 지원해드릴 수 있습니다.")
                    await message.author.add_roles(get(message.author.guild.roles, name="선도부"))
                    await message.channel.send(f"{message.author}님 선도부에 가입하셨습니다.\n감사합니다.")
                    await k.send(f"{message.author}님이 선도부에 가입하였습니다.")
                    return
                if i == sun_n and sund == 0:
                    await message.channel.send("선도부 가입신청은 먼저 관리자와 1 : 1 상담을 해야합니다.")
                    return




    #관리자 명령어
    if message.content == "!신원" and message.author.id == 789530448346480640:
        await message.delete()
        ch = client.get_channel(875256812486660116)
        await ch.send("신원을 밝혀주셔야 저희의 서비스를 제공할 수 있습니다.\n이 채널에 여러분의 이름(3글자의 가명 또는 본명)적어주세요.\n생년월일은 사실대로 적어주셔야 합니다.\n여러분의 신원은 확인후 이 채널에서 삭제됩니다.\n개인 정보를 밝히고 싶지않다면 관리자에게 개인매시지 부탁드립니다.\nex : 홍길동 03년 01월 01일")

    #신원 확인
    if message.channel.id == 875256812486660116 and n == 15:
        if a[4] == "0" and a[5] == "3" or a[4] == "0" and a[5] == "4" or a[4] == "0" and a[5] == "5" or a[4] == "0" and a[5] == "6" or a[4] == "0" and a[5] == "7" or a[4] == "0" and a[5] == "8" or a[4] == "0" and a[5] == "9" or a[4] == "1" and a[5] == "0" or a[4] == "1" and a[5] == "1":
            if a[6] == "년" and a[10] == "월" and a[14] == "일":
                #g는 가진 역할 수
                g = len(message.author.roles)
                #역할을 받았는지 확인
                if g > 1:
                    await message.channel.send("당신의 신원은 이미 확인되었습니다.\n 문제가 있다면 관리자에게 개인메시지 부탁드립니다.")
                    return

                await message.author.add_roles(get(message.author.guild.roles, name=a[4]+a[5]))
                await message.channel.send(f"{message.author}님에게 " + a[4] + a[5] + "년생 권한이 부여되었습니다.")
                #10초 기다리기
                await asyncio.sleep(10)

                await message.delete()
                await message.channel.send(f"```{message.author}님의 생년월일은 신원이 확인되어 자동으로 삭제되었습니다.```")

                #가입 신청 알림채널에 알림
                await k.send(f"{message.author}님이" + a[4] + a[5] + "역할을 부여 받았습니다.")

                #개인메시지
                c = await message.author.create_dm()
                await c.send("========\n안녕하세요. 저희 서버에 가입을 해주셔서 감사합니다.\n저는 서버를 관리하고 있는 봇입니다.\n 이름은 김 성 실 이라고 합니다.\n\n저희 서버에 들어오시면 최소 5명의 친구를 이곳에 초대해주십시오.")
                dirctory = os.path.dirname(__file__)
                file = discord.File(dirctory + "\\학생증.png")
                await c.send(file=file)
                await c.send("회원님의 역학은 " + a[4] + a[5] + "년생 역할입니다.\n 이는 회원님이 " + a[4] + a[5] + "년생 전용 채널에서 이야기를 할 수 있는 권한이 생긴 겁니다.\n 궁금한 점은 관리자에게 직접적으로 DM을 주시면 됩니다.\n 관리자의 응답이 좀 늦을 수 있으니 양해부탁드립니다.\n감사합니다.")

            else:
                await message.channel.send("형식에 맞지 않습니다. \n ex : ### @@년 @@월 @@일\n띄워쓰기 해주셔야 합니다.")
        else:
            await message.channel.send("현재 저희 서버의 서비스를 이용할 수 없는 나이입니다.")
    elif message.channel.id == 875256812486660116 and n != 15:
        await message.channel.send("이곳을 오직 신분을 확인하기 위한 채널입니다. 또는 신분확인 예와 형식이 맞지 않습니다.")


    #학생 머니
    if message.channel.id == 876443162439221298:
        if message.content == "!회원가입":
            print(1)
            file = openpyxl.load_workbook("rem.xlsx")
            sheet = file.active
            for i in range(1, 71):
                if sheet["A" + str(i)].value == message.author.id:
                    await message.channel.send("이미 회원가입을 하셨습니다.")
                    return
                elif sheet["A" + str(i)].value == "NULL":
                    sheet["A" + str(i)].value = message.author.id
                    sheet["B" + str(i)].value = 5000
                    print(sheet["A" + str(i)].value)
                    print(sheet["B" + str(i)].value)
                    await message.channel.send("회원가입을 하셨습니다.\n기본 학생머니 5000원이 지급되었습니다.\n자세한 설명은 <!학생머니 설명>이라는 명령어 사용을 부탁드리겠습니다.")
                    file.save("rem.xlsx")
                    return

        if message.content == "!학생머니 설명":
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(title=f"학생머니", description="", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00000)

            embed.add_field(name=f"<1>", value=f"저희 서버에서 학생머니를 이용하여 유저들과 물건을 사고 팔 수있습니다.", inline=False)
            embed.add_field(name=f"<2>", value=f"다만 절대로 실제 금전적 가치를 가진물건을 학생머니를 이용하여 파는 것은 절대적으로 금하고 저희서버에서 책임지지 않습니다.", inline=False)
            embed.add_field(name=f"<3>", value=f"학생 머니로는 동아리 활동에서 이루어지는 게임, 또는 신분을 위해서 사용됩니다.", inline=False)
            embed.add_field(name=f"<4>", value=f"학생머니는 문제 또는 동아리 활동을 통해 관리자나 동아리 주장으로부터 직접적으로 학생머니를 지급받습니다.", inline=False)
            await message.channel.send(embed=embed)

        # 공정 머니
        if message.channel.id == 876450741370380359:
            if message.content == "!회원가입":
                print(2)
                file = openpyxl.load_workbook("rem1.xlsx")
                sheet = file.active
                for i in range(1, 71):
                    if sheet["A" + str(i)].value == message.author.id:
                        await message.channel.send("이미 회원가입을 하셨습니다.")
                        return
                    elif sheet["A" + str(i)].value == "NULL":
                        sheet["A" + str(i)].value = message.author.id
                        sheet["B" + str(i)].value = 0
                        print(sheet["A" + str(i)].value)
                        print(sheet["B" + str(i)].value)
                        await message.channel.send("회원가입을 하셨습니다.\n자세한 설명은 <!공정머니 설명>이라는 명령어 사용을 부탁드리겠습니다.")
                        file.save("rem1.xlsx")
                        return

            if message.content == "!공정머니 설명":
                user = message.author
                date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                embed = discord.Embed(title=f"공정머니", description="", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00000)

                embed.add_field(name=f"<1>", value=f"저희 서버 내의 가상화폐인 학생머니를 제외하고 학생들끼리의 실제 금전적가치를 가진 물건을 서로 교환하거나 판매를 할때 현금을 대신하여 공정머니를 이용하실 수 있습니다.", inline=False)
                embed.add_field(name=f"<2>", value=f"공정머니 1코인은 100원의 가치를 가집니다.", inline=False)
                embed.add_field(name=f"<3>", value=f"공정머니는 학생머니화 다르게 금전적 가치를 명확하게 가지고있습니다.", inline=False)
                embed.add_field(name=f"<4>", value=f"공정머니는 학생머니와 다르다는 것을 다시한번 알려드립니다.", inline=False)
                embed.add_field(name=f"<5>", value=f"자신이 가진 공정머니는 계좌이체, 문화상품권, 기프티콘으로 교환이 가능합니다.", inline=False)
                embed.add_field(name=f"<6>", value=f"자신의 공정머니 잔고에있는 금액의 0.05%가 월 이자로 들어옵니다.", inline=False)
                embed.add_field(name=f"<7>", value=f"윗말은 공정머니 잔고에 1000원이 있는 상태로 1달이 지나면 50원 즉 0.5공정머니가 들어오는 것입니다.", inline=False)
                embed.add_field(name=f"<8>", value=f"저희 공정머니 이용중 시스템 문제로 인한 손해는 모두 관리자가 책임지며, 시스템 문제가 아닌 사람간의 갈등문제로 인한 손해는 책임지지 않습니다.", inline=False)
                embed.add_field(name=f"<9>", value=f"공정 머니를 이용한 거래는 계정, 프로그램, 게임 아이템, 기프티콘, 문화상품권 등만 거래가 가능하며, 다른 물건을 거래하는 것은 직거래 또는 택배로 해야하기에 저희 공정머니를 이용하실 수 없습니다.", inline=False)
                embed.add_field(name=f"<10>", value=f"공정 머니는 초등학교 6학년부터 가능합니다.", inline=False)
                await message.channel.send(embed=embed)




    #대화
    t = client.get_channel(875959680994783263)
    if message.channel.id == 875282574266728459:
        if a[0] == "반" and a[1] == "장":
            await t.send(f"=======\n{datetime.datetime.utcnow()}에 {message.author}님께서  '" + a + "' 라고 말씀 하셨습니다.\n=======")
            for i in range(0, n):
                if a[i] == "안" or a[i + 1] == "녕" or a[i] == "안" and a[i + 1] == "뇽" or a[i] == "ㅎ" and a[i + 1] == "ㅇ" or a[i] == "하" and a[i + 1] == "이":
                    await message.channel.send("안녕!!")
                    return
                if a[i] == "뭐" and a[i + 1] == "해" or a[i] == "뭐" and a[i + 1] == "하" and a[i + 2] == "니":
                    await message.channel.send("나 지금 공부하는 중!")
                    return
                if a[i] == "여" and a[i + 1] == "친" or a[i] == "여" and a[i + 1] == "자" and a[i + 2] == "친" and a[i + 3] == "구":
                    await message.channel.send("여자친구 없어!...ㅠㅠ")
                    return
                if a[i] == "고" and a[i + 1] == "마" or a[i] == "고" and a[i + 1] == "맙" or a[i] == "땡" and a[i + 1] == "큐":
                    await message.channel.send("고맙긴 뭘~~")
                    return
                if a[i] == "미" and a[i + 1] == "안":
                    await message.channel.send("....")
                    return
                if a[i] == "사" and a[i + 1] == "랑":
                    await message.channel.send("나도 사랑해~")
                    return

                if a[i] == "공" and a[i + 1] == "부":
                    await message.channel.send("어~공부")
                if a[i] == "왜" and a[i + 1] == "해":
                    await message.channel.send("다~이유가 있어")
                    return





client.run("ODc1MDUwMTA4NDQ0NjIyODU4.YRP36w.tzG1xuUaA4fOfLOjZxk2RVMFHJI")