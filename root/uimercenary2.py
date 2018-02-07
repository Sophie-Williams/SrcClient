import ui
import exception
import chat
import uiToolTip
import mouseModule
import constInfo
import wndMgr
import net

class MercenaryGui(ui.ScriptWindow):
	def __init__(self):
		self.Window = ui.ScriptWindow
		self.Window.__init__(self)
	
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

	def LoadGui(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiMercenaryTest.py")

		except:
			exception.Abort("Error: GUI Error: uiMercenaryTest.py")


			
