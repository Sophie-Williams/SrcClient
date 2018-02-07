import ui
import exception
import chat
import constInfo
import grp
import net
import player

MEDIUM_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_02.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.5)

class uiTeleporter(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadGui()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def LoadGui(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "tp/teleporter.py")
			self.board			= self.GetChild("Board")
			self.SetBlock()
		except:
			exception.Abort("Error: GUI Error: teleporter.py")
			
	def OnPressEscapeKey(self):
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
		self.map_list = [
								[ "pyungmoo", 			1 ],
								[ "bakra", 				1 ],
								[ "yongan", 			1 ],
								[ "yayang", 			1 ],
								[ "paludeinfetta", 		30 ],
								[ "pianadeilampi", 		50 ],
								[ "carta", 				70 ],
								[ "deserto", 			70 ],
								[ "seungryong", 		70 ],
								[ "montesohan", 		70 ],
								[ "forestaincantata",	90 ],
								[ "comingsoon",			115 ],
						]
		for i in xrange(len(self.map_list)):
			if self.level < self.map_list[i][1]:
				self.GetChild(str(self.map_list[i][0])).SetUpVisual("teleporter/" + str(self.map_list[i][0]) + "_block.jpg")
				self.GetChild(str(self.map_list[i][0])).SetOverVisual("teleporter/" + str(self.map_list[i][0]) + "_block.jpg")
				self.GetChild(str(self.map_list[i][0])).SetDownVisual("teleporter/" + str(self.map_list[i][0]) + "_block.jpg")
				self.GetChild(str(self.map_list[i][0])).SetToolTipText("Devi aver raggiunto almeno il livello " + str(self.map_list[i][1]), 0, 10)
			
	def Show(self):
		ui.ScriptWindow.Show(self)
	
	def Hide(self):
		ui.ScriptWindow.Hide(self)
		
	def Close(self):
		self.Hide()
