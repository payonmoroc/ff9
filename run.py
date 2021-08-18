import websocket, json, sys, os, requests, random,time,datetime,argparse, colorama, traceback,re,names
from random import randint
from websocket import create_connection
from colorama import Fore, Back, Style
from datetime import datetime as dtime
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
colorama.init(autoreset=True)

with open('config.json', 'r') as myfile:
  par = myfile.read()
config = json.loads(par)

#========== APIKEY AND REFERAL ID ========#

apiKey = 'd96c56ddcaaa462392a8fb61054c4ee7'
refID = 408900474

#========== APIKEY AND REFERAL ID ========#

birutua = "\033[0;34m"
putih = "\033[0m"
kuning = "\033[1;33m"
hijau = "\033[1;32m"
merah = "\033[1;31m"
biru = "\033[0;36m"
ungu = "\033[1;35m"
bghijau_white = "\033[5;37;42m"
bgmerah_black = "\033[5;37;41m"
bg_ab = '\x1b[1;36;100m'
bg_ab2 = '\x1b[1;37;100m'
bg_rd = '\x1b[1;37;41m'
bg_ij = '\x1b[0;30;42m'
bg_end = '\x1b[0m'
bg_kun2 = '\x1b[0;36;40m'
hijau = Style.BRIGHT+Fore.GREEN
res = Style.RESET_ALL
abu2 = Style.DIM+Fore.WHITE
ungu = Style.BRIGHT+Fore.MAGENTA
hijau2 = Style.BRIGHT+Fore.GREEN
red2 = Style.BRIGHT+Fore.RED
red = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
blue = Style.BRIGHT+Fore.BLUE
hitam = Style.NORMAL+Fore.BLACK
putih = Style.BRIGHT+Fore.WHITE
bred = Style.BRIGHT+Back.RED
bblue = Style.BRIGHT+Back.BLUE
bwhite = Style.BRIGHT+Back.WHITE
bgreen = Style.BRIGHT+Back.GREEN
babu = Style.DIM+Back.WHITE+Fore.WHITE
putih2 = Style.BRIGHT+Fore.WHITE
hitam2 = Style.BRIGHT+Fore.BLACK
merah = Style.NORMAL+Fore.RED
merah2 = Style.BRIGHT+Fore.RED
biru = Style.NORMAL+Fore.BLUE
biru2 = Style.BRIGHT+Fore.BLUE
biru3 = Style.BRIGHT+Fore.CYAN
kuning2 = Style.BRIGHT+Fore.YELLOW
rccolor = Style.BRIGHT+Back.WHITE+Fore.BLACK
rcfontcolor = Style.NORMAL+Fore.BLACK

banner = """\033[1;34m
██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗
██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗  
██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
 ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
 Authorized by Layscape and PPKM C-19                               © BOSGE-2021
                                                                                                           """

urlaspx = 'https://www.999doge.com/api/web.aspx'

userag = str(UserAgent)
headers = {
				"user-agent": userag,
				"content-type": "application/x-www-form-urlencoded",
				"accept": "/",
				"x-requested-with": "com.reland.relandicebot",
				"sec-fetch-site": "cross-site",
				"sec-fetch-mode": "cors",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				"cookie": "lang=id"
				}
aspx = "https://www.999doge.com/"
asp = "https://www.999doge.com/api/web.aspx"
num_format = "{:.8f}".format
num_ch = "{:.2f}".format
num_ms = "{0:.0f}".format
user = config['username']
paswd = config['password']
c = requests.session()


# API INDODAX FOR GET LAST PRICE
def tunggu(x):
	sys.stdout.write("\r")
	sys.stdout.write("                                                               ")
	for remaining in range(x, 0, -1):
		sys.stdout.write("\r")
		sys.stdout.write("\033[1;30m#\033[1;32mRelogin in \033[1;0m{:2d} \033[1;32mseconds".format(remaining))
		sys.stdout.flush()
		time.sleep(1)
		sys.stdout.write("                                             ")

def konvert(persen, taruhan):
		global high
		global low
		if taruhan.lower() == "low" or taruhan.lower() == "lo":
				low = 0
				high = int(int(float(persen) * 10000) - 1)
		else:
				low = int(1000000 - int(float(persen) * 10000))
				high = 999999

def cekhilo(win,hilo):
	if hilo.lower() == "lo" or hilo.lower() == "low":
		hilo = "L"
	if hilo.lower() == "hi":
		hilo = "H"
	if 1 <= win:
		cek = bgreen+" "+str(hilo)
	else:
		cek = bred+" "+str(hilo)
	return (cek)

def wssock():
	global ws
	try:
		x = requests.get('https://www.999proxy.com/signalr/negotiate?clientProtocol=1.5&connectionData=%5B%7B%22name%22%3A%22mainhub%22%7D%5D&_=1619447968415')
		p = x.json()
		p1 = requests.utils.quote(p['ConnectionToken'])
		head = x.headers
		ws = create_connection("wss://www.999proxy.com/signalr/connect?transport=webSockets&clientProtocol=1.5&connectionToken="+str(p1)+"&connectionData=%5B%7B%22name%22%3A%22mainhub%22%7D%5D&tid=0", header = {"user-agent": userag },cookie=cok)
	except Exception as e:
		pass
	return ws

def resultbet(win,bet):
		if 1 <= win:
				cek = hijau2+" "+str(bet)
		else:
				cek = red2+"-"+str(bet)
		return (cek)

def cektime(stime, etime):
		ctime = etime - stime
		restime = datetime.timedelta(seconds=ctime)
		return str(restime).split('.')[0]



def cekerjump(data):
		datanew = ['test']
		for x in data:
				if x["Toggle"].lower() == "on":
						datanew.append(x)
		datanew.pop(0)
		return datanew


def chance():
		global chance
		val = random.uniform(config["chance min"], config["chance max"])
		calchance = val * 10000
		chance = int(calchance)
		return chance

def post(data):
		global req
		req = c.post(asp,data=data,headers=headers).json()
		return req

def register():
	print("Creating Account")
	CreateAccount = 'a=CreateAccount&Key=d96c56ddcaaa462392a8fb61054c4ee7'
	post(CreateAccount)
	AccountCookie = req['AccountCookie']
	BeginSession = 'a=BeginSession&Key=d96c56ddcaaa462392a8fb61054c4ee7&AccountCookie='+AccountCookie
	post(BeginSession)
	Session = req['SessionCookie']
	data = {
		'username': username,
		'password': password
		}
	CreateUser = 'a=CreateUser&s='+Session+'&Username='+username+'&Password='+password
	post(CreateUser)
	try:
		if req['success'] == 1:
			time.sleep(1)
			print(hijau+"\n\nAKUN DAH JADI GAS LUR")
			time.sleep(1)
			print(hijau+"\nUsername : "+res+username)
			print(hijau+"Password : "+res+password)
			sys.exit()
	except Exception as e:
		pass
	try: 
		if req['AccountHasUser'] == 1:
			print(merah+"Account Has User")
			sys.exit()
	except Exception as e:
		pass
	try: 
		if req['UsernameTaken'] == 1:
			print(merah+"Username Udah di pake coba yang lain")
			sys.exit()
	except Exception as e:
		pass

def loginaspx():
		global ses
		global refer
		global dogebalance
		global accid
		global statslogin
		global dogewallet
		global getid
		global akunid
		login = 'a=Login&Key=d96c56ddcaaa462392a8fb61054c4ee7&Username='+user+'&Password='+paswd+'&Totp='+otp
		try:
				post(login)
				ses = req['SessionCookie']
				refer = req['ReferredById']
				accid = req['AccountId']
				dogebalance = req['Doge']['Balance'] / 100000000
				accid = req['AccountId']
				os.system('cls' if os.name=='nt' else 'clear')
				statslogin = "Online"
				getwalletdoge = 'a=GetDepositAddress&s='+ses+'&Currency=doge'
				post(getwalletdoge)
				dogewallet = req['Address']
				time.sleep(2)
		except:
				print(merah+"Login GAGAL ! CEK PASSWORD DAN 2FA !!"+res)
				sys.exit()

		return ses
		return refer
		return dogebalance
		return accid
		return statslogin
		return dogewallet

def verify():
		global refer
		global statssrv
		if refer == refID:
				print(hijau+"Akun Terdaftar di Ultimate Force Bot"+putih)
				time.sleep(2)
		else:
				print(merah+"Akun tidak terdaftar di Ultimate Force Bot!!"+putih)
				sys.exit()

def rev(num):
	if (len(num) < 8):
		panjang_nol = int(8 - len(num))
		num = ((panjang_nol*"0")+str(num))
		gg = num.rstrip('0')
		km  = int(8) - (len(gg))
		a = '0' * km
		result = ("0."+gg+abu2+a+res)
	if (len(num) == 8):
		panjang_nol = int(8 - len(num))
		num = ((panjang_nol*"0")+str(num))
		gg = num.rstrip('0')
		km  = int(8) - (len(gg))
		a = '0' * km
		result = ("0."+gg+abu2+a+res)
	else:
		len_num = len(num)
		end = num[-8:]
		first = num[:len_num-8]
		gg = end.rstrip('0')
		km  = int(8) - (len(gg))
		a = '0' * km
		result = (first+"."+gg+abu2+a+res)
	return (result)


def bet():
		global dogebalance
		global basebet
		if str(getbetset).lower() == "auto":
				if 2 <= len(config["Config"]):
						print(red + "          Auto Change Betset: "+hijau+"Switch ON")
						autobetset = "on"
						nobetset = 0
						setbetset = config["Config"][nobetset]
				else:
						print("Note: You must have more than 1 betset to activate this feature!")
						print("Auto Change Betset: "+red+"Switch OFF")
						autobetset = "off"
						nobetset = 0
						setbetset = config["Config"][0]
		else:
				autobetset = "off"
				try:
						nobetset = int(getbetset)
						setbetset = config["Config"][nobetset]
				except:
						print(red+"Bet Set gak ada!")
						sys.exit()
		basebet = int(float(setbetset['Base Bet']) * 100000000)
		win = 0
		lose = 0
		prof_betset = 0
		ls_bet = 0
		lb = 0
		wn_bet = 0
		ls_res = 0
		wn_res = 0
		roll_jump = 1
		ls_cbet = 0
		wn_cbet = 0
		cjump = 0
		m_ranbet = 0
		switchbet = 0
		res_profit = 0
		wn_cbet = 0
		wn_hilo = 0
		ls_hilo = 0
		stseed =0
		hilo_bet = 0
		w = 0
		l = 0
		sp = 0
		ls = 0
		prof = 0
		ll = 0
		largestlose = 0
		hilo = "hi"
		h =0
		cn = names.get_full_name()
		print("THANKS FOR USING ULTIMATE FORCE")
		print("Stay Health and Enjoy !")
		print(hijau2+"Ganti Nama dulu "+str(cn)+res)
		time.sleep(1)
		try:
			name = '{"H":"mainhub","M":"SetFriendlyName","A":["'+str(cn)+'"]}'
			ws.send(name)
			time.sleep(1)
			print(hijau2+"Success, Change Name to "+str(cn)+res)
		except:
			print(red+"Failed, Change Name to "+str(cn)+res)
			time.sleep(1)
		print("\nWelcome "+kuning2+str(cn)+res+"\n\n")
		check_balance = 'a=GetBalance&s='+ses+'&Currency=doge'
		dogebal = requests.post("https://www.999doge.com/api/web.aspx", data=check_balance, headers=headers).json()
		balance = dogebal['Balance'] / 100000000
		bal = dogebal['Balance']
		print(kuning+"Balance :"+num_format(balance))
		if dogebal['Balance'] < 1000000:
				print("Balance HABIS DEPI DULU LUR !")
				print("Minimal Balance : 0.01 DOGE")
				sys.exit()
		else:
				pass
		konvert(setbetset["Chance"],setbetset["Bet"]["Bet"])
		cc = round(random.uniform(float(setbetset["Random Chance"]["Min"]),float(setbetset["Random Chance"]["Max"])),2)
		autobet = '{"H":"mainhub","M":"PlaceAutomatedBets","A":[-1000000,'+str(int(low))+','+str(int(high))+',1,false,false,0,0,0,false,false,0,0,'+str(int(basebet))+',986343752,2,true]}'
		ws.send(autobet)
		start = time.time()
		awaltime = time.time()
		while True:
				data = ws.recv()
				try:
						result = json.loads(data)
				except Exception as e:
						pass
				try:
						fakyu = (time.time() - start) * 1000
						h+=1
						initbase = basebet
						hilo_bet += 1
						sp = ((time.time() - start) * 1000)
						payin = str(result["R"]['payIn']).replace('-', '')
						if int(result["R"]['payOut']) != 0:
								win += 1
								lose = 0
								ls_bet = 0
								wn_bet += 1
								ls_res = 0
								wn_res+= 1
								wn_cbet +=1
								ls = 0
						else:
								largestlose = prof
								win = 0
								lose += 1
								ls_bet += 1
								wn_bet = 0
								ls_res += 1
								wn_res = 0
								wn_cbet = 0
								ls +=1
						if basebet > lb:
								lb = basebet

						if ll > largestlose:
								ll = largestlose

						if win > w:
								w += 1
						if lose > l:
								l += 1

						try:
								sp = float(1000/sp)
						except ZeroDivisionError:
								sp = 0

						if setbetset["Random Chance"]["Toggle"].lower() == "on":
								if int(float(setbetset["Random Chance"]["If Base Bet"])* 100000000)  != 0:
										if int(float(setbetset["Random Chance"]["If Base Bet"])* 100000000) <= basebet:
												cc = round(random.uniform(float(setbetset["Random Chance"]["Min"]),float(setbetset["Random Chance"]["Max"])),2)
												rcc = "on"
										else:
												if int(setbetset["Random Chance"]["Reset Chance"]) !=0:
														rcc = "off"
														cc = float(setbetset["Chance"])
												else:
														rcc = "off"
								else:
										rcc = "on"
										cc = round(random.uniform(float(setbetset["Random Chance"]["Min"]),float(setbetset["Random Chance"]["Max"])),2)
								konvert(cc,str(hilo))
						else:
								rcc = "off"
								cc = float(setbetset["Chance"])
								konvert(cc,str(hilo))


						prof = result["R"]['startingBalance'] + int(result["R"]['payOut']) - int(basebet) - bal
						if 0 <= int(prof):
								tprof = prof
						else:
								tprof = str(prof).replace('-', '')
						if config["Tools"]["Client Seed"].lower() == "on":
								if rcc == "on":
										ised = hijau + "ON"
										cseed = randint(0,999999)
										stseed +=1
										seed = hijau+str(cseed)
								else:
										stseed = 0
										ised = red + "OFF"
										cseed = 986343752
										seed = red+str(cseed)
						finalbal = int(result["R"]['startingBalance']) + int(result["R"]['payOut']) - int(basebet)
						presentase = round(int(prof) / int(bal) * 100, 3)
						presentase_lb = round(int(lb) / int(bal) * 100, 3)
						presentase_ll = round(int(ll) / int(bal) * 100, 3)
						if presentase_ll <= 0:
								percent_ll = red+'('+str(presentase_ll)+'%)'
						if presentase_ll >= 0:
								percent_ll =  putih+'('+str(presentase_ll)+'%)'
						if presentase <= 0:
								presentase_pr = red+'('+str(presentase)+'%)'+res
						if presentase >= 0:
								presentase_pr =  putih+'('+str(presentase)+'%)'+res
						if presentase_lb <= 0:
								percent_lb = red+'('+str(presentase_lb)+'%)'
						if presentase_lb >= 0:
								percent_lb =  putih+'('+str(presentase_lb)+'%)'
						if prof > 0:
								if rcc == "on":
										print (res+"|"+cekhilo(win, hilo)+" "+'\x1b[0m'+res+"|"+resultbet(win,str(rev(str(payin))))+res+"|",res+"|"+"Profit",hijau2+"+"+str(rev(str(tprof)))+presentase_pr+res+"|",res+"|"+"Balance",kuning+str(rev(str(finalbal)))+res+"|"+biru2+str(float(cc))+res+"|"+abu2+num_ms(fakyu)+"ms"+res+"                   ")
								else:
										print (res+"|"+cekhilo(win, hilo)+" "+'\x1b[0m'+res+"|"+resultbet(win,str(rev(str(payin))))+res+"|",res+"|"+"Profit",hijau2+"+"+str(rev(str(tprof)))+presentase_pr+res+"|",res+"|"+"Balance",kuning+str(rev(str(finalbal)))+res+"|"+biru2+str(float(cc))+res+"|"+abu2+num_ms(fakyu)+"ms"+res+"                   ")
						else:
								if rcc == "on":
										print (res+"|"+cekhilo(win, hilo)+" "+'\x1b[0m'+res+"|"+resultbet(win,str(rev(str(payin))))+res+"|",res+"|"+" Lose ",red2+"-"+str(rev(str(tprof)))+presentase_pr+res+"|",res+"|"+"Balance",kuning+str(rev(str(finalbal)))+res+"|"+biru2+str(float(cc))+res+"|"+abu2+num_ms(fakyu)+"ms"+res+"                   ")
								else:
										print (res+"|"+cekhilo(win, hilo)+" "+'\x1b[0m'+res+"|"+resultbet(win,str(rev(str(payin))))+res+"|",res+"|"+" Lose ",red2+"-"+str(rev(str(tprof)))+presentase_pr+res+"|",res+"|"+"Balance",kuning+str(rev(str(finalbal)))+res+"|"+biru2+str(float(cc))+res+"|"+abu2+num_ms(fakyu)+"ms"+res+"                   ")
						if rcc == "on":
								print(" "+bg_rd+putih2+" "+cektime(awaltime, time.time())+" "+bblue+putih2+ ' ' + num_ms(sp) + '/s '+bg_ab2+putih+" LB "+rev(str(lb))+bg_ab2+str(percent_lb)+" "+bg_rd+putih2+" LL "+str(rev(str(ll).replace('-', '')))+bg_rd+str(percent_ll)+" "+bblue+putih2+" "+setbetset["Name Bet Set"]+" "+bg_ab+putih+" CSEED "+str(ised)+" "+bgreen+putih+" "+str(w)+" "+bred+putih+" "+str(l)+" "+bg_end,end="\r")
						else:
								print(" "+bg_rd+putih2+" "+cektime(awaltime, time.time())+" "+bblue+putih2+ ' ' + num_ms(sp) + '/s '+bg_ab2+putih+" LB "+rev(str(lb))+bg_ab2+str(percent_lb)+" "+bg_rd+putih2+" LL "+str(rev(str(ll).replace('-', '')))+bg_rd+str(percent_ll)+" "+bblue+putih2+" "+setbetset["Name Bet Set"]+" "+bg_ab+putih+" CSEED "+str(ised)+" "+bgreen+putih+" "+str(w)+" "+bred+putih+" "+str(l)+" "+bg_end,end="\r")

						if autobetset == "on":
								if int(float(config["Auto Change Betset"]["If Profit"])*(100000000)) != 0:
										prof_betset += int(result["R"]["payOut"]) - int(initbase)
										prof_betset = int(prof_betset)
										if int(float(config["Auto Change Betset"]["If Profit"])*(100000000)) <= prof_betset:
												if len(config["Config"]) == int(nobetset)+1:
														nobetset = 0
												else:
														nobetset +=1
												setbetset = config["Config"][nobetset]
												prof_betset = 0
												switchbet = 1
												roll_jump = 1
												cjump = 0
												m_ranbet = 0
												if config["Auto Change Betset"]["Reset to Base Bet"].lower() == "on":
														basebet = int(float(setbetset["Base Bet"])* 100000000)
												print("                \033[1;35m [Reset profit] - Ganti Betset Ke \033[1;36m["+res+setbetset["Name Bet Set"]+"\033[1;36m]                        ")
								if int(config["Auto Change Betset"]["If Lose Streak"]) != 0:
										if int(config["Auto Change Betset"]["If Lose Streak"]) <= ls_cbet:
												if len(config["Config"]) == int(nobetset)+1:
														nobetset = 0
												else:
														nobetset +=1
												setbetset = config["Config"][nobetset]
												ls_cbet = 0
												switchbet = 1
												roll_jump = 1
												cjump = 0
												m_ranbet = 0
												if config["Auto Change Betset"]["Reset to Base Bet"].lower() == "on":
														basebet = int(float(setbetset["base bet"])* 100000000)
												print("                       \033[1;35m [Reset Base bet] Change Betset To \033[1;36m["+res+setbetset["Name Bet Set"]+"\033[1;36m]                        ")
								if int(config["Auto Change Betset"]["If Win Streak"]) != 0:
										if int(config["Auto Change Betset"]["If Win Streak"]) <= wn_cbet:
												if len(config["Config"]) == int(nobetset)+1:
														nobetset = 0
												else:
														nobetset +=1
												setbetset = config["Config"][nobetset]
												wn_cbet = 0
												switchbet = 1
												roll_jump = 1
												cjump = 0
												m_ranbet = 0
												if config["Auto Change Betset"]["Reset to Base Bet"].lower() == "on":
														basebet = int(float(setbetset["Base Bet"])* 100000000)
												print("                       \033[1;35m [Reset Win] - Ganti Betset Ke \033[1;36m["+res+setbetset["Name Bet Set"]+"\033[1;36m]                        ")
						datjump = cekerjump(setbetset["Jump If Lose"])
						if 1 <= len(datjump):
								if switchbet == 1:
										roll_jump = 1
										switchbet = 0
								if roll_jump == 1:
										try:
												bacajump = datjump[int(cjump)]
										except IndexError:
												m_ranbet = 1
												cjump = 0
												bacajump = datjump[int(cjump)]
								if setbetset["Repeat Jump If Lose"].lower() == "on":
										if int(float(setbetset["Base Bet"])*100000000) == basebet:
														roll_jump = 1
														cjump = 0
														m_ranbet = 0
								if m_ranbet == 1:
										if int(float(setbetset["Base Bet"])*100000000) == basebet:
												roll_jump = 1
												cjump = 0
												m_ranbet = 0
								else:
										if int(bacajump["Number Of Bets"]) <= roll_jump:
												roll_jump = 1
												if len(datjump) == int(cjump)+1:
														cjump = 0
														m_ranbet = 1
												else :
														m_ranbet = 0
														cjump += 1
										else:
												roll_jump += 1
								try:
										bacajump = datjump[int(cjump)]
								except IndexError:
										m_ranbet = 1
										cjump = 0
										bacajump = datjump[int(cjump)]
								if m_ranbet == 0:
										basebet = int(float(setbetset["Base Bet"])*100000000) * float(bacajump["If Lose"])
										basebet = int(basebet)
								else:
										if ls > 0:
												basebet *= float(setbetset["If Lose"])
												basebet = int(basebet)
												ls = 0
										else:
												basebet *= float(setbetset["If Win"])
												basebet = int(basebet)
												ls = 0
						else:
								#perkalian base bet if lose(CLEAR)
								if float(setbetset["If Lose"]) != 0:
										if ls_bet != 0:
												basebet *= float(setbetset["If Lose"])
												basebet = int(basebet)
												ls_bet = 0
						#perkalian base bet if win(CLEAR)
						if float(setbetset["If Win"]) != 0:
								if wn_bet !=0:
										basebet *= float((setbetset["If Win"]))
										basebet = int(basebet)
										wn_bet = 0
						#variable reset if win streak(CLEAR)
						if int(setbetset["Reset If Win Streak"]) != 0:
								if int(setbetset["Reset If Win Streak"]) <= wn_res:
										basebet = int(float(setbetset["Base Bet"])*100000000)
										wn_res = 0
						#variable reset if lose streak(CLEAR)
						if int(setbetset["Reset If Lose Streak"]) != 0:
								if int(setbetset["Reset If Lose Streak"]) <= ls_res:
										basebet = int(float(setbetset["Base Bet"])*100000000)
										ls_res = 0
						#variable reset if profit (CLEAR)
						if int(float(setbetset["Reset If Profit"])*100000000) != 0:
								res_profit += int(result["R"]["payOut"]) - int(initbase)
								res_profit = int(res_profit)
								if int(float(setbetset["Reset If Profit"])*100000000) <= res_profit:
										basebet = int(float(setbetset["Base Bet"])*100000000)
										res_profit = 0
						if setbetset["Bet"]["Hi / Low"]["Toggle"].lower() == "on":
								if setbetset["Bet"]["Hi / Low"]["Random"].lower() == "on":
										 hilo = random.choice(["hi","low"])
								else:
										if win !=0:
												wn_hilo += 1
												ls_hilo = 0
										else:
												ls_hilo += 1
												wn_hilo = 0
										if int(setbetset["Bet"]["Hi / Low"]["If Bets"]) !=0:
											if int(setbetset["Bet"]["Hi / Low"]["If Bets"]) <= hilo_bet:
												if hilo.lower() == "hi":
													hilo = "lo"
												else:
													hilo = "hi"
												hilo_bet = 0
										if int(setbetset["Bet"]["Hi / Low"]["If Win Streak"]) !=0:
											if int(setbetset["Bet"]["Hi / Low"]["If Win Streak"]) <= wn_hilo:
												wn_hilo = 0
												if hilo.lower() == "hi":
													hilo = "lo"
												else:
													hilo = "hi"
										if int(setbetset["Bet"]["Hi / Low"]["If Lose Streak"]) !=0:
											if int(setbetset["Bet"]["Hi / Low"]["If Lose Streak"]) <= ls_hilo:
												ls_hilo = 0
												if hilo.lower() == "hi":
													hilo = "lo"
												else:
													hilo = "hi"
						else:
								hilo = setbetset["Bet"]["Bet"]
						if int(float(config["Target Profit"]["Target Profit"])* 100000000) != 0:
								if int(float(config["Target Profit"]["Target Profit"])* 100000000) <= prof:
										if config["Target Profit"]["Relogin If Target Profit"]["Toggle"].lower() == "on":
												ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
												decTP = ansi_escape.sub('', rev(str(tprof)))
												data = {
												"type": "add",
												"Account": user,
												"currentMsg": "Profit Brok !",
												"currentProf": decTP,
												"status": "Relogin !😎"
												}
												asu = requests.post("http://139.177.182.25/", data=data)
												tunggu(int(config["Target Profit"]["Relogin If Target Profit"]["Interval"]))
												os.system('cls' if os.name=='nt' else 'clear')
												print(banner)
												wssock()
												prof = 0
												bal = finalbal
												bet()
										else:
												ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
												decTP = ansi_escape.sub('', rev(str(tprof)))
												data = {
												"type": "add",
												"Account": user,
												"currentMsg": "Profit Brok !",
												"currentProf": decTP,
												"status": "Profit !😎"
												}
												asu = requests.post("http://139.177.182.25/", data=data)
												print (hijau+"\nYay.! \nProfit Mencapai Target.....!\n"+hijau+"Profit "+res+str(rev(str(prof))))
												sys.exit()
						if int(float(config["Target Balance"]["Target Balance"]) * 100000000) != 0:
								if int(float(config["Target Balance"]["Target Balance"]) * 100000000) <= finalbal:
										ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
										decTP = ansi_escape.sub('', rev(str(tprof)))
										data = {
											"type": "add",
											"Account": user,
											"currentMsg": "WES TEKAN TARGET STOP",
											"currentProf": decTP,
											"status": "WD LER!! NTAR MATI NANGIS"
										}
										asu = requests.post("http://139.177.182.25/", data=data)
										print("\n\n\n"+hijau+"YUHUUUUU !!! \nBALANCE MENCAPAI TARGET !!"+res)
										print(hijau+"Balance : "+putih2+str(rev(str(finalbal)))+res)
										sys.exit()
						if int(float(config["Target Lose"]['Target Lose']) * 100000000) != 0:
								if int(str(prof).find('-')) == 0:
										targetlose = int(str(prof).replace('-', ''))
								else:
										targetlose = 0
								if int(float(config["Target Lose"]['Target Lose']) * 100000000) <= targetlose:
										print(Style.BRIGHT + Fore.RED + '\nLose Target....!')
										sys.exit()
						autobet = '{"H":"mainhub","M":"PlaceAutomatedBets","A":[-1000000,'+str(int(low))+','+str(int(high))+',1,false,false,0,0,0,false,false,0,0,'+str(int(basebet))+','+str(int(cseed))+',2,true]}'
						start = time.time()
						ws.send(autobet)

				except (KeyError) as e:
					if str(e.args[0]) == "payOut":
						ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
						b = dogebal['Balance']
						decTP = ansi_escape.sub('', rev(str(b)))
						data = {
							"type": "add",
							"Account": user,
							"currentMsg": "Lose brok !🥺",
							"currentProf": decTP,
							"status": "Loses !🥺"
						}
						asu = requests.post("http://139.177.182.25/", data=data)
						sys.exit("\n"+bred+kuning2+"         N O M O R E B A L A N C E ! !         "+res)
				except KeyboardInterrupt:
					print("\n"+bred+kuning2+"    E X I T ! !    "+res)
					sys.exit()
							
				except ConnectionResetError:
					print("\n\n\n"+bred+putih+" CONNECTION RESET BY HOST !!")
					time.sleep(5)
					os.system('cls' if os.name=='nt' else 'clear')
					tunggu(3600)
					print(banner)
					wssock()
					bet()

def runs():
	global ws
	try:
		loginaspx()
		print("UserAccount  : "+str(user))
		print("AccountID    : "+str(accid))
		print("Balance      : "+str(dogebalance))
		print("Deposit Doge : "+dogewallet)
		input("Press Enter !")
		verify()
	except Exception as e: 
		pass
	except KeyboardInterrupt:
		print("\n"+bred+kuning2+"    E X I T ! !    "+res)
		sys.exit()


while True:
	try:
		if int(sys.argv[1].find('-c')) == 0:
				parser = argparse.ArgumentParser(description='999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risk')
				parser.add_argument('-c',
				'--betset', default=0,
				help='Enter Your Betset Number (default: 0)')
				getbetset = parser.parse_args().betset
				os.system('cls' if os.name=='nt' else 'clear')
				otp = ""
				otp = input("2FA Code (If Enabled) : ")
				login = 'a=Login&Key='+str(apiKey)+'&Username='+user+'&Password='+paswd+'&Totp='+otp
				r = requests.session()
				dat = r.post(aspx,headers=headers,data=login)
				js = list(r.cookies.get_dict().values())
				cok ='AccountId='+str(js[0])+';SessionId='+str(js[1])
				runs()
				wssock()
				bet()
		if int(sys.argv[1].find('register')) == 0:
			os.system('cls' if os.name=='nt' else 'clear')
			print("\033[1;34m≠=============================#\033[1;33m【>>　R E G I S T E R　<<】\033[1;34m#==============================≠")
			time.sleep(2)
			print(kuning2+"\nTerima kasih telah menggunakan bot, \nJangan lupa jaga kesehatan dan jangan Lupa Berdoa !\n"+res)
			time.sleep(1)
			print(putih2+"\nSilakan masukan Username, dan Password!\n"+res)
			user = input("Username : ")
			paswd = input("Password : ")
			username = user
			password = paswd
			register()



	except IndexError as e:
			os.system('cls' if os.name=='nt' else 'clear')
			otp = ""
			otp = input("2FA Code (If Enabled) : ")
			login = 'a=Login&Key=d96c56ddcaaa462392a8fb61054c4ee7&Username='+user+'&Password='+paswd+'&Totp='+otp
			r = requests.session()
			dat = r.post(aspx,headers=headers,data=login)
			js = list(r.cookies.get_dict().values())
			cok ='AccountId='+str(js[0])+';SessionId='+str(js[1])
			runs()
			wssock()
			getbetset = 0
			bet()
	except KeyboardInterrupt:
			print("\n"+bred+kuning2+"    E X I T ! !    "+res)
			sys.exit()
	except ConnectionResetError:
			print("\n\n\n"+bred+putih+" CONNECTION RESET BY HOST !!")
			cok ='AccountId='+str(js[0])+';SessionId='+str(js[1])
			wssock()
			bet()
