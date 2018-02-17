import net
import player
import item
import snd
import shop
import wndMgr
import app
import chat
import chr

import ui
import uiCommon
import uiToolTip
import mouseModule
import localeInfo
import constInfo

g_isEditingOfflineShop = False

def IsEditingOfflineShop():
	global g_isEditingOfflineShop
	if (g_isEditingOfflineShop):
		return True
	else:
		return False

###################################################################################################
## Offline Shop Admin Panel
class OfflineShopAdminPanelWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.wndOfflineShopAddItem = None
		self.wndOfflineShopRemoveItem = None
		self.wndOfflineShopMyBank = None
		self.closeQuestionDialog = None
		self.LoadWindow()
		self.LoadOtherWindows()
		
	def __del__(self):	
		ui.ScriptWindow.__del__(self)
		
	def Show(self):
		self.SetCenterPosition()
		self.SetTop()
		self.LoadWindow()
		
		ui.ScriptWindow.Show(self)
		
	def LoadWindow(self):
		if (self.isLoaded == 1):
			return
			
		self.isLoaded = 1
		#net.SendChatPacket(str(shop.OFFLINE_SHOP_SLOT_COUNT))
		
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/OfflineShopAdminPanel.py")
			#PythonScriptLoader.LoadScriptFile(self, "OfflineShopAdminPanel.py")
		except:
			import exception
			exception.Abort("OfflineShopAdminPanelWindow.LoadWindow.LoadObject")
			
		try:
			self.board = self.GetChild("Board")
			self.openOfflineShopButton = self.GetChild("OpenOfflineShopButton")
			self.closeOfflineShopButton = self.GetChild("CloseOfflineShopButton")
			self.addItemButton = self.GetChild("AddItemButton")
			self.removeItemButton = self.GetChild("RemoveItemButton")
			self.myBankButton = self.GetChild("MyBankButton")
		except:
			import exception
			exception.Abort("OfflineShopAdminPanelWindow.LoadWindow.BindObject")
			
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.openOfflineShopButton.SetEvent(ui.__mem_func__(self.ClickOpenOfflineShopButton))
		self.closeOfflineShopButton.SetEvent(ui.__mem_func__(self.ClickCloseOfflineShopButton))
		self.addItemButton.SetEvent(ui.__mem_func__(self.ClickAddItemButton))
		self.removeItemButton.SetEvent(ui.__mem_func__(self.ClickRemoveItemButton))
		self.myBankButton.SetEvent(ui.__mem_func__(self.ClickMyBankButton))
			
	def LoadOtherWindows(self):		
		# OFFLINE_SHOP_ADD_ITEM
		wndOfflineShopAddItem = OfflineShopAddItemWindow()
		self.wndOfflineShopAddItem = wndOfflineShopAddItem
		# END_OF_OFFLINE_SHOP_ADD_ITEM
		
		# OFFLINE_SHOP_REMOVE_ITEM
		wndOfflineShopRemoveItem = OfflineShopRemoveItemWindow()
		self.wndOfflineShopRemoveItem = wndOfflineShopRemoveItem
		# END_OF_OFFLINE_SHOP_REMOVE_ITEM
		
		# OFFLINE_SHOP_MY_BANK
		wndOfflineShopMyBank = OfflineShopBankDialog()
		self.wndOfflineShopMyBank = wndOfflineShopMyBank
		# END_OF_OFFLINE_SHOP_MY_BANK
		
	def ClickOpenOfflineShopButton(self):
		self.Close()
		net.SendChatPacket("/open_offlineshop")
		return True
		
	def ClickCloseOfflineShopButton(self):
		self.Close()
		closeQuestionDialog = uiCommon.QuestionDialog()
		closeQuestionDialog.SetText(localeInfo.DO_YOU_WANT_TO_CLOSE_OFFLINE_SHOP)
		closeQuestionDialog.SetAcceptEvent(lambda arg = True: self.AnswerCloseOfflineShop(arg))
		closeQuestionDialog.SetCancelEvent(lambda arg = False: self.AnswerCloseOfflineShop(arg))
		closeQuestionDialog.Open()
		self.closeQuestionDialog = closeQuestionDialog
	
	def AnswerCloseOfflineShop(self, flag):
		if (flag):
			net.SendDestroyOfflineShop()
			shop.ClearOfflineShopStock()
		else:
			self.Close()
			
		self.closeQuestionDialog = None
		
	def ClickAddItemButton(self):
		self.Close()
		self.wndOfflineShopAddItem.SetTop()
		self.wndOfflineShopAddItem.SetCenterPosition()
		self.wndOfflineShopAddItem.Open(localeInfo.OFFLINE_SHOP + player.GetName())
		return True
		
	def ClickRemoveItemButton(self):
		self.Close()
		self.wndOfflineShopRemoveItem.SetTop()
		self.wndOfflineShopRemoveItem.SetCenterPosition()		
		self.wndOfflineShopRemoveItem.Open(localeInfo.OFFLINE_SHOP + player.GetName())
		return True
				
	def ClickMyBankButton(self):
		self.Close()
		self.wndOfflineShopMyBank.Open()
		return True
		
	def BindInterfaceClass(self, interface):
		self.interface = interface
	
	def Destroy(self):
		self.ClearDictionary()
		self.interface = None
		
	def Close(self):
		self.Hide()
		return True
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def OnPressExitKey(self):
		self.Close()
		return True
		
###################################################################################################
## Offline Shop Add Item Window
class OfflineShopAddItemWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()
		self.tooltipItem = None
		self.priceInputBoard = None
		self.title = ""
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Refresh(self):
		net.SendRefreshOfflineShop()	
		for i in xrange(shop.OFFLINE_SHOP_SLOT_COUNT):
			itemCount = shop.GetOfflineShopItemCount(i)
			if (itemCount <= 1):
				itemCount
				
			self.itemSlot.SetItemSlot(i, shop.GetOfflineShopItemID(i))
		
		wndMgr.RefreshSlot(self.itemSlot.GetWindowHandle())
		
	def SetItemData(self, pos, itemID, itemCount, itemPrice):
		shop.SetOfflineShopItemData(pos, itemID, itemCount, itemPrice)
		
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/OfflineShopBuilder.py")
		except:
			import exception
			exception.Abort("OfflineShopAddItemWindow.LoadWindow.LoadObject")
			
		try:
			self.nameLine = self.GetChild("NameLine")
			self.itemSlot = self.GetChild("ItemSlot")
			self.btnOk = self.GetChild("OkButton")
			self.btnClose = self.GetChild("CloseButton")
			self.board = self.GetChild("Board")
		except:
			import exception
			exception.Abort("OfflineShopAddItemWindow.LoadWindow.BindObject")
			
		self.btnOk.Hide()
		self.btnClose.Hide()
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		
		# RESIZE OFFLINE SHOP ADD ITEM WINDOW
		self.board.SetSize(406, 400)
		self.SetSize(406, 400)
		# END OF RESIZE OFFLINE SHOP ADD ITEM WINDOW
		
	def Destroy(self):
		self.ClearDictionary()
		
		self.nameLine = None
		self.itemSlot = None
		self.btnOk = None
		self.btnClose = None
		self.board = None
		
	def Open(self, title):
		self.title = title
		
		if (len(title) > 25):
			self.title = title[:22] + "..."
			
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()
		self.board.SetTitleName("Meritocracy2 - Stai aggiungendo item al tuo negozio..")		
		self.Refresh()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()
		
		self.nameLine.SetText(title)
		global g_isEditingOfflineShop
		g_isEditingOfflineShop = True
		
	def Close(self):
		global g_isEditingOfflineShop
		g_isEditingOfflineShop = False
		
		self.title = ""
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def OnPressExitKey(self):
		self.Close()
		return True
		
	def SelectEmptySlot(self, slotIndex):
		try:
			if (constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1):
				return
				
			if (mouseModule.mouseController.isAttached()):
				attachedSlotType = mouseModule.mouseController.GetAttachedType()
				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				mouseModule.mouseController.DeattachObject()
				
				if (player.SLOT_TYPE_INVENTORY != attachedSlotType and player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedSlotType and player.SLOT_TYPE_GUILD_SAFEBOX != attachedSlotType):
					return
					
				attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
				itemVnum = player.GetItemIndex(attachedInvenType, attachedSlotPos)
				item.SelectItem(itemVnum)
				
				if (item.IsAntiFlag(item.ANTIFLAG_GIVE) or item.IsAntiFlag(item.ANTIFLAG_MYSHOP)):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINE_SHOP_CANNOT_SELL_ITEM)
					return
					
				priceInputBoard = uiCommon.MoneyInputDialog()
				priceInputBoard.SetTitle(item.GetItemName() + " prezzo")
				priceInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputPrice))
				priceInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputPrice))
				priceInputBoard.Open()
				
				self.priceInputBoard = priceInputBoard
				self.priceInputBoard.bDisplayPos = slotIndex
				self.priceInputBoard.bPos = attachedSlotPos
		except Exception, e:
			import dbg
			dbg.TraceError("Exception : SelectEmptySlot, %s" %(e))
				
	def AcceptInputPrice(self):
		if (not self.priceInputBoard):
			return True
			
		text = self.priceInputBoard.GetText()
		
		if (not text):
			return True
			
		if (not text.isdigit()):
			return True
			
		if (int(text) <= 0):
			return True
			
		net.SendAddOfflineShopItem(self.priceInputBoard.bPos, self.priceInputBoard.bDisplayPos, int(self.priceInputBoard.GetText()))
		snd.PlaySound("sound/ui/drop.wav")
		self.Refresh()
		self.priceInputBoard = None
		return True
		
	def CancelInputPrice(self):
		self.priceInputBoard = None
		return True
		
	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem
		
	def OverInItem(self, slotIndex):
		if (mouseModule.mouseController.isAttached()):
			return
			
		if (self.tooltipItem != 0):
			self.tooltipItem.SetOfflineShopItem(slotIndex)
			
	def OverOutItem(self):
		if (self.tooltipItem != 0):
			self.tooltipItem.HideToolTip()
			
	def OnUpdate(self):
		for i in xrange(shop.OFFLINE_SHOP_SLOT_COUNT):
			itemCount = shop.GetOfflineShopItemCount(i)
			if (itemCount <= 1):
				itemCount
				
			self.itemSlot.SetItemSlot(i, shop.GetOfflineShopItemID(i))
		
		wndMgr.RefreshSlot(self.itemSlot.GetWindowHandle())		
		
			
###################################################################################################
## Offline Shop Remove Item Window
class OfflineShopRemoveItemWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()
		self.tooltipItem = None
		self.questionDialog = None
		self.title = ""
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Refresh(self):
		net.SendRefreshOfflineShop()
		iCount = 0
		for i in xrange(shop.OFFLINE_SHOP_SLOT_COUNT):
			if (shop.GetOfflineShopItemID(i) == -842150451):
				iCount = iCount + 1
				
		if (iCount == shop.OFFLINE_SHOP_SLOT_COUNT):
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Meritocracy2> Non hai un negozio aperto.")
			return
			
		for i in xrange(shop.OFFLINE_SHOP_SLOT_COUNT):
			itemCount = shop.GetOfflineShopItemCount(i)
			if (itemCount <= 1):
				itemCount = 0
					
			self.itemSlot.SetItemSlot(i, shop.GetOfflineShopItemID(i))
		
		wndMgr.RefreshSlot(self.itemSlot.GetWindowHandle())
		
	def SetItemData(self, pos, itemID, itemCount, itemPrice):
		shop.SetOfflineShopItemData(pos, itemID, itemCount, itemPrice)
		
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/OfflineShopBuilder.py")
		except:
			import exception
			exception.Abort("OfflineShopRemoveItemWindow.LoadWindow.LoadObject")
			
		try:
			self.nameLine = self.GetChild("NameLine")
			self.itemSlot = self.GetChild("ItemSlot")
			self.btnOk = self.GetChild("OkButton")
			self.btnClose = self.GetChild("CloseButton")
			self.board = self.GetChild("Board")
		except:
			import exception
			exception.Abort("OfflineShopRemoveItemWindow.LoadWindow.BindObject")
			
		self.btnOk.Hide()
		self.btnClose.Hide()
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		
		self.itemSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.itemSlot.SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))				
		
		# RESIZE OFFLINE SHOP REMOVE ITEM WINDOW
		self.board.SetSize(406, 400)
		self.SetSize(406, 400)
		# END OF RESIZE OFFLINE SHOP REMOVE ITEM WINDOW
		
	def Destroy(self):
		self.ClearDictionary()
		
		self.nameLine = None
		self.itemSlot = None
		self.btnOk = None
		self.btnClose = None
		self.board = None
		
	def Open(self, title):
		self.title = title
		
		if (len(title) > 25):
			self.title = title[:22] + "..."
			
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()
		self.board.SetTitleName("Meritocracy2 - Stai rimuovendo oggetti dal tuo negozio..")		
		self.Refresh()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()
		
		self.nameLine.SetText(title)
		global g_isEditingOfflineShop
		g_isEditingOfflineShop = True
		
	def Close(self):
		global g_isEditingOfflineShop
		g_isEditingOfflineShop = False
		
		if (self.questionDialog):
			self.questionDialog.Close()
			self.questionDialog = None
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		
		self.title = ""
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def OnPressExitKey(self):
		self.Close()
		return True
		
	def UnselectItemSlot(self, selectedSlotPos):
		if (constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1):
			return
			
		itemIndex = shop.GetOfflineShopItemID(selectedSlotPos)
		item.SelectItem(itemIndex)
		itemName = item.GetItemName()
		
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.DO_YOU_WANT_TO_REMOVE_ITEM % (itemName))
		questionDialog.SetAcceptEvent(lambda arg = True : self.AnswerRemoveItem(arg))
		questionDialog.SetCancelEvent(lambda arg = False : self.AnswerRemoveItem(arg))
		questionDialog.Open()
		questionDialog.pos = selectedSlotPos
		self.questionDialog = questionDialog
		
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		
	def AnswerRemoveItem(self, flag):
		if (flag):
			pos = self.questionDialog.pos
			net.SendRemoveOfflineShopItem(pos)
			
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		self.Refresh()
		
	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem
		
	def OverInItem(self, slotIndex):
		if (mouseModule.mouseController.isAttached()):
			return
			
		if (self.tooltipItem != 0):
			self.tooltipItem.SetOfflineShopItem(slotIndex)
			
	def OverOutItem(self):
		if (self.tooltipItem != 0):
			self.tooltipItem.HideToolTip()
			
	def OnUpdate(self):
		for i in xrange(shop.OFFLINE_SHOP_SLOT_COUNT):
			itemCount = shop.GetOfflineShopItemCount(i)
			if (itemCount <= 1):
				itemCount
				
			self.itemSlot.SetItemSlot(i, shop.GetOfflineShopItemID(i))
		
		wndMgr.RefreshSlot(self.itemSlot.GetWindowHandle())	
		
					
###################################################################################################
## Offline Shop Bank Dialog
class OfflineShopBankDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.updateTime = 0
		self.withdrawMoneyTime = 0
		self.LoadWindow()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/OfflineShop_BankDialog.py")
			#pyScrLoader.LoadScriptFile(self, "OfflineShop_BankDialog.py")
		except:
			import exception
			exception.Abort("OfflineShopBankDialog.LoadWindow.LoadScript")
			
		try:
			self.Board = self.GetChild("Board")
			self.currentMoneyLine = self.GetChild("CurrentMoneyLine")
			self.WithdrawMoneyButton = self.GetChild("withdraw_button")
			#self.CancelButton = self.GetChild("cancel_button")
		except:
			import exception
			exception.Abort("OfflineShopBankDialog.LoadWindow.BindObject")
			
		self.Board.SetCloseEvent(ui.__mem_func__(self.Close))
		#self.CancelButton.SetEvent(ui.__mem_func__(self.Close))
		self.WithdrawMoneyButton.SetEvent(ui.__mem_func__(self.WithdrawMoney))
		
	def Close(self):
		self.currentMoneyLine.SetText("")
		self.Hide()
		
	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		
		net.SendRefreshOfflineShopMoney()

		self.currentMoneyLine.SetText(localeInfo.NumberToMoneyString(player.GetCurrentOfflineShopMoney()))
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "Gli yang vengono aggiornati ogni 15 secondi.")
		self.Show()
		
	def WithdrawMoney(self):
		try:
			currentMoney = player.GetCurrentOfflineShopMoney()
			if (currentMoney == 0):
				return
			net.SendOfflineShopWithdrawMoney(currentMoney)
			self.currentMoneyLine.SetText(localeInfo.NumberToMoneyString(player.GetCurrentOfflineShopMoney()))
		except ValueError:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Errore.")
		
	
###################################################################################################
## Offline Shop Input
class OfflineShopInputDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()
	
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/OfflineShopInputDialog.py")
			#PythonScriptLoader.LoadScriptFile(self, "OfflineShopInputDialog.py")
		except:
			import exception
			exception.Abort("OfflineShopInputDialog.LoadWindow.LoadObject")
			
		try:
			self.acceptButton = self.GetChild("AgreeButton")
			#self.cancelButton = self.GetChild("CancelButton")
			self.inputSlot = self.GetChild("InputSlot")
			self.inputValue = self.GetChild("InputValue")
			
			#self.cancelButton.SetEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("OfflineShopInputDialog.LoadWindow.BindObject")
			
			
	def Open(self):
		self.inputValue.SetFocus()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()
	
	def Close(self):
		self.ClearDictionary()
		self.inputSlot = None
		self.inputValue = None
		self.Hide()
				
	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event
		
	def SetCancelEvent(self, event):
		self.inputValue.OnPressEscapeKey = event
		
	def GetTitle(self):
		return self.inputValue.GetText()
		
	def GetTime(self):
		return 24
###################################################################################################
## Offline Shop
class OfflineShopDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.tooltipItem = 0
		self.xShopStart = 0
		self.yShopStart = 0
		self.questionDialog = None
		self.popup = None
		self.itemBuyQuestionDialog = None
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Refresh(self):
		for i in xrange(shop.OFFLINE_SHOP_SLOT_COUNT):
			itemCount = shop.GetOfflineShopItemCount(i)
			if (itemCount <= 1 or itemCount == None):
				itemCount = 0
			self.itemSlotWindow.SetItemSlot(i, shop.GetOfflineShopItemID(i), itemCount)
			
		wndMgr.RefreshSlot(self.itemSlotWindow.GetWindowHandle())
		
	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/OfflineShopDialog.py")
			#pyScrLoader.LoadScriptFile(self, "OfflineShopDialog.py")
		except:
			import exception
			exception.Abort("OfflineShopDialog.LoadDialog.LoadObject")
			
		try:
			self.itemSlotWindow = self.GetChild("ItemSlot")
			self.btnBuy = self.GetChild("BuyButton")
			# self.btnAdd = self.GetChild("AddButton")
			# self.btnRemove = self.GetChild("RemoveButton")
			# self.btnClose = self.GetChild("CloseButton")
			self.titleBar = self.GetChild("TitleBar")
			self.titleName = self.GetChild("TitleName")
		except:	
			import exception
			exception.Abort("OfflineShopDialog.LoadDialog.BindObject")			
			
		self.itemSlotWindow.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EXIST", self.SelectItemSlot)
		self.itemSlotWindow.SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)
		
		self.itemSlotWindow.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlotWindow.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		
		self.OfflineShopAdmin = OfflineShopAdminPanelWindow()

		# self.btnAdd.SetEvent(ui.__mem_func__(self.AddItem)) 
		# self.btnRemove.SetEvent(ui.__mem_func__(self.RemoveItem)) 
		# self.btnClose.SetEvent(ui.__mem_func__(self.CloseShop)) 
	
		#self.myBankButton.SetEvent(ui.__mem_func__(self.ClickMyBankButton))
			
			
		# self.btnAdd.Hide()
		# self.btnRemove.Hide()
		# self.btnClose.Hide()
		
		self.btnBuy.SetToggleUpEvent(ui.__mem_func__(self.CancelShopping))
		self.btnBuy.SetToggleDownEvent(ui.__mem_func__(self.OnBuy))
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))			
		self.Refresh()
			
	def AddItem(self):
		self.OfflineShopAdmin.ClickAddItemButton()
		self.Close()
		
	def RemoveItem(self):
		self.OfflineShopAdmin.ClickRemoveItemButton()
		self.Close()
		
	def CloseShop(self):
		self.OfflineShopAdmin.ClickCloseOfflineShopButton()
		self.Close()
		
	def Destroy(self):
		self.Close()
		self.ClearDictionary()
		
		self.tooltipItem = 0
		self.itemSlotWindow = 0
		self.btnBuy = 0
		self.titleBar = 0
		self.questionDialog = None
		self.popup = None
		
	def Open(self, vid):
		# xxx
		# self.btnAdd.Hide()
		# self.btnRemove.Hide()
		# self.btnClose.Hide()
		self.btnBuy.Show()

		shop.Open(False, False, True)
		self.Refresh()
		self.SetTop()
		self.Show()

		# Set Title Name
		if (("Negozio di " + player.GetName()) == chr.GetNameByVID(vid)):
			self.titleName.SetText("Il tuo negozio")
			self.btnBuy.Hide()
			# self.btnAdd.Show()
			# self.btnRemove.Show()
			# self.btnClose.Show()
		else:
			self.titleName.SetText(chr.GetNameByVID(vid))
		
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()
		
	def Close(self):
		if (self.itemBuyQuestionDialog):
			self.itemBuyQuestionDialog.Close()
			self.itemBuyQuestionDialog = None
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
			
		if (self.questionDialog):	
			self.OnCloseQuestionDialog()
		
		shop.Close()
		net.SendOfflineShopEndPacket()
		self.CancelShopping()
		self.tooltipItem.HideToolTip()
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def OnPressExitKey(self):
		self.Close()
		return True
		
	def OnBuy(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINE_SHOP_WARNING1)
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINE_SHOP_WARNING2)
		app.SetCursor(app.BUY)
		
	def CancelShopping(self):
		self.btnBuy.SetUp()
		app.SetCursor(app.NORMAL)
		
	def OnCloseQuestionDialog(self):
		if (not self.questionDialog):
			return
			
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		
	def UnselectItemSlot(self, selectedSlotPos):
		if (constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1):
			return
			
		self.AskBuyItem(selectedSlotPos)
		
	def SelectItemSlot(self, selectedSlotPos):
		if (constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1):
			return
			
		isAttached = mouseModule.mouseController.isAttached()
		if (not isAttached):
			curCursorNum = app.GetCursor()
			if (app.BUY == curCursorNum):
				net.SendOfflineShopBuyPacket(selectedSlotPos)
			else:
				selectedItemID = shop.GetOfflineShopItemID(selectedSlotPos)
				itemCount = shop.GetOfflineShopItemCount(selectedSlotPos)
				
				type = player.SLOT_TYPE_OFFLINE_SHOP
				mouseModule.mouseController.AttachObject(self, type, selectedSlotPos, selectedItemID, itemCount)
				mouseModule.mouseController.SetCallBack("INVENTORY", ui.__mem_func__(self.DropToInventory))
				snd.PlaySound("sound/ui/pick.wav")

	def DropToInventory(self):
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		self.AskBuyItem(attachedSlotPos)

	def AskBuyItem(self, slotPos):
		itemIndex = shop.GetOfflineShopItemID(slotPos)
		itemPrice = shop.GetOfflineShopItemPrice(slotPos)
		itemCount = shop.GetOfflineShopItemCount(slotPos)

		item.SelectItem(itemIndex)
		itemName = item.GetItemName()

		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.pos = slotPos
		self.itemBuyQuestionDialog = itemBuyQuestionDialog
		
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		
	def AnswerBuyItem(self, flag):
		if (flag):
			pos = self.itemBuyQuestionDialog.pos
			net.SendOfflineShopBuyPacket(pos)

		self.itemBuyQuestionDialog.Close()
		self.itemBuyQuestionDialog = None
		
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)		
		
	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem
		
	def OverInItem(self, slotIndex):
		if (mouseModule.mouseController.isAttached()):
			return
			
		if (self.tooltipItem != 0):
			self.tooltipItem.SetOfflineShopItem(slotIndex)
			
	def OverOutItem(self):
		if (self.tooltipItem != 0):
			self.tooltipItem.HideToolTip()
		
	def OnUpdate(self):
		USE_SHOP_LIMIT_RANGE = 1500
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.Close()

