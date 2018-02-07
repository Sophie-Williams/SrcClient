import ui
import exception
import chat
import uiToolTip
import mouseModule
import constInfo
import wndMgr
import net

class BiologistGui(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine
			self.index = 0
			
		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 15)

	def __init__(self):
		self.Window = ui.ScriptWindow
		self.Window.__init__(self)
		self.tooltipInfo = self.TextToolTip()
		self.tooltipInfo2 = self.TextToolTip()
		self.tooltipInfo3 = self.TextToolTip()
		

	
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

	def LoadGui(self, idx, count):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "Biologist/Quest/uiQuest.py")
			self.name_map		= self.GetChild("name_map")
			self.label1			= self.GetChild("label1")
			self.label2			= self.GetChild("label2")
			self.label3			= self.GetChild("label3")
			self.item			= self.GetChild("item")
			self.label_item		= self.GetChild("label_item")
			self.button			= self.GetChild("AcceptButton")
			self.index = idx
			self.monster = []
			for i in xrange(len(constInfo.QUEST_INFO[idx]['monster_list'])):
				self.monster.append(self.GetChild("m" + str(i+1)))

			self.board		= self.GetChild("TitleBar")
			self.board.SetCloseEvent(ui.__mem_func__(self.Close))
			self.button.SetEvent(ui.__mem_func__(self.SendItem))
			self.Setup(idx, count)

		except:
			exception.Abort("Error: GUI Error: BiologistGui.py")

	def SendItem(self):
		net.SendChatPacket("/biologist_send_item")
	
	
	def Setup(self, idx, count):
		self.name_map.SetText(str(constInfo.QUEST_INFO[idx]['map']))
		self.label2.SetText("Raccogli 30 " + str(constInfo.QUEST_INFO[idx]['item']) + " per avere")
		self.label_item.SetText("Ti mancano ancora " + str(count) + " " + str(constInfo.QUEST_INFO[idx]['item']))
		self.item.LoadImage("Biologist/img/item/" + str(constInfo.QUEST_INFO[idx]['img_item']))
		for i in xrange(len(constInfo.QUEST_INFO[idx]['monster_list'])):
			self.monster[i].SetText(str(constInfo.QUEST_INFO[idx]['monster_list'][i]))
		
	def UpdateItem(self, c):
		self.label_item.SetText("Ti mancano ancora " + str(c) + " " + str(constInfo.QUEST_INFO[self.index]['item']))

	def Reward(self):
		self.label1.SetText("Hai consegnato tutti gli oggetti richiesti.")
		self.label2.SetText("Come ricompensa riceverai una rugiada")
		self.label3.SetText("casuale da PvP.")
		self.button.Hide()
		self.name_map.Hide()
		self.item.Hide()
		self.label_item.Hide()
		for i in xrange(len(constInfo.QUEST_INFO[self.index]['monster_list'])):
			self.monster[i].Hide()

			
