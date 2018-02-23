import uiScriptLocale

window = {
	"name" : "InputDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 230,
	"height" : 110,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 230,
			"height" : 110,

			"title" : uiScriptLocale.GUILD_WAR_DECLARE,

			"children" :
			(
				## Label1
				{
					"name" : "InputName",
					"type" : "text",

					"x" : 18,
					"y" : 40,

					"text" : "Puoi sfidare tutte le gilde con punteggio simile",
				},
				## Label2
				{
					"name" : "InputName",
					"type" : "text",

					"x" : 18,
					"y" : 55,

					"text" : "al tuo. Vuoi cercare un avversario?",
				},
				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : - 61 - 5 + 30,
					"y" : 75,
					"horizontal_align" : "center",

					"text" : "Cerca",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 5 + 30,
					"y" : 75,
					"horizontal_align" : "center",

					"text" : "Chiudi",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}
