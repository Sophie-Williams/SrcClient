import grp
QUEST_ID = 1 # default
QUEST_INFO = { 
				0: 
				{
					"item"  		: "Palla di ghiaccio",
					"img_item"		: "palla_ghiaccio.jpg",
					"map"			: "Monte",
					"monster_list"	: [ "-Ottenibile da tutti i mostri x1",
										"-Boss Nove Code x5",
										"-Scatola Rara per Principianti",
										"-Scatola Epica per Principianti",
										"-Scatola Leggendaria per Principianti"],
				},
				1: 
				{
					"item"  		: "Occhi di ragno",
					"img_item"		: "occhi_ragno.jpg",
					"map"			: "Deserto",
					"monster_list"	: [ "-Ottenibile da tutti i mostri x1",
										"-Boss Tartaruga del Deserto x5",
										"-Scatola Rara per Principianti",
										"-Scatola Epica per Principianti",
										"-Scatola Leggendaria per Principianti"],
				},
				2: 
				{
					"item"  		: "Sacca veleno di ragno",
					"img_item"		: "sacca_veleno.jpg",
					"map"			: "Deserto",
					"monster_list"	: [ "-Ottenibile da tutti i mostri x1",
										"-Boss Tartaruga del Deserto x5",
										"-Scatola Rara per Principianti",
										"-Scatola Epica per Principianti",
										"-Scatola Leggendaria per Principianti"],
				},
				3: 
				{
					"item"  		: "Criniera fiammante",
					"img_item"		: "cri_fiammante.jpg",
					"map"			: "Carta",
					"monster_list"	: [ "-Ottenibile da tutti i mostri x1",
										"-Boss Re Fiamme x5",
										"-Scatola Rara per Principianti",
										"-Scatola Epica per Principianti",
										"-Scatola Leggendaria per Principianti"],
				},
				4: 
				{
					"item"  		: "Guida esoterica",
					"img_item"		: "guida_esoterica.jpg",
					"map"			: "Valle",
					"monster_list"	: [ "-Ottenibile da tutti i mostri x1",
										"-Boss Capo Orco x5",
										"-Scatola Rara per Principianti",
										"-Scatola Epica per Principianti",
										"-Scatola Leggendaria per Principianti"],
				},
				5: 
				{
					"item"  		: "Amuleto dell'orco",
					"img_item"		: "amuleto_orco.jpg",
					"map"			: "Valle",
					"monster_list"	: [ "-Ottenibile da tutti i mostri x1",
										"-Boss Capo Orco x5",
										"-Scatola Rara per Principianti",
										"-Scatola Epica per Principianti",
										"-Scatola Leggendaria per Principianti"],
				},
				6: 
				{
					"item"  		: "Simbolo del guerriero",
					"img_item"		: "simbolo_guerriero.jpg",
					"map"			: "Carta",
					"monster_list"	: [ "-Ottenibile da tutti i mostri x1",
										"-Boss Re Fiamme x5",
										"-Scatola Rara per Principianti",
										"-Scatola Epica per Principianti",
										"-Scatola Leggendaria per Principianti"],
				},
				7: 
				{
					"item"  		: "Pezzo di ghiaccio",
					"img_item"		: "pezzo_ghiaccio.jpg",
					"map"			: "Monte",
					"monster_list"	: [ "-Ottenibile da tutti i mostri x1",
										"-Boss Nove Code x5",
										"-Scatola Rara per Principianti",
										"-Scatola Epica per Principianti",
										"-Scatola Leggendaria per Principianti"],
				},
			}
HEIGHT = 220
WIDTH = 304
GQUEST_MAP_INFO = { 
			0: 
			{ 	"HEIGHT" 			: 220,
				"WIDTH"  			: 304,
				"bg"				: "bg_villo.jpg",
				# (int) ((lv_pg-30)/2) = next quest  
				"levelup_quest"		: [ "[Raggiungi il livello 20] x2 Frammento razza",
										"[Raggiungi il livello 22] x2 Frammento razza",
										"[Raggiungi il livello 24] x2 Frammento razza",
										"[Raggiungi il livello 26] x2 Frammento razza",
										"[Raggiungi il livello 28] x2 Frammento razza",
										"[Raggiungi il livello 30] x2 Frammento razza",
									  ],
				# idx+lv
				"target"			: [ "Fante Selvaggio",
										"Scagnozzo Selvaggio",
										"Soldato Vento Oscuro",
										"Maniaco del Vento Oscuro",
									],
				"hunting_quest"		: [ ],
										
				"main_quest"		: 	"[Nuova Quest] [Lv30] La capitale",
				
				"color"				:	[grp.GenerateColor(0.67, 1.0, 0.92, 1.0),
										 grp.GenerateColor(0.50, 0.94, 0.73, 1.0),
										 grp.GenerateColor(1, 0.89, 0.68, 1.0),
										],

			},

			1: 
			{ 	"HEIGHT" 			: 220,
				"WIDTH"  			: 304,
				"bg"				: "bg_palude.jpg",
				# (int) ((lv_pg-30)/2) = next quest  
				"levelup_quest"		: [ "[Raggiungi il livello 32] x2 Frammento razza",
										"[Raggiungi il livello 34] x2 PDA",
										"[Raggiungi il livello 36] x2 Frammento razza",
										"[Raggiungi il livello 38] x2 PDA",
										"[Raggiungi il livello 40] x2 Frammento razza",
										"[Raggiungi il livello 42] x2 PDA",
										"[Raggiungi il livello 44] x2 Frammento razza",
										"[Raggiungi il livello 46] x2 PDA",
										"[Raggiungi il livello 48] x2 Frammento razza",
										"[Raggiungi il livello 50] x10 PDA",
									  ],
				# idx+lv
				"target"			: [ "Uomini Appestati",
										"Spadaccini Appestati",
										"Lancieri Appestati",
									],
				"hunting_quest"		: [ ],
										
				"main_quest"		: 	"[Nuova Quest] [Lv50] Una mappa elettrica",
				
				"color"				:	[grp.GenerateColor(0.69, 0.89, 0.68, 1.0),
										 grp.GenerateColor(1, 0.89, 0.68, 1.0),
										 grp.GenerateColor(1, 0.89, 0.68, 1.0),
										],

			},
			2: 
			{ 	"HEIGHT" 			: 220,
				"WIDTH"  			: 304,
				"bg"				: "bg_piana.jpg",
				# (int) ((lv_pg-30)/2) = next quest  
				"levelup_quest"		: [ "[Raggiungi il livello 52] x2 Frammento razza",
										"[Raggiungi il livello 54] x5 PDA",
										"[Raggiungi il livello 56] x2 Frammento razza",
										"[Raggiungi il livello 58] x5 PDA",
										"[Raggiungi il livello 60] x2 Frammento razza",
										"[Raggiungi il livello 62] x5 PDA",
										"[Raggiungi il livello 64] x2 Frammento razza",
										"[Raggiungi il livello 66] x5 PDA",
										"[Raggiungi il livello 68] x2 Frammento razza",
										"[Raggiungi il livello 70] x20 PDA",
									  ],
				# idx+lv
				"target"			: [ "Golem di Pietra",
										"Mangiasassi",
										"Golem Gigante di Pietra",
										"Guerriero Ogre",
										"Mille Guerrieri",
									],
				"hunting_quest"		: [ ],
										
				"main_quest"		: 	"[Nuova Quest] [Lv70] Un nuovo equipaggiamento.",
				
				"color"				:	[grp.GenerateColor(0.69, 0.89, 0.68, 1.0),
										 grp.GenerateColor(1, 0.89, 0.68, 1.0),
										 grp.GenerateColor(1, 0.89, 0.68, 1.0),
										],

			},

		}
	
GQUEST_STATUS_QUEST = {
	# type 1 = levelup reward
	# type 2 = hunt reward
	# type 3 = main quest
	
	
	
}
info_stone = { 
					0: [
							"Comune ", 
							"Questa magnifica pietra e' talmente comune da essere posseduta da tutti.",
							grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)],
					1: [
							"Non Comune ", 
							"Questa magnifica pietra non e' molto comune tra i nuovi arrivati.",
							grp.GenerateColor(0, 0.7, 1.0, 1.0)],
					2: [
							"Rara ", 
							"Una pietra incredibilmente rara. Solo in pochi la possiedono.",
							grp.GenerateColor(0.4, 0.7, 0.4, 1.0)],
					3: [
							"Epica ", 
							"Unica nel suo genere. Solo pochi eletti possono vantarsi di possederne anche solo una.",
							grp.GenerateColor(1.0, 0.0, 1.0, 1.0)],
					4: [
							"Leggendaria ", 
							"Esisteva sul serio..",
							grp.GenerateColor(1.0, 0.20, 0.0, 1.0)],
					}


# EXTRA BEGIN
# loads 5 (B,M,G,P,F) skills .mse
ENABLE_NEW_LEVELSKILL_SYSTEM = 0
# don"t set a random channel when you open the client
ENABLE_RANDOM_CHANNEL_SEL = 0
# don"t remove id&pass if the login attempt fails
ENABLE_CLEAN_DATA_IF_FAIL_LOGIN = 0
# ctrl+v will now work
ENABLE_PASTE_FEATURE = 0
# display all the bonuses added by a stone instead of the first one
ENABLE_FULLSTONE_DETAILS = 1
# enable successfulness % in the refine dialog
ENABLE_REFINE_PCT = 0
# extra ui features
EXTRA_UI_FEATURE = 1
# enable accessory socket expire
ENABLE_ACCESSORY_SOCKET_EXPIRE = 0
#
NEW_678TH_SKILL_ENABLE = 1
# EXTRA END

# option
IN_GAME_SHOP_ENABLE = 1
CONSOLE_ENABLE = 0

PVPMODE_ENABLE = 1
PVPMODE_TEST_ENABLE = 0
PVPMODE_ACCELKEY_ENABLE = 1
PVPMODE_ACCELKEY_DELAY = 0.5
PVPMODE_PROTECTED_LEVEL = 30

FOG_LEVEL0 = 4800.0
FOG_LEVEL1 = 9600.0
FOG_LEVEL2 = 12800.0
FOG_LEVEL = FOG_LEVEL0
FOG_LEVEL_LIST=[FOG_LEVEL0, FOG_LEVEL1, FOG_LEVEL2]

CAMERA_MAX_DISTANCE_SHORT = 2500.0
CAMERA_MAX_DISTANCE_LONG = 3500.0
CAMERA_MAX_DISTANCE_LIST=[CAMERA_MAX_DISTANCE_SHORT, CAMERA_MAX_DISTANCE_LONG]
CAMERA_MAX_DISTANCE = CAMERA_MAX_DISTANCE_SHORT

CHRNAME_COLOR_INDEX = 0

ENVIRONMENT_NIGHT="d:/ymir work/environment/moonlight04.msenv"

# constant
HIGH_PRICE = 500000
MIDDLE_PRICE = 50000
ERROR_METIN_STONE = 28960
SUB2_LOADING_ENABLE = 1
EXPANDED_COMBO_ENABLE = 1
CONVERT_EMPIRE_LANGUAGE_ENABLE = 1
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
ADD_DEF_BONUS_ENABLE = 1
LOGIN_COUNT_LIMIT_ENABLE = 0

USE_SKILL_EFFECT_UPGRADE_ENABLE = 1

VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = 1
GUILD_MONEY_PER_GSP = 100
GUILD_WAR_TYPE_SELECT_ENABLE = 1
TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE = 0

HAIR_COLOR_ENABLE = 1
ARMOR_SPECULAR_ENABLE = 1
WEAPON_SPECULAR_ENABLE = 1
SEQUENCE_PACKET_ENABLE = 1
KEEP_ACCOUNT_CONNETION_ENABLE = 1
MINIMAP_POSITIONINFO_ENABLE = 1
CONVERT_EMPIRE_LANGUAGE_ENABLE = 0
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
ADD_DEF_BONUS_ENABLE = 0
LOGIN_COUNT_LIMIT_ENABLE = 0
PVPMODE_PROTECTED_LEVEL = 15
TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE = 10

isItemQuestionDialog = 0

def GET_ITEM_QUESTION_DIALOG_STATUS():
	global isItemQuestionDialog
	return isItemQuestionDialog

def SET_ITEM_QUESTION_DIALOG_STATUS(flag):
	global isItemQuestionDialog
	isItemQuestionDialog = flag

import app
import net

########################

def SET_DEFAULT_FOG_LEVEL():
	global FOG_LEVEL
	app.SetMinFog(FOG_LEVEL)

def SET_FOG_LEVEL_INDEX(index):
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	try:
		FOG_LEVEL=FOG_LEVEL_LIST[index]
	except IndexError:
		FOG_LEVEL=FOG_LEVEL_LIST[0]
	app.SetMinFog(FOG_LEVEL)

def GET_FOG_LEVEL_INDEX():
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	return 10000000
	#return FOG_LEVEL_LIST.index(FOG_LEVEL)

########################

def SET_DEFAULT_CAMERA_MAX_DISTANCE():
	global CAMERA_MAX_DISTANCE
	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def SET_CAMERA_MAX_DISTANCE_INDEX(index):
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	try:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[index]
	except:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[0]

	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def GET_CAMERA_MAX_DISTANCE_INDEX():
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	return CAMERA_MAX_DISTANCE_LIST.index(CAMERA_MAX_DISTANCE)

########################

import chrmgr
import player
import app

def SET_DEFAULT_CHRNAME_COLOR():
	global CHRNAME_COLOR_INDEX
	chrmgr.SetEmpireNameMode(CHRNAME_COLOR_INDEX)

def SET_CHRNAME_COLOR_INDEX(index):
	global CHRNAME_COLOR_INDEX
	CHRNAME_COLOR_INDEX=index
	chrmgr.SetEmpireNameMode(index)

def GET_CHRNAME_COLOR_INDEX():
	global CHRNAME_COLOR_INDEX
	return CHRNAME_COLOR_INDEX

def SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(index):
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = index

def GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD():
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	return VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD

def SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE():
	global CONVERT_EMPIRE_LANGUAGE_ENABLE
	net.SetEmpireLanguageMode(CONVERT_EMPIRE_LANGUAGE_ENABLE)

def SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS():
	global USE_ITEM_WEAPON_TABLE_ATTACK_BONUS
	player.SetWeaponAttackBonusFlag(USE_ITEM_WEAPON_TABLE_ATTACK_BONUS)

def SET_DEFAULT_USE_SKILL_EFFECT_ENABLE():
	global USE_SKILL_EFFECT_UPGRADE_ENABLE
	app.SetSkillEffectUpgradeEnable(USE_SKILL_EFFECT_UPGRADE_ENABLE)

def SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE():
	global TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE
	app.SetTwoHandedWeaponAttSpeedDecreaseValue(TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE)

########################
import item


ACCESSORY_MATERIAL_LIST = [50623, 50624, 50625, 50626, 50627, 50628, 50629, 50630, 50631, 50632, 50633, 50634, 50635, 50636, 50637, 50638, 50639]
JewelAccessoryInfos = [
		# jewel		wrist	neck	ear
		# [ 50634,	14420,	16220,	17220 ],
		# [ 50635,	14500,	16500,	17500 ],
		# [ 50636,	14520,	16520,	17520 ],
		# [ 50637,	14540,	16540,	17540 ],
		# [ 50638,	14560,	16560,	17560 ],
		# [ 50639,	14570,	16570,	17570 ],
		[ 	50627, 	0, 		16300, 	0		],	# giada
		[ 	50628, 	0, 		16310, 	17300 	],	# ebano
		[ 	50629, 	0, 		16320, 	0 		],	# perle
		[ 	50630, 	14300, 	16330, 	0 		],	# platino
		[ 	50631, 	0, 		0, 		17310 	],	# cristallo
		[ 	50632, 	0, 		0, 		17330 	],	# ametista
		[ 	50633, 	14310, 	16340, 	17320 	],	# lacrime
	]
def GET_ACCESSORY_MATERIAL_VNUM(vnum, subType):
	ret = vnum
	item_base = (vnum / 10) * 10
	for info in JewelAccessoryInfos:
		if item.ARMOR_WRIST == subType:
			if info[1] == item_base:
				return info[0]
		elif item.ARMOR_NECK == subType:
			if info[2] == item_base:
				return info[0]
		elif item.ARMOR_EAR == subType:
			if info[3] == item_base:
				return info[0]

	if vnum >= 16210 and vnum <= 16219:
		return 50625

	if item.ARMOR_WRIST == subType:
		WRIST_ITEM_VNUM_BASE = 14000
		ret -= WRIST_ITEM_VNUM_BASE
	elif item.ARMOR_NECK == subType:
		NECK_ITEM_VNUM_BASE = 16000
		ret -= NECK_ITEM_VNUM_BASE
	elif item.ARMOR_EAR == subType:
		EAR_ITEM_VNUM_BASE = 17000
		ret -= EAR_ITEM_VNUM_BASE

	type = ret/20

	if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
		type = (ret-170) / 20
		if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
			return 0

	return ACCESSORY_MATERIAL_LIST[type]

##################################################################
## 새로 추가된 "벨트" 아이템 타입과, 벨트의 소켓에 꽂을 아이템 관련..
## 벨트의 소켓시스템은 악세서리와 동일하기 때문에, 위 악세서리 관련 하드코딩처럼 이런식으로 할 수밖에 없다..

def GET_BELT_MATERIAL_VNUM(vnum, subType = 0):
	# 현재는 모든 벨트에는 하나의 아이템(#18900)만 삽입 가능
	return 18900

##################################################################
## 자동물약 (HP: #72723 ~ #72726, SP: #72727 ~ #72730)

# 해당 vnum이 자동물약인가?
def IS_AUTO_POTION(itemVnum):
	return IS_AUTO_POTION_HP(itemVnum) or IS_AUTO_POTION_SP(itemVnum)

# 해당 vnum이 HP 자동물약인가?
def IS_AUTO_POTION_HP(itemVnum):
	if 72723 <= itemVnum and 72726 >= itemVnum:
		return 1
	elif itemVnum >= 76021 and itemVnum <= 76022:		## 새로 들어간 선물용 화룡의 축복
		return 1
	elif itemVnum == 79012:
		return 1

	return 0

# 해당 vnum이 SP 자동물약인가?
def IS_AUTO_POTION_SP(itemVnum):
	if 72727 <= itemVnum and 72730 >= itemVnum:
		return 1
	elif itemVnum >= 76004 and itemVnum <= 76005:		## 새로 들어간 선물용 수룡의 축복
		return 1
	elif itemVnum == 79013:
		return 1

	return 0

