import uiScriptLocale

window = {
	"name" : "PickMoneyDialog",

	"x" : 100,
	"y" : 100,

	"style" : ("movable", "float",),

	"width" : 170,
	"height" : 110,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 170,
			"height" : 110,
			"title" : "Converti in Won",

			"children" :
			(
				# {
					# "name" : "label1",
					# "type" : "text",

					# "x" : 30,
					# "y" : 70,

					# "text" : "Vuoi convertire?",
				# },
				## Won Slot
				{
					"name" : "won_slot",
					"type" : "image",

					"x" : 30+20,
					"y" : 48+3,

					"image" : "d:/ymir work/ui/public/gold_slot.sub",

					"children" :
					(
						{
							"name" : "won_value",
							"type" : "editline",

							"x" : 3,
							"y" : 2,

							"width" : 60,
							"height" : 18,

							"input_limit" : 6,
							"only_number" : 1,

							"text" : "1",
						},
					),
				},
				## Money Slot
				{
					"name" : "money_slot",
					"type" : "image",

					"x" : 30+20,
					"y" : 28+3,

					"image" : "d:/ymir work/ui/public/gold_slot.sub",

					"children" :
					(
						{"name" : "money_value", "type":"text", "text":"1", "x":0, "y":0, "all_align":"center"},
					),
				},
				{
					"name":"Cheque_Icon",
					"type":"image",
						
					"x":10+20,
					"y":48+3,

					"image":"d:/ymir work/ui/game/windows/cheque_icon.sub",
				},
				{
					"name":"Money_Icon",
					"type":"image",
						
					"x":10+20,
					"y":28+3,

					"image":"d:/ymir work/ui/game/windows/money_icon.sub",
				},

				## Button
				{
					"name" : "accept_button",
					"type" : "button",

					"x" : 20,
					"y" : 70+3,

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 90,
					"y" : 70+3,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}