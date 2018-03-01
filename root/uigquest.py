import ui
import exception
import chat
import uiToolTip
import mouseModule
import constInfo
import wndMgr
import net
import grp
import item

ROOT_PATH = "d:/ymir work/ui/game/windows/"

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
		self.set_bar = 0
		self.listRewardLabelText = {}
		self.listRewardBoxText = {}
		self.listRewardBox = {}
		self.reset = 0
		self.isLoaded = 0
		
	def __del__(self):
		self.Window = ui.ScriptWindow
		self.Window.__del__(self)
	
	def GetLabelInfo(self):
		return 18, self.label_y
		
	def GetQuestInfo(self):
		return 200, self.label_y-2
	
	def GetRewardInfo(self, idx):
		return 18, 33+25*idx
		
	def IncRewardPosition(self, step):
		self.label_y += step

	def IncLabelPosition(self, step):
		self.label_y += step
	
	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.isLoaded = 0
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
			
	def GetLoaded(self):
		return self.isLoaded
		
	def Open(self, title, reset):
		try:
			if self.isLoaded == 1:
				self.Close()
				return
			if (self.reset == 0 or self.isLoaded == 0):
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "gquest_system/GQuest.py")
				self.board		= self.GetChild("Board")
				self.board2		= self.GetChild("Board2")
				self.board.SetCloseEvent(ui.__mem_func__(self.Close))
				self.board2.Hide()
				self.board.SetTitleName(title)
				self.CreateRewardBoard()
				self.reset = 1
			else:
				self.ClearGui()
				self.board.SetTitleName(title)
			self.isLoaded = 1

			# self.TestLabel()
		except:
			exception.Abort("Error: GUI Error: GQuest.py")
		
	def Open2(self):
		if self.isLoaded == 1:
			self.Close()
			self.isLoaded = 0
			return
		else:
			self.isLoaded = 1
			self.Show()
						
	def ClearGui(self):
		for child in self.board.Children:
			child.Hide()

		self.label_y = 32
		self.label_inc = 0
		self.cQuest = 0
		self.lQuest = {}
		self.reward = {}
		self.listRewardLabelText = {}
		self.listRewardBoxText = {}
		self.listRewardBox = {}
		self.set_bar = 0
		
	def RefreshGui(self):
		new_y = 54 + (self.label_inc*20) + (self.cQuest*20)
		#chat.AppendChat(chat.CHAT_TYPE_INFO, str(new_y))
		self.board.SetSize(300, new_y)
		# chat.AppendChat(chat.CHAT_TYPE_INFO, str(new_y) + " " + str(self.label_inc) + " " + str(self.cQuest))
		
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
		
	def AppendNormalQuest(self, text, difficulty, kill, totalkill, exp, yang, itemVnum):
		if self.set_bar == 0:
			self.set_bar = 1
			self.AppendBar()
		item.SelectItem(itemVnum)
		self.reward[self.cQuest] = (difficulty, exp, yang, item.GetItemName())
		x, y = self.GetQuestInfo()
		boxinfo = self.MakeBoxInfo(self.board, x, y)
		self.AppendQuest(text)
		self.lQuest[self.cQuest] = (self.MakeTextLine(boxinfo, str(kill) + "/" + str(totalkill), 0, 3))
		self.lQuest[self.cQuest].SetWindowHorizontalAlignCenter()
		self.lQuest[self.cQuest].SetHorizontalAlignCenter()

		tmpButton = ui.MakeButton(self.board, x+70, y+3, "Ricompensa", ROOT_PATH, "btn_plus_up.sub", "btn_plus_over.sub", "btn_plus_down.sub")
		tmpButton.SetEvent(lambda arg=self.cQuest: self.SetRewardQuest(arg))

		self.board.Children.append(self.lQuest[self.cQuest])
		self.board.Children.append(boxinfo)
		self.board.Children.append(tmpButton)
		self.cQuest += 1
		self.RefreshGui()

	def UpdateKill(self, idx, kill, totalkill):
		self.lQuest[idx].SetText(str(kill) + "/" + str(totalkill))
		
	def ResetRewardQuest(self):
		for i in xrange(4):
			# self.listRewardLabelText[i].SetText("")
			self.listRewardLabelText[i].Hide()
			self.listRewardBoxText[i].SetText("")
			self.listRewardBoxText[i].Hide()
			self.listRewardBox[i].Hide()

	def CreateRewardBoard(self):
		for i in xrange(4):
			x, y = self.GetRewardInfo(i)
			if (i == 0):
				self.listRewardLabelText[i] = self.MakeTextLine(self.board2, "Grado missione", x, y)
			else:
				self.listRewardLabelText[i] = self.MakeTextLine(self.board2, str(i) + ") Ricompensa", x, y)
			self.listRewardLabelText[i].Hide()
			self.listRewardBox[i] = self.MakeRewardBoxInfo(self.board2, 90, y)
			self.listRewardBox[i].Hide()
			self.listRewardBoxText[i] = self.MakeTextLine(self.listRewardBox[i], "" , 0, 3)
			self.listRewardBoxText[i].SetWindowHorizontalAlignCenter()
			self.listRewardBoxText[i].SetHorizontalAlignCenter()
			self.listRewardBoxText[i].Hide()
			self.board2.Children.append(self.listRewardLabelText[i])
			self.board2.Children.append(self.listRewardBox[i])
	
	def SetRewardQuest(self, idx):
		self.ResetRewardQuest()
		self.board2.Show()
		self.text_reward = ("", " Exp", " Yang", "")
		for i in xrange(len(self.reward[idx])):
			if (self.reward[idx][i] == 0):
				continue
			x, y = self.GetRewardInfo(i)
			
			self.listRewardBoxText[i].SetText(str(self.reward[idx][i]) + self.text_reward[i])
			self.listRewardBox[i].Show()
			self.listRewardBoxText[i].Show()
			self.listRewardLabelText[i].Show()
		self.RefreshGui()
