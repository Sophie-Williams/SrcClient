import uiScriptLocale

window = {
	"name" : "OfflineShopInputDialog",
	
	"x" : 0,
	"y" : 0,
	
	"style" : ("movable", "float",),
	
	"width" : 386,
	"height" : 70,
	
	"children" :
	(
		# board
		{
			"name" : "board",
			"type" : "board",
			
			"style" : ("attach",),
			
			"x" : 0,
			"y" : 0,
			
			"width" : 386,
			"height" : 70,
			
			"children":
			(
				{
					"name" : "title",
					"type" : "text",
					
					"x" : 20,
					"y" : 13,
					
					"text" : "Importante: L'apertura del negozio costera' 500k di Yang e durera' 24 ore.",
				},
				{
					"name" : "title2",
					"type" : "text",
					
					"x" : 20,
					"y" : 35,
					
					"text" : "Nome del negozio: ",
				},
				
				{
					"name" : "AgreeButton",
					"type" : "button",
					
					"x" : 260,
					"y" : 28+5,
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
					
					"text" : "Apri negozio",
				},
				
				## Input Slot
				{
					"name" : "InputSlot",
					"type" : "slotbar",

					"x" : -15,
					"y" : 30+5,
					
					"width" : 150,
					"height" : 15,
					
					"horizontal_align" : "center",
					
					"children" :
					(
						{
							"name" : "InputValue",
							"type" : "editline",

							"x" : 1,
							"y" : 1,

							"width" : 150,
							"height" : 15,

							"input_limit" : 32,
						},
					),
				},				
			),
		},
	),
}