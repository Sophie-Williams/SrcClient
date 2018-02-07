import ui
import exception
import chat
import uiToolTip
import mouseModule
import constInfo
import wndMgr
import net
import grp
from _weakref import proxy
import app
import player

BUTTON_IMAGE = ["d:/ymir work/ui/public/Middle_Button_01.sub", "d:/ymir work/ui/public/Middle_Button_02.sub", "d:/ymir work/ui/public/Middle_Button_03.sub"]
NORMAL_QUEST = grp.GenerateColor(0.69, 0.89, 0.68, 1.0)
MAIN_QUEST = grp.GenerateColor(1, 0.89, 0.68, 1.0)
class MouseReflector(ui.Window):
	def __init__(self, parent):
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.AddFlag("not_pick")
		self.width = self.height = 0
		self.isDown = False

	def Down(self):
		self.isDown = True

	def Up(self):
		self.isDown = False

	def OnRender(self):

		if self.isDown:
			grp.SetColor(ui.WHITE_COLOR)
		else:
			grp.SetColor(ui.HALF_WHITE_COLOR)

		x, y = self.GetGlobalPosition()
		grp.RenderBar(x+2, y+2, self.GetWidth()-4, self.GetHeight()-4)

class CheckBox(ui.ImageBox):
	def __init__(self, parent, x, y, event, size):
		filename = "d:/ymir work/ui/public/Parameter_Slot_0" + str(size) + ".sub"
		ui.ImageBox.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.LoadImage(filename)

		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

		image = ui.MakeImageBox(self, "d:/ymir work/ui/public/check_image.sub", 0, 0)
		image.AddFlag("not_pick")
		image.SetWindowHorizontalAlignCenter()
		image.SetWindowVerticalAlignCenter()
		image.Hide()
		self.Enable = True
		self.image = image
		self.event = event
		self.Show()
		self.clicked = False
		self.mouseReflector.UpdateRect()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def SetCheck(self, flag):
		if flag:
			self.image.Show()
			self.clicked = True
		else:
			self.image.Hide()
			self.clicked = False

	def Toggle(self):
		if self.clicked:
			self.SetCheck(False)
		else:
			self.SetCheck(True)
			
	def Disable(self):
		self.Enable = False

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouseReflector.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouseReflector.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouseReflector.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return
		self.mouseReflector.Up()
		self.event()

class MercenaryGui(ui.ScriptWindow):
	def __init__(self):
		self.Window = ui.ScriptWindow
		self.Window.__init__(self)
		self.rButton = []
		self.rStatus = "Bloccato"
		self.tmpText = []
		self.index = 0
		self.grade = []
		self.itemDataDict = {}
		# self._mercenary = {
								# "name":			"Nessuno",
								# "race":			1,
								# "grade":		1,
								# "kill":			110,
								# "war_count":	1,
								# "leave_count":	1,
								# "level":		1,
							# }
		self.mercenary_list = {}
		self.war_list = {}
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()

		# self.TestMercenary()
		# self.TestWarList()
	def __del__(self):
		self.Window = ui.ScriptWindow
		self.Window.__del__(self)
	
	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
	def MakeButton(self, parent, x, y, tooltipText):
		button = ui.Button()
		button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(BUTTON_IMAGE[0])
		button.SetOverVisual(BUTTON_IMAGE[1])
		button.SetDownVisual(BUTTON_IMAGE[2])
		button.SetText(tooltipText)
		button.Show()
		return button
		
	def MakeTextLine(self, parent, text, color, x, y):
		textLine = ui.TextLine()
		textLine.SetParent(parent)
		textLine.SetText(text)
		textLine.SetPosition(x, y)
		textLine.SetPackedFontColor(color)
		textLine.Show()
		return textLine

	class PageWindow(ui.ScriptWindow):
		def __init__(self, parent, filename):
			ui.ScriptWindow.__init__(self)
			self.SetParent(parent)
			self.filename = filename
		def GetScriptFileName(self):
			return self.filename


	def LoadGui(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			
			#self.titlebar		= self.GetChild("TitleBar")
			#self.titlebar.SetCloseEvent(ui.__mem_func__(self.Close))
			pyScrLoader.LoadScriptFile(self, "mercenary_system/uiMercenary.py")
			self.pageWindow = self.GetChild("Board")
			self.slotWindow = self.GetChild("EquipmentSlot")
			# MercenaryInfo
			self.pName = self.GetChild("PlayerName")
			self.pLevel = self.GetChild("Level")
			self.pRace1 = self.GetChild("Race1")
			self.pRace2 = self.GetChild("Race2")
			self.pGrade = self.GetChild("Grade")
			self.pKill = self.GetChild("Kill")
			self.pWarCount = self.GetChild("WarCount")
			self.pWarLeave = self.GetChild("WarLeave")
			# WarLog
			self.WarLog1 = self.GetChild("WarLog1")
			self.WarLog2 = self.GetChild("WarLog2")
			self.WarLog3 = self.GetChild("WarLog3")
			self.WarLog4 = self.GetChild("WarLog4")
			self.KillLog1 = self.GetChild("KillLog1")
			self.KillLog2 = self.GetChild("KillLog2")
			self.KillLog3 = self.GetChild("KillLog3")
			self.KillLog4 = self.GetChild("KillLog4")
			
			self.MakeGui()
			self.pageWindow.Show()
			self.slotWindow.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.slotWindow.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		except:
			exception.Abort("Error: GUI Error: GQuest.py")
			
								# "name":			"Nessuno",
								# "race":			1,
								# "grade":		1,
								# "kill":			110,
								# "war_count":	1,
								# "leave_count":	1,
								# "level":		1,
	def TestMercenary(self):
		self.listMercenary = ["Peppe", "Spikeino", "Spykeino", "Spikelino", "Spika",
							"Ippopu", "So OP", "Elle", "Effe", "Peppe", "Secsi",
							"Secso", "Forse", "mlml"]

		for i in xrange(len(self.listMercenary)):
			#self.mercenary_list[i] = (self.listMercenary[i], 22, "Recluta", "Recluta", "Recluta", "Recluta", "Recluta")
			self.AddMercenary(i, self.listMercenary[i], app.GetRandom(1, 8), "Recluta", app.GetRandom(1, 1000), 8, 2, app.GetRandom(1, 110))
			
	def GetRaceName(self, idx):
		if (idx < 1 or idx > 8):
			return 0, 0

		self.listRace = { 1 : ["Guerriero", "Corporale"],
						  2 : ["Guerriero", "Mentale"],
						  3 : ["Ninja", "CaC"],
						  4 : ["Ninja", "Arco"],
						  5 : ["Sura", "Armi Magiche"],
						  6 : ["Sura", "Nero"],
						  7 : ["Shamano", "Cura"],
						  8 : ["Shamano", "Drago"],
						  }
		return self.listRace[idx][0], self.listRace[idx][1]
	def GetGradeFromAlign(self, align):
		return "Recluta"
		
	def AddMercenary(self, idx, name, race, grade, kill, war_count, leave_count, level):
		race1, race2 = self.GetRaceName(race)
		self.mercenary_list[idx] = (name, race1, race2, self.GetGradeFromAlign(grade), kill, war_count, leave_count, level)
		
	def AddWarList(self, idx, name, kill):
		self.war_list[idx] = (name, kill)
		if (idx == 3):
			self.SetWarLogList()
		
	def SetWarLogList(self):
		self.WarLog1.SetText(self.war_list[0][0])
		self.WarLog2.SetText(self.war_list[1][0])
		self.WarLog3.SetText(self.war_list[2][0])
		self.WarLog4.SetText(self.war_list[3][0])
		self.KillLog1.SetText(self.war_list[0][1])
		self.KillLog2.SetText(self.war_list[1][1])
		self.KillLog3.SetText(self.war_list[2][1])
		self.KillLog4.SetText(self.war_list[3][1])

	# def TestWarList(self):
		# for idx in xrange(10):
			# for i in xrange(4):
				# self.war_list[idx].append("Pinco Jo contro mlml", app.GetRandom(1, 8))

	def MakeGui(self):
		page = self.pageWindow
	
		yPos = 90 
		
		## Invite Authority
		for i in xrange(5):
			event = lambda argSelf=proxy(self), argIndex=i : apply(argSelf.ClickGrade, (argIndex,))
			inviteAuthorityCheckBox = CheckBox(page, 22+70*i, yPos, event, 1)
			self.grade.append(inviteAuthorityCheckBox)
			page.Children.append(inviteAuthorityCheckBox)
		self.MakeListMercenary()
		# label1 = ui.MakeTextLine(inviteAuthorityCheckBox)
		# label1.SetText("So secsi")
		# page.Children.append(label1)
		
	def MakeListMercenary(self):
		self.mlml_y = 152
		self.mlml_x = 20
		page = self.pageWindow
		self.mercenarySelected = []
		
		for i in xrange(len(self.mercenary_list)):
			if (i % 5 == 0):
				self.mlml_y += 20
				self.mlml_x = 20
			event = lambda argSelf=proxy(self), argIndex=i : apply(argSelf.ClickMercenary, (argIndex,))
			mercenaryCheckBox = CheckBox(page, self.mlml_x, self.mlml_y, event, 2)
			label1 = ui.MakeTextLine(mercenaryCheckBox)
			label1.SetText(self.mercenary_list[i][0])
			page.Children.append(label1)
			page.Children.append(mercenaryCheckBox)
			self.mlml_x += 80
								# "name":			"Nessuno",
								# "race":			1,
								# "grade":		1,
								# "kill":			110,
								# "war_count":	1,
								# "leave_count":	1,
								# "level":		1,


			# WarLog
			# self.WarLog1.SetText(self.mercenary_list[i][0])
			# self.WarLog2.SetText(self.mercenary_list[i][0])
			# self.WarLog3.SetText(self.mercenary_list[i][0])
			# self.WarLog4.SetText(self.mercenary_list[i][0])
			# self.KillLog1.SetText(self.mercenary_list[i][0])
			# self.KillLog2.SetText(self.mercenary_list[i][0])
			# self.KillLog3.SetText(self.mercenary_list[i][0])
			# self.KillLog4.SetText(self.mercenary_list[i][0])

	def ClickGrade(self, index):
		self.grade[index].Toggle()
		
	def ClickMercenary(self, index):
		# MercenaryInfo
		self.pName.SetText(str(self.mercenary_list[index][0]))
		self.pRace1.SetText(str(self.mercenary_list[index][1]))
		self.pRace2.SetText(str(self.mercenary_list[index][2]))
		self.pGrade.SetText(str(self.mercenary_list[index][3]))
		self.pKill.SetText(str(self.mercenary_list[index][4]))
		self.pWarCount.SetText(str(self.mercenary_list[index][5]))
		self.pWarLeave.SetText(str(self.mercenary_list[index][6]))
		self.pLevel.SetText(str(self.mercenary_list[index][7]))
		net.SendChatPacket("/get_mercenary_equip "+ str(index))
		

	def SetEquipmentDialogItem(self, slotIndex, vnum, count):
		if count <= 1:
			count = 0
		self.slotWindow.SetItemSlot(slotIndex, vnum, count)

		emptySocketList = []
		emptyAttrList = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			emptySocketList.append(0)
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			emptyAttrList.append((0, 0))
		self.itemDataDict[slotIndex] = (vnum, count, emptySocketList, emptyAttrList)

	def SetEquipmentDialogSocket(self, slotIndex, value1, value2, value3):
		if not slotIndex in self.itemDataDict:
			return
		self.itemDataDict[slotIndex][2][0] = value1
		self.itemDataDict[slotIndex][2][1] = value2
		self.itemDataDict[slotIndex][2][2] = value3

	def SetEquipmentDialogAttr(self, slotIndex, attrIndex, type, value):
		if not slotIndex in self.itemDataDict:
			return
		if attrIndex < 0 or attrIndex > player.ATTRIBUTE_SLOT_MAX_NUM:
			return
		self.itemDataDict[slotIndex][3][attrIndex] = (type, value)

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem
	def OverInItem(self, slotIndex):

		if None == self.tooltipItem:
			return

		if not slotIndex in self.itemDataDict:
			return

		itemVnum = self.itemDataDict[slotIndex][0]
		if 0 == itemVnum:
			return

		self.tooltipItem.ClearToolTip()
		metinSlot = self.itemDataDict[slotIndex][2]
		attrSlot = self.itemDataDict[slotIndex][3]
		self.tooltipItem.AddItemData(itemVnum, metinSlot, attrSlot)
		self.tooltipItem.ShowToolTip()

	def OverOutItem(self):
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

