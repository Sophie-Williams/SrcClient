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
	def __init__(self, parent, x, y, event, filename = "d:/ymir work/ui/public/Parameter_Slot_01.sub"):
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

class GQuestGui(ui.ScriptWindow):
	def __init__(self):
		self.Window = ui.ScriptWindow
		self.Window.__init__(self)
		self.rButton = []
		self.rStatus = "Bloccato"
		self.tmpGQList = []
		self.gqHuntingList = []
		self.tmpText = []
		self.index = 0
		self.grade = []
		self.itemDataDict = {}
		

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

	def LoadGui(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "GQuest/uiGQuest.py")
			#pyScrLoader.LoadScriptFile(self, "uiGQuest.py")
			self.titlebar		= self.GetChild("TitleBar")
			self.bg		= self.GetChild("background")
			
			self.text_zone = self.GetChild("text_zone")
			self.titlebar.SetCloseEvent(ui.__mem_func__(self.Close))

		except:
			exception.Abort("Error: GUI Error: GQuest.py")
			
	class PageWindow(ui.ScriptWindow):
		def __init__(self, parent, filename):
			ui.ScriptWindow.__init__(self)
			self.SetParent(parent)
			self.filename = filename
		def GetScriptFileName(self):
			return self.filename


	def LoadGui2(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			#pyScrLoader.LoadScriptFile(self, "GQuest/uiGQuest.py")
			
			#self.titlebar		= self.GetChild("TitleBar")
			#self.titlebar.SetCloseEvent(ui.__mem_func__(self.Close))
			pyScrLoader.LoadScriptFile(self, "uiGQuest.py")
			self.pageWindow = self.GetChild("Board")
			self.slotWindow = self.GetChild("EquipmentSlot")
			self.MakeGui()
			self.pageWindow.Show()
			self.slotWindow.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.slotWindow.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		except:
			exception.Abort("Error: GUI Error: GQuest.py")
			
	def MakeGui(self):
		page = self.pageWindow
		
		self.listMercenary = ["Peppe", "Spikeino", "Spykeino", "Spikelino", "Spika",
								"Ippopu", "So OP", "Elle", "Effe", "Peppe", "Secsi",
								"Secso", "Forse", "mlml"]
		self.arrayRandom = []
		for i in xrange(len(self.listMercenary)):
			self.arrayRandom.append([self.listMercenary[i], app.GetRandom(1,5)])


		yPos = 70 
		
		## Invite Authority
		for i in xrange(5):
			event = lambda argSelf=proxy(self), argIndex=i : apply(argSelf.ClickGrade, (argIndex,))
			inviteAuthorityCheckBox = CheckBox(page, 20+70*i, yPos, event)
			self.grade.append(inviteAuthorityCheckBox)
			page.Children.append(inviteAuthorityCheckBox)
		self.MakeListMercenary()
		# label1 = ui.MakeTextLine(inviteAuthorityCheckBox)
		# label1.SetText("So secsi")
		# page.Children.append(label1)
		
	def MakeListMercenary(self):
		self.mlml_y = 150
		self.mlml_x = 20
		page = self.pageWindow
		self.mercenarySelected = []
		
		for i in xrange(len(self.arrayRandom)):
			if (i % 5 == 0):
				self.mlml_y += 20
				self.mlml_x = 20
			event = lambda argSelf=proxy(self), argIndex=i : apply(argSelf.ClickMercenary, (argIndex,))
			mercenaryCheckBox = CheckBox(page, self.mlml_x, self.mlml_y, event)
			label1 = ui.MakeTextLine(mercenaryCheckBox)
			label1.SetText(self.arrayRandom[i][0])
			page.Children.append(label1)
			page.Children.append(mercenaryCheckBox)
			self.mlml_x += 70

	def ClickGrade(self, index):
		self.grade[index].Toggle()
		
	def ClickMercenary(self, index):
		self.gg = 0
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

	def SetEquipmentDialogSocket(self, slotIndex, socketIndex, value):
		if not slotIndex in self.itemDataDict:
			return
		if socketIndex < 0 or socketIndex > player.METIN_SOCKET_MAX_NUM:
			return
		self.itemDataDict[slotIndex][2][socketIndex] = value

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

	def ADDHuntingQuest(self, idx, _target, kill, total_kill):
		constInfo.GQUEST_MAP_INFO[idx]['hunting_quest'].append("[Caccia] Sconfiggi " + str(_target) + " " + str(kill) + "/" + str(total_kill) + ".")
		
	def UpdateHuntingQuest(self, idx, _target, kill, total_kill):
		self.tmpText[idx].SetText("[Caccia] Sconfiggi " + str(_target) + " " + str(kill) + "/" + str(total_kill) + ".")

	def ClearListGQuest(self):
		for i in xrange(len(self.tmpText)):
			self.tmpText[i] = None
		self.tmpGQList = []

	def MakeListGQuest(self, idx, idx_lv):
		self.index = idx
		self.ClearListGQuest()
		self.gqHuntingList = constInfo.GQUEST_MAP_INFO[idx]['hunting_quest']
		for i in xrange(len(self.gqHuntingList)):
			self.tmpGQList.append(self.gqHuntingList[i])
		self.tmpGQList.append(constInfo.GQUEST_MAP_INFO[idx]['levelup_quest'][idx_lv])
		self.tmpGQList.append(constInfo.GQUEST_MAP_INFO[idx]['main_quest'])
		self.bg.LoadImage("GQuest/" + constInfo.GQUEST_MAP_INFO[idx]['bg'])
		self.PrintListQuest()
		
	def PrintListQuest(self):
		self.tmpText = []
		for i in xrange(len(self.tmpGQList)):
			self.tmpText.append(self.MakeTextLine(self.text_zone, self.tmpGQList[i], constInfo.GQUEST_MAP_INFO[self.index]['color'][0], 15, 30+30*i))
		
		self.tmpText[len(self.tmpGQList)-1].SetPackedFontColor(constInfo.GQUEST_MAP_INFO[self.index]['color'][1])
		self.tmpText[len(self.tmpGQList)-2].SetPackedFontColor(constInfo.GQUEST_MAP_INFO[self.index]['color'][2])
