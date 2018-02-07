import ui
import exception
import chat
import uiToolTip
import mouseModule
import constInfo
import wndMgr
import net

class HorseGui(ui.ScriptWindow):
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
		

	
	def __del__(self):
		self.Window = ui.ScriptWindow
		self.Window.__del__(self)
	
	def Show(self):
		self.LoadGui()
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def LoadGui(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uihorsesystem.py")
			self.vsmob 		= self.GetChild("Bonus1_Plus")
			self.board		= self.GetChild("TitleBar")
			self.board.SetCloseEvent(ui.__mem_func__(self.Close))

		except:
			exception.Abort("Error: GUI Error: HelpSystem.py")


			
	def OnUpdate(self):
		if TRUE == self.vsmob.IsIn():
			self.tooltipInfo.SetText("Potenzia!")
			self.tooltipInfo.Show()
		else:
			self.tooltipInfo.Hide()

			
