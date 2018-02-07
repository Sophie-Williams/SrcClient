import ui
import exception
import chat
import uiToolTip
import mouseModule
import constInfo
import wndMgr
import net
import grp
MEDIUM_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_02.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.5)

class uiGQuest(ui.ScriptWindow):
	def __init__(self):
		self.Window = ui.ScriptWindow
		self.Window.__init__(self)
		self.label_y = 32
		self.label_inc = 0
		self.cQuest = 0
		self.lQuest = {}
		self.reward = {}
		
	def __del__(self):
		self.Window = ui.ScriptWindow
		self.Window.__del__(self)
	
	def GetLabelInfo(self):
		return 18, self.label_y
		
	def GetQuestInfo(self):
		return 200, self.label_y-2
	
	def GetRewardInfo(self, idx):
		return 18, 33+20*idx
		
	def IncRewardPosition(self, step):
		self.label_y += step

	def IncLabelPosition(self, step):
		self.label_y += step
	
	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
	def MakeTextLine(self, parent, text, x, y):
		textLine = ui.TextLine()
		textLine.SetParent(parent)
		textLine.SetText(text)
		textLine.SetPosition(x, y)
		textLine.SetFontColor(0.85, 0.85, 0.85)
		textLine.Show()
		return textLine
		
	def MakeHorizontalBar(self, parent, x, y):
		bar = ui.HorizontalBar()
		bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.Create(270)
		bar.Show()
		return bar
		
	def MakeBoxInfo(self, parent, x, y):
		image = ui.ImageBox()
		image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(MEDIUM_VALUE_FILE)
		image.Show()
		return image
		
	def MakeRewardBoxInfo(self, parent, x, y):
		image = ui.ImageBox()
		image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(LARGE_VALUE_FILE)
		image.Show()
		return image

	def LoadGui(self, title):
		try:
			self.ClearGui()
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "gquest_system/GQuest.py")
			self.board		= self.GetChild("Board")
			self.board2		= self.GetChild("Board2")
			self.board.SetTitleName(title)
			#self.TestLabel()
		except:
			exception.Abort("Error: GUI Error: GQuest.py")
			
	def Open(self, title):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "GQuest.py")
			self.board		= self.GetChild("Board")
			self.board2		= self.GetChild("Board2")
			self.TestLabel()
		except:
			exception.Abort("Error: GUI Error: GQuest.py")

	def ClearGui(self):
		self.label_y = 32
		self.label_inc = 0
		self.cQuest = 0
		self.lQuest = {}
		self.reward = {}
		
	def RefreshGui(self):
		#chat.AppendChat(chat.CHAT_TYPE_INFO, str(30) + " " + str(self.label_inc*15) + " " + str(self.cQuest*20))
		new_y = 50 + (self.label_inc*20) + (self.cQuest*25)
		chat.AppendChat(chat.CHAT_TYPE_INFO, str(new_y))
		self.board.SetSize(300, new_y)
		
	def AppendLabel(self, text):
		x, y = self.GetLabelInfo()
		self.board.Children.append(self.MakeTextLine(self.board, text, x, y))
		self.IncLabelPosition(15)
		self.label_inc += 1
		self.RefreshGui()

	def AppendQuest(self, text):
		x, y = self.GetLabelInfo()
		self.board.Children.append(self.MakeTextLine(self.board, text, x, y))
		self.IncLabelPosition(20)
		self.RefreshGui()

	def AppendBar(self):
		x, y = self.GetLabelInfo()
		self.bar = self.MakeHorizontalBar(self.board, 16, y+3)
		self.board.Children.append(self.MakeTextLine(self.bar, "Lista Missioni", 100, 2))
		self.board.Children.append(self.bar)
		self.IncLabelPosition(27)
		self.RefreshGui()

	def TestLabel(self):
		self.AppendLabel("prova")
		self.AppendLabel("provassss")
		self.AppendLabel("provasssssss")
		self.AppendBar()
		self.AppendNormalQuest("1) Uccidi ottordici mazzole appuntite", "TOP", 100000, 1000, 27003)
		self.AppendNormalQuest("2) Uccidi ottordici mazzole appuntite", "TOP", 100000, 1000, 27003)
		self.AppendNormalQuest("3) Uccidi novordici mazzole appuntite", "TOP", 100000, 1000, 27003)
		self.SetRewardQuest(1)
		self.RefreshGui()
		
	def AppendNormalQuest(self, text, difficulty, exp, yang, item):
		self.reward[self.cQuest] = (exp, yang, item)
		x, y = self.GetQuestInfo()
		boxinfo = self.MakeBoxInfo(self.board, x, y)
		self.AppendQuest(text)
		self.lQuest[self.cQuest] = (self.MakeTextLine(boxinfo, "100/200", 0, 4))
		self.lQuest[self.cQuest].SetWindowHorizontalAlignCenter()
		self.lQuest[self.cQuest].SetHorizontalAlignCenter()
		self.board.Children.append(self.lQuest[self.cQuest])
		self.board.Children.append(boxinfo)
		self.cQuest += 1
		self.RefreshGui()

	def SetRewardQuest(self, idx):
		self.text_reward = (" Exp", " Yang", "")
		for i in xrange(len(self.reward[idx])):
			if (self.reward[idx][i] == 0):
				continue
			x, y = self.GetRewardInfo(i+1)
			self.board.Children.append(self.MakeTextLine(self.board2, str(idx) + ") Ricompensa", x, y))
			boxinfo = self.MakeRewardBoxInfo(self.board2, 90, y)
			textinfo = (self.MakeTextLine(boxinfo, str(self.reward[idx][i]) + self.text_reward[i] , 0, 4))
			textinfo.SetWindowHorizontalAlignCenter()
			textinfo.SetHorizontalAlignCenter()
			self.board2.Children.append(textinfo)
			self.board2.Children.append(boxinfo)
		self.RefreshGui()
