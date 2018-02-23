import uiScriptLocale

window = {
	"name" : "OfflineShopAdminPanelWindow",
	
	"style" : ("movable", "float",),
	
	"x" : 0,
	"y" : 0,
	
	"width" : 220,
	"height" : 140,
	
	"children":
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			
			"style" : ("attach", ),
			
			"x" : 0,
			"y" : 0,
			
			"width" : 220,
			"height" : 140,
			
			"title" : "OfflineShop",
			
			"children" :
			(
				#Apri Negozio
				{
					"name" : "OpenOfflineShopButton",
					"type" : "button",
					
					"x" : 20,
					"y" : 55,
					
					"text" : "Apri Negozio",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				#Chiudi Negozio
				{
					"name" : "CloseOfflineShopButton",
					"type" : "button",
					
					"x" : 110,
					"y" : 55,
					
					"text" : "Chiudi Negozio",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				#Rimuovi Item
				{
					"name" : "RemoveItemButton",
					"type" : "button",
					
					"x" : 110,
					"y" : 80,
					
					"text" : "Rimuovi Item",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				#Aggiungi Item
				{
					"name" : "AddItemButton",
					"type" : "button",
					
					"x" : 20,
					"y" : 80,
					
					"text" : "Aggiungi Item",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				#Banca
				{
					"name" : "MyBankButton",
					"type" : "button",
					
					"x" : 65,
					"y" : 105,
					
					"text" : "Banca",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",										
				},
				
				# User Name
				{
					"name" : "UserName",
					"type" : "text",
					
					"x" : 20,
					"y" : 35,
					
					"text" : "Benvenuto, cosa desideri fare?",
				},
			),
		},
	),
}