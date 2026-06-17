class VaisalaIconURL:
    BASE_URL = "https://raw.githubusercontent.com/komunidad-global/xweather_icons/main/icons"

    ICON_MAP = {
        "1001": "blizzard",
        "1002": "blizzardn",
        "1003": "blowingsnow",
        "1004": "blowingsnown",
        "1005": "clear",
        "1006": "clearn",
        "1007": "clearw",
        "1008": "clearwn",
        "1009": "cloudy",
        "1010": "cloudyn",
        "1011": "cloudyw",
        "1012": "cloudywn",
        "1013": "cold",
        "1014": "coldn",
        "1015": "drizzle",
        "1016": "drizzlef",
        "1017": "drizzlen",
        "1018": "dust",
        "1019": "dustn",
        "1020": "fair",
        "1021": "fairn",
        "1022": "fdrizzle",
        "1023": "fdrizzlen",
        "1024": "flurries",
        "1025": "flurriesn",
        "1026": "flurriesw",
        "1027": "flurrieswn",
        "1028": "fog",
        "1029": "fogn",
        "1030": "freezingrain",
        "1031": "freezingrainn",
        "1032": "hazy",
        "1033": "hazyn",
        "1034": "hot",
        "1035": "mcloudy",
        "1036": "mcloudyn",
        "1037": "mcloudyr",
        "1038": "mcloudyrn",
        "1039": "mcloudyrw",
        "1040": "mcloudyrwn",
        "1041": "mcloudys",
        "1042": "mcloudysf",
        "1043": "mcloudysfn",
        "1044": "mcloudysfw",
        "1045": "mcloudysfwn",
        "1046": "mcloudysn",
        "1047": "mcloudysw",
        "1048": "mcloudyswn",
        "1049": "mcloudyt",
        "1050": "mcloudytn",
        "1051": "mcloudytw",
        "1052": "mcloudytwn",
        "1053": "mcloudyw",
        "1054": "mcloudywn",
        "1055": "na",
        "1056": "pcloudy",
        "1057": "pcloudyn",
        "1058": "pcloudyr",
        "1059": "pcloudyrn",
        "1060": "pcloudyrw",
        "1061": "pcloudyrwn",
        "1062": "pcloudys",
        "1063": "pcloudysf",
        "1064": "pcloudysfn",
        "1065": "pcloudysfw",
        "1066": "pcloudysfwn",
        "1067": "pcloudysn",
        "1068": "pcloudysw",
        "1069": "pcloudyswn",
        "1070": "pcloudyt",
        "1071": "pcloudytn",
        "1072": "pcloudytw",
        "1073": "pcloudytwn",
        "1074": "pcloudyw",
        "1075": "pcloudywn",
        "1076": "rain",
        "1077": "rainandsnow",
        "1078": "rainandsnown",
        "1079": "rainn",
        "1080": "raintosnow",
        "1081": "raintosnown",
        "1082": "rainw",
        "1083": "showers",
        "1084": "showersn",
        "1085": "showersw",
        "1086": "showerswn",
        "1087": "sleet",
        "1088": "sleetn",
        "1089": "sleetsnow",
        "1090": "sleetsnown",
        "1091": "smoke",
        "1092": "smoken",
        "1093": "snow",
        "1094": "snowflurries",
        "1095": "snown",
        "1096": "snowshowers",
        "1097": "snowshowersn",
        "1098": "snowshowersw",
        "1099": "snowshowerswn",
        "1100": "snowtorain",
        "1101": "snowtorainn",
        "1102": "snoww",
        "1103": "sunny",
        "1104": "sunnyn",
        "1105": "sunnyw",
        "1106": "tstorm",
        "1107": "tstormn",
        "1108": "tstorms",
        "1109": "tstormsn",
        "1110": "tstormsw",
        "1111": "tstormswn",
        "1112": "wind",
        "1113": "windy",
        "1114": "wintrymix",
        "1115": "wintrymixn"
    }

    @classmethod
    def get_icon_url(cls, code) -> str:
        code_str = str(code)

        # Ensure the string is 5 characters long by padding at the end
        code_str = code_str.ljust(5, '0')

        # remove last digit due to old api add 1 or 0 to determine if night or day. Not needed here
        key = code_str[:-1] 

        icon_name = cls.ICON_MAP.get(key)
        if icon_name is None:
            raise ValueError(f"Unknown icon code: {code} (stripped key {key})")

        filename = f"{icon_name}.png"
        return f"{cls.BASE_URL}/{filename}"



# Sample
# print(VaisalaIconURL.get_icon_url(1001))