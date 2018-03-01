import uiScriptLocale

window = {
	"name" : "OfflineShopBankWindow",
	
	"style" : ("movable", "float", ),
	
	"x" : 0,
	"y" : 0,
	
	"width" : 252,
	"height" : 97,
	
	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			
			"style" : ("attach", ),
			
			"x" : 0,
			"y" : 0,
			
			"width" : 252,
			"height" : 97,
			
			"title" : "Banca",
			
			"children" :
			(
				# {
					# "name" : "icon",
					# "type" : "expanded_image",
					
					# "x" : 15,
					# "y" : 43,
					
					# "image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/moneybag.tga",
				# },
				{
					"name" : "InfoText",
					"type" : "text",
							
					"x" : 20,
					"y" : 35,
														
					"text" : "Yang presenti in banca:",
				},
				{
					"name" : "CurrentMoneySlot",
					"type" : "slotbar",
					
					"x" : 130,
					"y" : 35,
					
					"width" : 100,
					"height" : 16,
					
					"children" :
					(
						{
							"name" : "CurrentMoneyLine",
							"type" : "text",
							
							"x" : 3,
							"y" : 1,
							
							"width" : 100,
							"height" : 16,
							
							#"text" : "Yang attuali:",
						},
					),
				},
				
				{
					"name" : "withdraw_button",
					"type" : "button",
					
					"x" : 30,
					"y" : 60,
					
					"text" : "Ritira",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				{
					"name" : "cancel_button",
					"type" : "button",
					
					"x" : 140,
					"y" : 60,
					
					"text" : "Chiudi",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",					
				},
			),
		},
	),
}