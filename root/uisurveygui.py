import ui
import exception
import chat
import uiToolTip
import mouseModule
import constInfo
import wndMgr
import net

class SurveyGui(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

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
		self.tooltipInfo.Show()
		self.text_splitted = []
		self.option_splitted = []
		self.vote = 0
		self.idx = 0
	
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
		
	def HideText(self):
		for i in xrange(5):
			self.GetChild("s" + str(i+1)).Hide()
			self.GetChild("select" + str(i+1)).Hide()
			self.GetChild("label" + str(i+1)).Hide()
			
	
	def LoadGui(self, id, title, text, options):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "Survey/uiSurvey.py")
			self.idx = id
			self.HideText()
			self.GetChild("title_survey").SetText(title)
			self.select = []
			self.option_splitted = options.split('\n') 
			self.text_splitted = text.split('\n')
			for i in xrange(len(self.text_splitted)):
				self.GetChild("label" + str(i+1)).SetText(self.text_splitted[i])
				self.GetChild("label" + str(i+1)).Show()
			for i in xrange(len(self.option_splitted)):
				if (i > 5):
					continue
				self.select.append(self.GetChild("select" + str(i+1)))
				self.select[i].SetEvent(lambda arg=i: self.SetSelect(arg))
				self.select[i].Show()
				self.GetChild("s" + str(i+1)).SetText(self.option_splitted[i])
				self.GetChild("s" + str(i+1)).Show()

			self.confirm = self.GetChild("confirm")
			self.confirm.SetEvent(ui.__mem_func__(self.SendVote))

			self.board		= self.GetChild("TitleBar")
			self.board.SetCloseEvent(ui.__mem_func__(self.Close))

		except:
			exception.Abort("Error: GUI Error: SurveyGui.py")

	def ResetSelect(self):
		for i in xrange(len(self.option_splitted)):
			self.select[i].SetUp()

	def SendVote(self):
		self.Close()
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "Voto inviato!")
		net.SendChatPacket("/survey_vote " + str(self.idx) + " " + str(self.vote))


	def SetSelect(self, i):
		self.ResetSelect()
		self.vote = i+1
		self.select[i].Down()
			
	# def OnUpdate(self):
		# if TRUE == self.vsmob.IsIn():
			# self.tooltipInfo.SetText("Potenzia!")
			# self.tooltipInfo.Show()
		# else:
			# self.tooltipInfo.Hide()

			
