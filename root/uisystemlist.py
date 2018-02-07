import ui
import exception
import chat
import constInfo
import grp
import net

MEDIUM_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_02.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.5)

class uiSystemList(ui.ScriptWindow):

	def LoadGui(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "system_list.py")
			self.board			= self.GetChild("Board")
		except:
			exception.Abort("Error: GUI Error: system_list.py")

	def Show(self):
		ui.ScriptWindow.Show(self)
	
	def Hide(self):
		ui.ScriptWindow.Hide(self)
		
	def Close(self):
		self.Hide()
	
