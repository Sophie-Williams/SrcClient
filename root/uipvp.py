import ui
import exception
import chat
import constInfo
import grp
import net

MEDIUM_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_02.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.5)

class uiPvP(ui.ScriptWindow):
	def __init__(self):
		self.Window = ui.ScriptWindow
		self.Window.__init__(self)
		self.isLoaded = 0
	def __del__(self):
		self.Window = ui.ScriptWindow
		self.Window.__del__(self)

	def LoadGui(self, state):
		if self.isLoaded == 1:
			self.Close()
			return True
		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "pvp_system/Register.py")
			self.board			= self.GetChild("Board")
			self.subscribe		= self.GetChild("Subscribe")
			self.subscribe.SetEvent(ui.__mem_func__(self.OnClickSubscribe))
			self.state = state
			self.SetSubscribe(self.state)
		except:
			exception.Abort("Error: GUI Error: Register.py")

	def Show(self):
		ui.ScriptWindow.Show(self)
	
	def Hide(self):
		ui.ScriptWindow.Hide(self)
		
	def Close(self):
		self.Hide()
		self.isLoaded = 0
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def OnClickSubscribe(self):
		if self.state == 0:
			net.SendChatPacket("/auto_pvp_subscribe")
		else:
		#logout
			net.SendChatPacket("/auto_pvp_unsubscribe")
		
	# launcher
	def SetSubscribe(self, state):
		self.state = state
		if state == 1:
			self.subscribe.SetText("Cancella Iscrizione")
		else:
			self.subscribe.SetText("Iscriviti")
	