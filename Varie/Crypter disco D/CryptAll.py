import os
import shutil
#archivi = '', 'locale_it'
#archivi = '', 'metin2_map_newboss', 'metin2_patch_6th_armor', 'OutdoorA1', 'metin2_patch_10th'
archivi2 = 'BGM', 'Effect', 'ETC', 'guild', 'icon', 'indoordeviltower1', 'indoormonkeydungeon1', 'indoormonkeydungeon2', 'indoormonkeydungeon3', 'indoorspiderdungeon1', 'item', 'locale_it', 'meritocracy2_patch_1', 'meritocracy_patch_shining', 'metin2_patch_5th_armor', 'metin2_patch_acce', 'metin2_patch_attendance', 'metin2_patch_common', 'metin2_patch_costume_soccer', 'metin2_patch_dance', 'metin2_patch_dawnmist_dungeon', 'metin2_patch_dawnmist_dungeon_mob', 'metin2_patch_dragon_rock', 'metin2_patch_dragon_rock_mobs', 'metin2_patch_dragon_rock_mobs_texcache', 'metin2_patch_dragon_rock_texcache', 'metin2_patch_ds', 'metin2_patch_dss_box', 'metin2_patch_e1', 'metin2_patch_easter1', 'metin2_patch_easter2016', 'metin2_patch_etc', 'metin2_patch_etc_costume1', 'metin2_patch_eu2', 'metin2_patch_eu3', 'metin2_patch_eu4', 'metin2_patch_flame', 'metin2_patch_flame_dragonlair', 'metin2_patch_flame_dungeon', 'metin2_patch_guildrenewal', 'metin2_patch_guildwar', 'metin2_patch_guildwar_object', 'metin2_patch_halloween', 'metin2_patch_mineral', 'metin2_patch_minigame_okey', 'metin2_patch_monster_card', 'metin2_patch_mundi', 'metin2_patch_new_halloween', 'metin2_patch_new_halloween_weapon', 'metin2_patch_new_pet', 'metin2_patch_new_select_ui', 'metin2_patch_party', 'metin2_patch_pc3', 'metin2_patch_pc3_m', 'metin2_patch_pepsi', 'metin2_patch_pet1', 'metin2_patch_pet2', 'metin2_patch_privateshop', 'metin2_patch_public', 'metin2_patch_ramadan_costume', 'metin2_patch_sd', 'metin2_patch_second_guildrenewal', 'metin2_patch_snow', 'metin2_patch_snow_dungeon', 'metin2_patch_valentine_pet', 'metin2_patch_w20_etc', 'metin2_patch_w20_sound', 'metin2_patch_w21_etc', 'metin2_patch_w21_mobs', 'metin2_patch_w21_mobs_m', 'metin2_patch_xmas', 'monster', 'monster2', 'NPC', 'npc2', 'Outdoor', 'OutdoorA1', 'OutdoorA2', 'OutdoorA3', 'OutdoorB1', 'OutdoorB3', 'OutdoorC1', 'OutdoorC3', 'outdoordesert1', 'outdoorduel', 'outdoorempirebattle1', 'outdoorfielddungeon1', 'outdoorflame1', 'outdoorgmguildbuild', 'outdoorguild1', 'outdoorguild2', 'outdoorguild3', 'outdoormilgyo1', 'OutdoorSnow1', 'outdoort1', 'outdoort2', 'outdoort3', 'outdoort4', 'outdoortrent', 'outdoortrent02', 'outdoorwedding', 'patch1', 'PC', 'pc2', 'Property', 'season1', 'season2', 'season3_eu', 'Sound', 'sound2', 'sound_m', 'Terrain', 'textureset', 'Tree', 'uiloading', 'uiscript', 'Zone'
c = 0
k = 0
archivi = {}

for root, directories, files in os.walk("cartelle"):
	archivi[k] = root.replace("cartelle\\", "")
	#print archivi[k]
	shutil.move(root, archivi[k])
	k = k + 1

for j in xrange(k-1):
	j = j+1
	#print "Cartella: "+archivi[j]
	shutil.move(archivi[j], "cartelle\\" + archivi[j])
	
while (c < k):
	print "Nome archivio: "
	cartella = {}
	i = 0
	c = c + 1
	PACK = archivi[c]
	print PACK
	try:
		for root, directories, files in os.walk("cartelle\\" + PACK):
			prova = root
			prova = prova.replace("cartelle\\" + PACK + '\\', "")
			if (root.find("ymir work") > 0): 
				ymir = 1
			
			shutil.move(root, prova)
			prova = prova.replace("cartelle\\", "")
			prova = prova.replace("ymir work", "d:\\ymir work")
			cartella[i] = prova
			i = i + 1
		for j in xrange(i):
			print "Cartella memorizzata: " + cartella[j]

		with open(PACK+'.txt' , 'w') as fp:
			fp.write('FolderName "pack"\n')
			fp.write('PackName "'+cartella[0]+'"\n\n')
			fp.write('List ExcludedFolderNameList\n{\n\t".svn"\n}\n\n')
			fp.write('List ExcludedPathList\n{\n\t"d:/ymir work/bin/"\n}\n\n')
			fp.write('List ExcludedFileNameList\n{\n\t"MakePack.exe"\n}\n\n')
			fp.write('List CompressExtNameList\n{\n\tpy\n\ttxt\n\tmsk\n\tmss\n\tmse\n\tmsf\n\tmsa\n\tspt\n\tatr\n\tdds\n\traw\n\twtr\n\tmde\n\ttga\n}\n')

			fp.write('List FileList\n{\n')
			for j in xrange(i):
				if (j == 0): j = 1
				print "Controllo nella cartella: " + cartella[j]
				for root, directories, files in os.walk(cartella[j]):
					for filename in files:
						filepath = os.path.join(root, filename)
						fp.write('\t"'+filepath+'"\n')
			fp.write('}')
			fp.close()
			os.system("MakePack.exe "+PACK+'.txt')
		for j in xrange(i-1):
			j = j+1
			if (cartella[j].find("ymir work") > 0):
				shutil.move("ymir work", "cartelle\\" + PACK + "\\" + "ymir work")
				j = j+1
				print "Sposto ymir"
			else:
				print "Risposto la cartella: " + cartella[j]
				shutil.move(cartella[j], "cartelle\\" + PACK + "\\" + cartella[j])
		#shutil.move( "cartelle\\" + PACK, "cartelle_criptate\\" + PACK)

		os.system("clear.bat")
	except:
		print "Errore"
		input()
	
raw_input()
