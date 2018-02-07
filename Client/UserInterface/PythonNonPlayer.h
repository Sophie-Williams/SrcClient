#pragma once

/*
 *	NPC ������ ������ Ÿ���� ���� �Ѵ�.
 */
class CPythonNonPlayer : public CSingleton<CPythonNonPlayer>
{
	public:
		enum  EClickEvent
		{
			ON_CLICK_EVENT_NONE		= 0,
			ON_CLICK_EVENT_BATTLE	= 1,
			ON_CLICK_EVENT_SHOP		= 2,
			ON_CLICK_EVENT_TALK		= 3,
			ON_CLICK_EVENT_VEHICLE	= 4,

			ON_CLICK_EVENT_MAX_NUM,
		};

#ifdef WJ_SHOW_MOB_INFO
		enum EAIFlags
		{
			AIFLAG_AGGRESSIVE	= (1 << 0),
			AIFLAG_NOMOVE	= (1 << 1),
			AIFLAG_COWARD	= (1 << 2),
			AIFLAG_NOATTACKSHINSU	= (1 << 3),
			AIFLAG_NOATTACKJINNO	= (1 << 4),
			AIFLAG_NOATTACKCHUNJO	= (1 << 5),
			AIFLAG_ATTACKMOB = (1 << 6 ),
			AIFLAG_BERSERK	= (1 << 7),
			AIFLAG_STONESKIN	= (1 << 8),
			AIFLAG_GODSPEED	= (1 << 9),
			AIFLAG_DEATHBLOW	= (1 << 10),
			AIFLAG_REVIVE		= (1 << 11),
		};
#endif

#ifdef WJ_SHOW_MOB_INFO_EX
		enum EImmuneFlags
		{
			IMMUNE_STUN		= (1 << 0),
			IMMUNE_SLOW		= (1 << 1),
			IMMUNE_FALL		= (1 << 2),
			IMMUNE_CURSE	= (1 << 3),
			IMMUNE_POISON	= (1 << 4),
			IMMUNE_TERROR	= (1 << 5),
			IMMUNE_REFLECT	= (1 << 6),
		};

		enum ERaceFlags
		{
			RACE_FLAG_ANIMAL	= (1 << 0),
			RACE_FLAG_UNDEAD	= (1 << 1),
			RACE_FLAG_DEVIL		= (1 << 2),
			RACE_FLAG_HUMAN		= (1 << 3),
			RACE_FLAG_ORC		= (1 << 4),
			RACE_FLAG_MILGYO	= (1 << 5),
			RACE_FLAG_INSECT	= (1 << 6),
			RACE_FLAG_FIRE		= (1 << 7),
			RACE_FLAG_ICE		= (1 << 8),
			RACE_FLAG_DESERT	= (1 << 9),
			RACE_FLAG_TREE		= (1 << 10),
			RACE_FLAG_ATT_ELEC	= (1 << 11),
			RACE_FLAG_ATT_FIRE	= (1 << 12),
			RACE_FLAG_ATT_ICE	= (1 << 13),
			RACE_FLAG_ATT_WIND	= (1 << 14),
			RACE_FLAG_ATT_EARTH	= (1 << 15),
			RACE_FLAG_ATT_DARK	= (1 << 16),
		};
#endif

		enum EMobEnchants
		{
			MOB_ENCHANT_CURSE,
			MOB_ENCHANT_SLOW,
			MOB_ENCHANT_POISON,
			MOB_ENCHANT_STUN,
			MOB_ENCHANT_CRITICAL,
			MOB_ENCHANT_PENETRATE,
			MOB_ENCHANTS_MAX_NUM
		};

		enum EMobResists
		{
			MOB_RESIST_SWORD,
			MOB_RESIST_TWOHAND,
			MOB_RESIST_DAGGER,
			MOB_RESIST_BELL,
			MOB_RESIST_FAN,
			MOB_RESIST_BOW,
			MOB_RESIST_FIRE,
			MOB_RESIST_ELECT,
			MOB_RESIST_MAGIC,
			MOB_RESIST_WIND,
			MOB_RESIST_POISON,
			MOB_RESISTS_MAX_NUM
		};

		enum EMobMaxNum
		{
			MOB_ATTRIBUTE_MAX_NUM = 12,
			MOB_SKILL_MAX_NUM = 5,
		};

#pragma pack(push)
#pragma pack(1)
		typedef struct SMobSkillLevel
		{
			DWORD       dwVnum;
			BYTE        bLevel;
		} TMobSkillLevel;

		typedef struct SMobTable_r235
		{
			enum EMobMaxNum
			{
				MOB_ATTRIBUTE_MAX_NUM = 12,
				MOB_SKILL_MAX_NUM = 1,//r1
			};

			DWORD       dwVnum;
			char        szName[CHARACTER_NAME_MAX_LEN + 1];
			char        szLocaleName[CHARACTER_NAME_MAX_LEN + 1];

			BYTE        bType;                  // Monster, NPC
			BYTE        bRank;                  // PAWN, KNIGHT, KING
			BYTE        bBattleType;            // MELEE, etc..
			BYTE        bLevel;                 // Level
			BYTE        bSize;

			DWORD       dwGoldMin;
			DWORD       dwGoldMax;
			DWORD       dwExp;
			DWORD       dwMaxHP;
			BYTE        bRegenCycle;
			BYTE        bRegenPercent;
			WORD        wDef;

			DWORD       dwAIFlag;
			DWORD       dwRaceFlag;
			DWORD       dwImmuneFlag;

			BYTE        bStr, bDex, bCon, bInt;
			DWORD       dwDamageRange[2];

			short       sAttackSpeed;
			short       sMovingSpeed;
			BYTE        bAggresiveHPPct;
			WORD        wAggressiveSight;
			WORD        wAttackRange;

			char        cEnchants[MOB_ENCHANTS_MAX_NUM];
			char        cResists[MOB_RESISTS_MAX_NUM];

			DWORD       dwResurrectionVnum;
			DWORD       dwDropItemVnum;

			BYTE        bMountCapacity;
			BYTE        bOnClickType;

			BYTE        bEmpire;
			char        szFolder[64 + 1];
			float       fDamMultiply;
			DWORD       dwSummonVnum;
			DWORD       dwDrainSP;
			DWORD		dwMonsterColor;
		    DWORD       dwPolymorphItemVnum;

			TMobSkillLevel	Skills[SMobTable_r235::MOB_SKILL_MAX_NUM];

		    BYTE		bBerserkPoint;
			BYTE		bStoneSkinPoint;
			BYTE		bGodSpeedPoint;
			BYTE		bDeathBlowPoint;
			BYTE		bRevivePoint;
		} TMobTable_r235;

		typedef struct SMobTable_r255
		{
			DWORD       dwVnum;
			char        szName[CHARACTER_NAME_MAX_LEN + 1];
			char        szLocaleName[CHARACTER_NAME_MAX_LEN + 1];

			BYTE        bType;                  // Monster, NPC
			BYTE        bRank;                  // PAWN, KNIGHT, KING
			BYTE        bBattleType;            // MELEE, etc..
			BYTE        bLevel;                 // Level
			BYTE        bSize;

			DWORD       dwGoldMin;
			DWORD       dwGoldMax;
			DWORD       dwExp;
			DWORD       dwMaxHP;
			BYTE        bRegenCycle;
			BYTE        bRegenPercent;
			WORD        wDef;

			DWORD       dwAIFlag;
			DWORD       dwRaceFlag;
			DWORD       dwImmuneFlag;

			BYTE        bStr, bDex, bCon, bInt;
			DWORD       dwDamageRange[2];

			short       sAttackSpeed;
			short       sMovingSpeed;
			BYTE        bAggresiveHPPct;
			WORD        wAggressiveSight;
			WORD        wAttackRange;

			char        cEnchants[MOB_ENCHANTS_MAX_NUM];
			char        cResists[MOB_RESISTS_MAX_NUM];

			DWORD       dwResurrectionVnum;
			DWORD       dwDropItemVnum;

			BYTE        bMountCapacity;
			BYTE        bOnClickType;

			BYTE        bEmpire;
			char        szFolder[64 + 1];
			float       fDamMultiply;
			DWORD       dwSummonVnum;
			DWORD       dwDrainSP;
			DWORD		dwMonsterColor;
		    DWORD       dwPolymorphItemVnum;

			TMobSkillLevel	Skills[MOB_SKILL_MAX_NUM];

		    BYTE		bBerserkPoint;
			BYTE		bStoneSkinPoint;
			BYTE		bGodSpeedPoint;
			BYTE		bDeathBlowPoint;
			BYTE		bRevivePoint;
		} TMobTable_r255;

		typedef struct SMobTable_r256
		{
			enum EMobResists_r3
			{
				MOB_RESIST_SWORD,
				MOB_RESIST_TWOHAND,
				MOB_RESIST_DAGGER,
				MOB_RESIST_BELL,
				MOB_RESIST_FAN,
				MOB_RESIST_BOW,
				MOB_RESIST_FIRE,
				MOB_RESIST_ELECT,
				MOB_RESIST_MAGIC,
				MOB_RESIST_WIND,
				MOB_RESIST_POISON,
				MOB_RESIST_BLEEDING,//r3
				MOB_RESISTS_MAX_NUM
			};

			DWORD       dwVnum;
			char        szName[CHARACTER_NAME_MAX_LEN + 1];
			char        szLocaleName[CHARACTER_NAME_MAX_LEN + 1];

			BYTE        bType;                  // Monster, NPC
			BYTE        bRank;                  // PAWN, KNIGHT, KING
			BYTE        bBattleType;            // MELEE, etc..
			BYTE        bLevel;                 // Level
			BYTE        bSize;

			DWORD       dwGoldMin;
			DWORD       dwGoldMax;
			DWORD       dwExp;
			DWORD       dwMaxHP;
			BYTE        bRegenCycle;
			BYTE        bRegenPercent;
			WORD        wDef;

			DWORD       dwAIFlag;
			DWORD       dwRaceFlag;
			DWORD       dwImmuneFlag;

			BYTE        bStr, bDex, bCon, bInt;
			DWORD       dwDamageRange[2];

			short       sAttackSpeed;
			short       sMovingSpeed;
			BYTE        bAggresiveHPPct;
			WORD        wAggressiveSight;
			WORD        wAttackRange;

			char        cEnchants[MOB_ENCHANTS_MAX_NUM];
			char        cResists[SMobTable_r256::MOB_RESISTS_MAX_NUM];

			DWORD       dwResurrectionVnum;
			DWORD       dwDropItemVnum;

			BYTE        bMountCapacity;
			BYTE        bOnClickType;

			BYTE        bEmpire;
			char        szFolder[64 + 1];
			float       fDamMultiply;
			DWORD       dwSummonVnum;
			DWORD       dwDrainSP;
			DWORD		dwMonsterColor;
		    DWORD       dwPolymorphItemVnum;

			TMobSkillLevel	Skills[MOB_SKILL_MAX_NUM];

		    BYTE		bBerserkPoint;
			BYTE		bStoneSkinPoint;
			BYTE		bGodSpeedPoint;
			BYTE		bDeathBlowPoint;
			BYTE		bRevivePoint;
		} TMobTable_r256;

		typedef struct SMobTable_r262
		{
			enum EMobResists_r4
			{
				MOB_RESIST_SWORD,
				MOB_RESIST_TWOHAND,
				MOB_RESIST_DAGGER,
				MOB_RESIST_BELL,
				MOB_RESIST_FAN,
				MOB_RESIST_BOW,
				MOB_RESIST_CLAW,//r4
				MOB_RESIST_FIRE,
				MOB_RESIST_ELECT,
				MOB_RESIST_MAGIC,
				MOB_RESIST_WIND,
				MOB_RESIST_POISON,
				MOB_RESIST_BLEEDING,//r3
				MOB_RESISTS_MAX_NUM
			};

			DWORD       dwVnum;
			char        szName[CHARACTER_NAME_MAX_LEN + 1];
			char        szLocaleName[CHARACTER_NAME_MAX_LEN + 1];

			BYTE        bType;                  // Monster, NPC
			BYTE        bRank;                  // PAWN, KNIGHT, KING
			BYTE        bBattleType;            // MELEE, etc..
			BYTE        bLevel;                 // Level
			BYTE		bLvlPct;
			BYTE        bSize;//r4

			DWORD       dwGoldMin;
			DWORD       dwGoldMax;
			DWORD       dwExp;
			DWORD       dwMaxHP;
			BYTE        bRegenCycle;
			BYTE        bRegenPercent;
			WORD        wDef;

			DWORD       dwAIFlag;
			DWORD       dwRaceFlag;
			DWORD       dwImmuneFlag;

			BYTE        bStr, bDex, bCon, bInt;
			DWORD       dwDamageRange[2];

			short       sAttackSpeed;
			short       sMovingSpeed;
			BYTE        bAggresiveHPPct;
			WORD        wAggressiveSight;
			WORD        wAttackRange;

			char        cEnchants[MOB_ENCHANTS_MAX_NUM];
			char        cResists[SMobTable_r262::MOB_RESISTS_MAX_NUM];

			DWORD       dwResurrectionVnum;
			DWORD       dwDropItemVnum;

			BYTE        bMountCapacity;
			BYTE        bOnClickType;

			BYTE        bEmpire;
			char        szFolder[64 + 1];
			float       fDamMultiply;
			DWORD       dwSummonVnum;
			DWORD       dwDrainSP;
			DWORD		dwMonsterColor;
		    DWORD       dwPolymorphItemVnum;

			TMobSkillLevel	Skills[MOB_SKILL_MAX_NUM];

		    BYTE		bBerserkPoint;
			BYTE		bStoneSkinPoint;
			BYTE		bGodSpeedPoint;
			BYTE		bDeathBlowPoint;
			BYTE		bRevivePoint;

			DWORD		dwHealerPoint;//r4
		} TMobTable_r262;

		typedef struct SMobTable_r263
		{
			enum EMobResists_r5
			{
				MOB_RESIST_SWORD,
				MOB_RESIST_TWOHAND,
				MOB_RESIST_DAGGER,
				MOB_RESIST_BELL,
				MOB_RESIST_FAN,
				MOB_RESIST_BOW,
				MOB_RESIST_CLAW,//r4
				MOB_RESIST_FIRE,
				MOB_RESIST_ELECT,
				MOB_RESIST_MAGIC,
				MOB_RESIST_WIND,
				MOB_RESIST_POISON,
				MOB_RESIST_BLEEDING,//r3
				MOB_RESISTS_MAX_NUM
			};

			DWORD       dwVnum;
			char        szName[CHARACTER_NAME_MAX_LEN + 1];
			char        szLocaleName[CHARACTER_NAME_MAX_LEN + 1];

			BYTE        bType;                  // Monster, NPC
			BYTE        bRank;                  // PAWN, KNIGHT, KING
			BYTE        bBattleType;            // MELEE, etc..
			BYTE        bLevel;                 // Level
			BYTE		bLvlPct;
			BYTE        bSize;//r4

			DWORD       dwGoldMin;
			DWORD       dwGoldMax;
			DWORD       dwExp;
			DWORD       dwMaxHP;
			BYTE        bRegenCycle;
			BYTE        bRegenPercent;
			WORD        wDef;

			DWORD       dwAIFlag;
			DWORD       dwRaceFlag;
			DWORD       dwImmuneFlag;

			BYTE        bStr, bDex, bCon, bInt;
			DWORD       dwDamageRange[2];

			short       sAttackSpeed;
			short       sMovingSpeed;
			BYTE        bAggresiveHPPct;
			WORD        wAggressiveSight;
			WORD        wAttackRange;

			char        cEnchants[MOB_ENCHANTS_MAX_NUM];
			char        cResists[SMobTable_r263::MOB_RESISTS_MAX_NUM];

			DWORD       dwResurrectionVnum;
			DWORD       dwDropItemVnum;

			BYTE        bMountCapacity;
			BYTE        bOnClickType;

			BYTE        bEmpire;
			char        szFolder[64 + 1];
			float       fDamMultiply;
			DWORD       dwSummonVnum;
			DWORD       dwDrainSP;
			DWORD		dwMonsterColor;
		    DWORD       dwPolymorphItemVnum;

			TMobSkillLevel	Skills[MOB_SKILL_MAX_NUM];

		    BYTE		bBerserkPoint;
			BYTE		bStoneSkinPoint;
			BYTE		bGodSpeedPoint;
			BYTE		bDeathBlowPoint;
			BYTE		bRevivePoint;

			DWORD		dwHealerPoint;//r5
			BYTE		bUnk263;//r5
		} TMobTable_r263; //brazilian only 2016/08

		typedef struct SMobTable_r275
		{
			enum EMobResists_r6
			{
				MOB_RESIST_SWORD,
				MOB_RESIST_TWOHAND,
				MOB_RESIST_DAGGER,
				MOB_RESIST_BELL,
				MOB_RESIST_FAN,
				MOB_RESIST_BOW,
				MOB_RESIST_CLAW,//r4
				MOB_RESIST_FIRE,
				MOB_RESIST_ELECT,
				MOB_RESIST_MAGIC,
				MOB_RESIST_WIND,
				MOB_RESIST_POISON,
				MOB_RESIST_BLEEDING,//r3
				MOB_RESISTS_MAX_NUM
			};

			enum EMobEnchants_6
			{
				MOB_ENCHANT_CURSE,
				MOB_ENCHANT_SLOW,
				MOB_ENCHANT_POISON,
				MOB_ENCHANT_STUN,
				MOB_ENCHANT_CRITICAL,
				MOB_ENCHANT_PENETRATE,
				MOB_ENCHANTS_MAX_NUM
			};

			DWORD       dwVnum;
			char        szName[CHARACTER_NAME_MAX_LEN + 1];
			char        szLocaleName[CHARACTER_NAME_MAX_LEN + 1];

			BYTE        bType;                  // Monster, NPC
			BYTE        bRank;                  // PAWN, KNIGHT, KING
			BYTE        bBattleType;            // MELEE, etc..
			BYTE        bLevel;                 // Level
			BYTE		bLvlPct;
			BYTE        bSize;//r4

			DWORD       dwGoldMin;
			DWORD       dwGoldMax;
			DWORD       dwExp;
			DWORD       dwMaxHP;
			BYTE        bRegenCycle;
			BYTE        bRegenPercent;
			WORD        wDef;

			DWORD       dwAIFlag;
			DWORD       dwRaceFlag;
			DWORD       dwImmuneFlag;

			BYTE        bStr, bDex, bCon, bInt;
			DWORD       dwDamageRange[2];

			short       sAttackSpeed;
			short       sMovingSpeed;
			BYTE        bAggresiveHPPct;
			WORD        wAggressiveSight;
			WORD        wAttackRange;

			char        cEnchants[SMobTable_r275::MOB_ENCHANTS_MAX_NUM];
			char        cResists[SMobTable_r275::MOB_RESISTS_MAX_NUM];
			BYTE		bUnk265[9];//r6

			DWORD       dwResurrectionVnum;
			DWORD       dwDropItemVnum;

			BYTE        bMountCapacity;
			BYTE        bOnClickType;

			BYTE        bEmpire;
			char        szFolder[64 + 1];
			float       fDamMultiply;
			DWORD       dwSummonVnum;
			DWORD       dwDrainSP;
			DWORD		dwMonsterColor;
			DWORD       dwPolymorphItemVnum;

			TMobSkillLevel	Skills[MOB_SKILL_MAX_NUM];

			BYTE		bBerserkPoint;
			BYTE		bStoneSkinPoint;
			BYTE		bGodSpeedPoint;
			BYTE		bDeathBlowPoint;
			BYTE		bRevivePoint;

			DWORD		dwHealerPoint;//r5
			BYTE		bUnk263;//r5
			BYTE		bUnk264[3];//r6
		} TMobTable_r275; //new 2018/1 mob_proto type for zodiac

		typedef TMobTable_r255 SMobTable, TMobTable;

#ifdef ENABLE_PROTOSTRUCT_AUTODETECT
		typedef struct SMobTableAll
		{
			static bool IsValidStruct(DWORD structSize)
			{
				switch (structSize)
				{
					case sizeof(TMobTable_r235):
					case sizeof(TMobTable_r255):
					case sizeof(TMobTable_r256):
					case sizeof(TMobTable_r262):
					case sizeof(TMobTable_r263):
					case sizeof(TMobTable_r275):
						return true;
						break;
				}
				return false;
			}
			
			static DWORD GetResistFromStruct(DWORD structSize, DWORD resistID)
			{
				#define MTABLE_SWITCH_RESIST(len)\
				switch (resistID)\
				{\
					case MOB_RESIST_SWORD:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_SWORD;\
						break;\
					case MOB_RESIST_TWOHAND:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_TWOHAND;\
						break;\
					case MOB_RESIST_DAGGER:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_DAGGER;\
						break;\
					case MOB_RESIST_BELL:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_BELL;\
						break;\
					case MOB_RESIST_FAN:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_FAN;\
						break;\
					case MOB_RESIST_BOW:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_BOW;\
						break;\
					case MOB_RESIST_FIRE:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_FIRE;\
						break;\
					case MOB_RESIST_ELECT:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_ELECT;\
						break;\
					case MOB_RESIST_MAGIC:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_MAGIC;\
						break;\
					case MOB_RESIST_WIND:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_WIND;\
						break;\
					case MOB_RESIST_POISON:\
						return CPythonNonPlayer::TMobTable_r##len##::MOB_RESIST_POISON;\
						break;\
				}

				switch (structSize)
				{
					case sizeof(TMobTable_r256):
					{
						MTABLE_SWITCH_RESIST(256);
					}
					break;
					case sizeof(TMobTable_r262):
					{
						MTABLE_SWITCH_RESIST(262);
					}
					break;
					case sizeof(TMobTable_r263):
					{
						MTABLE_SWITCH_RESIST(263);
					}
					break;
					case sizeof(TMobTable_r275):
					{
						MTABLE_SWITCH_RESIST(275);
					}
					break;
				}

				return resistID;
			}

			static void Process(void* obj, DWORD structSize, DWORD i, CPythonNonPlayer::TMobTable& t)
			{
				#define MGET_RESIST2(resistSTR) CPythonNonPlayer::TMobTableAll::GetResistFromStruct(structSize, CPythonNonPlayer::MOB_RESIST_##resistSTR##)
				#define MGET_RESIST(resistID) CPythonNonPlayer::TMobTableAll::GetResistFromStruct(structSize, resistID)
				#define MTABLE_COPY_STR(x) strncpy_s(t.##x##, sizeof(t.##x##), r.##x##, _TRUNCATE)
				#define MTABLE_COPY_INT(x) t.##x## = r.##x
				#define MTABLE_COPY_INT2(x, y) t.##x## = r.##y
				#define MTABLE_COPY_FLT(x) t.##x## = r.##x
				#define MTABLE_COUNT(x) _countof(t.##x##)
				#define MTABLE_PROCESS(len)\
					CPythonNonPlayer::TMobTable_r##len## & r = *((CPythonNonPlayer::TMobTable_r##len## *) obj + i);\
					MTABLE_COPY_INT(dwVnum);\
					MTABLE_COPY_STR(szName);\
					MTABLE_COPY_STR(szLocaleName);\
					MTABLE_COPY_INT(bType);\
					MTABLE_COPY_INT(bRank);\
					MTABLE_COPY_INT(bBattleType);\
					MTABLE_COPY_INT(bLevel);\
					MTABLE_COPY_INT(bSize);\
					MTABLE_COPY_INT(dwGoldMin);\
					MTABLE_COPY_INT(dwGoldMax);\
					MTABLE_COPY_INT(dwExp);\
					MTABLE_COPY_INT(dwMaxHP);\
					MTABLE_COPY_INT(bRegenCycle);\
					MTABLE_COPY_INT(bRegenPercent);\
					MTABLE_COPY_INT(wDef);\
					MTABLE_COPY_INT(dwAIFlag);\
					MTABLE_COPY_INT(dwRaceFlag);\
					MTABLE_COPY_INT(dwImmuneFlag);\
					MTABLE_COPY_INT(bStr);\
					MTABLE_COPY_INT(bDex);\
					MTABLE_COPY_INT(bCon);\
					MTABLE_COPY_INT(bInt);\
					for (size_t i=0; i<MTABLE_COUNT(dwDamageRange); ++i)\
					{\
						MTABLE_COPY_INT(dwDamageRange[i]);\
					}\
					MTABLE_COPY_INT(sAttackSpeed);\
					MTABLE_COPY_INT(sMovingSpeed);\
					MTABLE_COPY_INT(bAggresiveHPPct);\
					MTABLE_COPY_INT(wAggressiveSight);\
					MTABLE_COPY_INT(wAttackRange);\
					for (size_t i=0; i<MTABLE_COUNT(cEnchants); ++i)\
					{\
						MTABLE_COPY_INT(cEnchants[i]);\
					}\
					for (size_t i=0; i<MTABLE_COUNT(cResists); ++i)\
					{\
						MTABLE_COPY_INT2(cResists[i], cResists[GetResistFromStruct(structSize, i)]);\
					}\
					MTABLE_COPY_INT(dwResurrectionVnum);\
					MTABLE_COPY_INT(dwDropItemVnum);\
					MTABLE_COPY_INT(bMountCapacity);\
					MTABLE_COPY_INT(bOnClickType);\
					MTABLE_COPY_INT(bEmpire);\
					MTABLE_COPY_STR(szFolder);\
					MTABLE_COPY_FLT(fDamMultiply);\
					MTABLE_COPY_INT(dwSummonVnum);\
					MTABLE_COPY_INT(dwDrainSP);\
					MTABLE_COPY_INT(dwMonsterColor);\
					MTABLE_COPY_INT(dwPolymorphItemVnum);\
					for (size_t i=0; i<MTABLE_COUNT(Skills); ++i)\
					{\
						MTABLE_COPY_INT(Skills[i].dwVnum);\
						MTABLE_COPY_INT(Skills[i].bLevel);\
					}\
					MTABLE_COPY_INT(bBerserkPoint);\
					MTABLE_COPY_INT(bStoneSkinPoint);\
					MTABLE_COPY_INT(bGodSpeedPoint);\
					MTABLE_COPY_INT(bDeathBlowPoint);\
					MTABLE_COPY_INT(bRevivePoint);

				switch (structSize)
				{
					case sizeof(TMobTable_r235):
					{
						MTABLE_PROCESS(235);
					}
					break;
					case sizeof(TMobTable_r255):
					{
						MTABLE_PROCESS(255);
					}
					break;
					case sizeof(TMobTable_r256):
					{
						MTABLE_PROCESS(256);
					}
					break;
					case sizeof(TMobTable_r262):
					{
						MTABLE_PROCESS(262);
					}
					break;
					case sizeof(TMobTable_r263):
					{
						MTABLE_PROCESS(263);
					}
					break;
					case sizeof(TMobTable_r275):
					{
						MTABLE_PROCESS(275);
					}
 					break;
				}
			}
		} TMobTableAll;
#endif //ENABLE_PROTOSTRUCT_AUTODETECT

#pragma pack(pop)

		typedef std::list<TMobTable *> TMobTableList;
		typedef std::map<DWORD, TMobTable *> TNonPlayerDataMap;

	public:
		CPythonNonPlayer(void);
		virtual ~CPythonNonPlayer(void);

		void Clear();
		void Destroy();

		bool				LoadNonPlayerData(const char * c_szFileName);

		const TMobTable *	GetTable(DWORD dwVnum);
		bool				GetName(DWORD dwVnum, const char ** c_pszName);
		bool				GetInstanceType(DWORD dwVnum, BYTE* pbType);
		BYTE				GetEventType(DWORD dwVnum);
		BYTE				GetEventTypeByVID(DWORD dwVID);
		DWORD				GetMonsterColor(DWORD dwVnum);
		const char*			GetMonsterName(DWORD dwVnum);

#if defined(WJ_SHOW_MOB_INFO) && defined(ENABLE_SHOW_MOBLEVEL)
		DWORD				GetMonsterLevel(DWORD dwVnum);
#endif

#if defined(WJ_SHOW_MOB_INFO) && defined(ENABLE_SHOW_MOBAIFLAG)
		bool				IsAggressive(DWORD dwVnum);
#endif

		// Function for outer
		void				GetMatchableMobList(int iLevel, int iInterval, TMobTableList * pMobTableList);

	protected:
		TNonPlayerDataMap	m_NonPlayerDataMap;
};