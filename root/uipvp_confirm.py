import ui
import exception
import chat
import constInfo
import grp
import net
import app

MEDIUM_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_02.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.5)
SPECIAL_TITLE_COLOR = grp.GenerateColor(1.0, 0.7843, 0.0, 1.0)

class uiPvP(ui.ScriptWindow):

	def LoadGui(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "pvp_system/pvp_confirm.py")
			self.board			= self.GetChild("Board")
			self.confirm		= self.GetChild("confirm")
			self.nb1			= self.GetChild("nb1")
			self.nb1.SetPackedFontColor(SPECIAL_TITLE_COLOR)
			self.confirm.SetEvent(ui.__mem_func__(self.AcceptDuel))
			self.left_time = app.GetTime()+30
			app.FlashApplication()
		except:
			exception.Abort("Error: GUI Error: pvp_confirm.py")

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Hide(self):
		ui.ScriptWindow.Hide(self)
			
	def OnUpdate(self):
		if self.left_time < app.GetTime():
			self.Hide()
		else:
			self.confirm.SetText("Entra(" + str(int(self.left_time-app.GetTime())) + ")")
	
	def AcceptDuel(self):
		net.SendChatPacket("/auto_pvp_enter")
		
	