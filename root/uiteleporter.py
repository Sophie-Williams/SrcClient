import ui
import exception
import chat
import constInfo
import grp
import net
import player
from _weakref import proxy

MEDIUM_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_02.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.5)
class QuestionDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)
	#tilted
	# def OnPressEscapeKey(self):
		# self.Close()
		# return True

class uiTeleporter(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.questionDialog = None
		self.map_list = [
								[ "pyungmoo", 			1,	"Pyungmoo(Villo1 Jinno)"],
								[ "bakra", 				1,	"Bakra(Villo2 Jinno)"],
								[ "yongan", 			1,	"Yongan (Villo1 Shinsoo)"],
								[ "yayang", 			1,	"Yayang (Villo2 Shinsoo)"],
								[ "paludeinfetta", 		30,	"Palude Infetta (Mappa exp)" ],
								[ "pianadeilampi", 		50, "Piana dei Lampi (Mappa exp)"],
								[ "carta", 				70,	"Carta (Mappa drop)"],
								[ "deserto", 			70,	"Deserto (Mappa drop)"],
								[ "seungryong", 		70,	"Seungryong (Mappa drop)"],
								[ "montesohan", 		70, "Monte Sohan (Mappa drop)"],
								[ "forestaincantata",	90, "Foresta Incantata" ],
								[ "comingsoon",			115 ],
						]
		self.isLoaded = 0
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def LoadGui(self):
		try:
			if self.isLoaded == 1:
				self.Close()
				return
			self.isLoaded = 1

			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "tp/teleporter.py")
			self.board			= self.GetChild("Board")
			self.SetBlock()
		except:
			exception.Abort("Error: GUI Error: teleporter.py")
			
	def OnPressEscapeKey(self):
		if (self.questionDialog):
			self.OnCloseQuestionDialog()
		else:
			self.Close()
		return True

	def MakeButton(self):
		button = Button()
		button.SetParent(self)
		button.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		button.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		button.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		button.SetToolTipText(localeInfo.UI_CLOSE, 0, -23)
		button.Show()
		

	def SetBlock(self):
		self.level = player.GetStatus(player.LEVEL)
		for i in xrange(len(self.map_list)):
			if self.level < self.map_list[i][1]:
				self.GetChild(str(self.map_list[i][0])).SetUpVisual("teleporter/" + str(self.map_list[i][0]) + "_block.jpg")
				self.GetChild(str(self.map_list[i][0])).SetOverVisual("teleporter/" + str(self.map_list[i][0]) + "_block.jpg")
				self.GetChild(str(self.map_list[i][0])).SetDownVisual("teleporter/" + str(self.map_list[i][0]) + "_block.jpg")
				self.GetChild(str(self.map_list[i][0])).SetToolTipText("Devi aver raggiunto almeno il livello " + str(self.map_list[i][1]), 0, 10)
			else:
				self.GetChild(str(self.map_list[i][0])).SetEvent(lambda idx=i, argSelf=proxy(self): argSelf.ClickTP(idx))

	def ClickTP(self, idx):
		if (self.questionDialog):
			self.OnCloseQuestionDialog()
			
		# il fumo uccide!
		questionDialog = QuestionDialog()
		# fine
		
		questionDialog.SetText("Vuoi essere teletrasportato a %s?" % (str(self.map_list[idx][2])))
		questionDialog.SetAcceptEvent(lambda arg = True, arg2 = idx : self.ChoseTP(arg, arg2))
		questionDialog.SetCancelEvent(lambda arg = False, arg2 = idx : self.ChoseTP(arg, arg2))
		questionDialog.Open()
		self.questionDialog = questionDialog
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	def ChoseTP(self, flag, idx):
		if flag == True:
			net.SendChatPacket("/warlords_tp " + str(self.map_list[idx][0]))
			self.Close()
		else:
			self.OnCloseQuestionDialog()

	def Show(self):
		ui.ScriptWindow.Show(self)
	
	def Hide(self):
		ui.ScriptWindow.Hide(self)
		
	def OnCloseQuestionDialog(self):
		if (not self.questionDialog):
			return
			
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		
	def Close(self):
		self.OnCloseQuestionDialog()
		self.Hide()
		self.isLoaded = 0