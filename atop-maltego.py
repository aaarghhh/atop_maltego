from atop.atop import *
from MaltegoTransform import *
from dotenv import dotenv_values

asset_maltego = sys.argv[1]

try:
    config = dotenv_values(".env")
except:
    pass


def check_format(_string):
    if re.match(r"\+?888[0-9\s]{0,12}", _string.strip()):
        return "NUMBER"
    if re.match(r"[a-z0-9-_]+\.ton", _string.strip()):
        return "DOMAIN"
    if re.match(r"@[a-z0-9_]", _string.strip()):
        return "NICKNAME"
    return "NONE"


def scan_ton():
    search_maltego = asset_maltego.lower()
    if check_format(search_maltego) == "NONE":
        search_maltego = "@" + search_maltego

    try:
        telegram_pivot = True

        if len(config) == 0 or (
            not config["API_ID"]
            or not config["API_HASH"]
            or not config["SESSION_STRING"]
        ):
            telegram_pivot = False

        # print("telegram input --> " + search_maltego, str(True), str(False), str(True), "pivot: "+str(telegram_pivot), "---", config["API_ID"],
        #                               config["API_HASH"],"---", config["SESSION_STRING"])
        # print("telegram pivot:  " + str(telegram_pivot))

        if telegram_pivot:
            current_parser = Ton_retriever(
                search_maltego,
                True,
                False,
                True,
                telegram_pivot,
                None,
                config["API_HASH"],
                config["API_ID"],
                None,
                config["SESSION_STRING"],
            )
        else:
            current_parser = Ton_retriever(
                search_maltego, True, False, True, telegram_pivot
            )
        current_parser.start_searching()
    except Exception as exx:
        print(f"we got some problem, {exx}")
        exit(0)

    trx = MaltegoTransform()
    if current_parser.address != "":
        extra_attributes = []
        extra_attributes.append(
            [
                "balance",
                "Balance",
                "balance",
                str(
                    round(int(current_parser.info["result"]["balance"]) / 1000000000, 2)
                ),
            ]
        )
        if current_parser.owner_name != "":
            extra_attributes.append(
                ["nickname", "Nickname", "nickname", current_parser.owner_name]
            )

        entity = MaltegoEntity(
            "atop.TONaddress", current_parser.address, extra_attributes
        )
        trx.entities.append(entity)

    if current_parser.nfts:
        if "data" in current_parser.nfts.keys():
            if "nftItemsByOwner" in current_parser.nfts["data"].keys():
                for item in current_parser.nfts["data"]["nftItemsByOwner"]["items"]:
                    extra_attributes = []
                    extra_attributes.append(
                        ["address", "Address", "address", item["address"]]
                    )
                    special = False
                    entity = None

                    if "collection" in item.keys() and item["collection"]:
                        if "Usernames" in item["collection"]["name"]:
                            entity = MaltegoEntity(
                                "atop.TONnickname", item["name"], extra_attributes
                            )
                            special = True
                        if "Numbers" in item["collection"]["name"]:
                            entity = MaltegoEntity(
                                "atop.TONtelephonenumber",
                                item["name"],
                                extra_attributes,
                            )
                            special = True
                        if "TON DNS" in item["collection"]["name"]:
                            entity = MaltegoEntity(
                                "atop.TONdomain", item["name"], extra_attributes
                            )
                            special = True
                    if not special:
                        entity = MaltegoEntity(
                            "atop.TONnft", item["name"], extra_attributes
                        )
                    trx.entities.append(entity)

                    id = ""
                    name = ""
                    nickname = ""
                    kind = ""
                    photo = ""
                    description = ""
                    partecipants = ""

                    if "tg-data" in item.keys():
                        if "apidetail" in item["tg-data"][2].keys():
                            id = str(item["tg-data"][2]["apidetail"].id)
                            if item["tg-data"][2]["apidetail"].first_name:
                                name = name + item["tg-data"][2]["apidetail"].first_name
                            if item["tg-data"][2]["apidetail"].last_name:
                                name = name + item["tg-data"][2]["apidetail"].last_name

                        if "webdetail" in item["tg-data"][2].keys():
                            if (
                                item["tg-data"][2]["webdetail"]["nickname"]
                                and item["tg-data"][2]["webdetail"]["nickname"] != "N/A"
                            ):
                                nickname = item["tg-data"][2]["webdetail"]["nickname"]

                            if (
                                item["tg-data"][2]["webdetail"]["kind"]
                                and item["tg-data"][2]["webdetail"]["kind"] != "N/A"
                            ):
                                kind = item["tg-data"][2]["webdetail"]["kind"]

                            if (
                                item["tg-data"][2]["webdetail"]["participants"]
                                and item["tg-data"][2]["webdetail"]["participants"]
                                != "N/A"
                            ):
                                partecipants = item["tg-data"][2]["webdetail"][
                                    "participants"
                                ]

                            if (
                                item["tg-data"][2]["webdetail"]["image"]
                                and item["tg-data"][2]["webdetail"]["image"] != "N/A"
                            ):
                                photo = item["tg-data"][2]["webdetail"]["image"]

                            if (
                                item["tg-data"][2]["webdetail"]["description"]
                                and item["tg-data"][2]["webdetail"]["description"]
                                != "N/A"
                            ):
                                description = item["tg-data"][2]["webdetail"][
                                    "description"
                                ]

                        extra_attributes = []
                        extra_attributes.append(["id", "Id", "id", id])
                        extra_attributes.append(["name", "Name", "name", name])
                        extra_attributes.append(
                            ["nickname", "Nickname", "nickname", nickname]
                        )
                        extra_attributes.append(["kind", "Kind", "kind", kind])
                        extra_attributes.append(
                            ["description", "Description", "description", description]
                        )
                        extra_attributes.append(
                            ["affiliates", "Affiliates", "affiliates", description]
                        )

                        entityTG = MaltegoEntity(
                            "atop.TelegramEntity", id, extra_attributes
                        )
                        trx.entities.append(entityTG)

                        if photo != "" and photo != "N/A":
                            extra_attributes = []
                            extra_attributes.append(["url", "Url", "url", photo])
                            tgPhoto = MaltegoEntity(
                                "maltego.Image", photo, extra_attributes
                            )
                            trx.entities.append(tgPhoto)

    if current_parser.ens_detail:
        if "data" in current_parser.ens_detail.keys():
            if "domains" in current_parser.ens_detail["data"].keys():
                if len(current_parser.ens_detail["data"]["domains"]) > 0:
                    entity = MaltegoEntity(
                        "maltego.ETHAddress",
                        current_parser.ens_detail["data"]["domains"][0]["owner"]["id"],
                    )
                    trx.entities.append(entity)
                    entity = MaltegoEntity(
                        "atop.ENSdomain",
                        current_parser.ens_detail["data"]["domains"][0]["name"],
                    )
                    trx.entities.append(entity)
    print(trx.returnOutput())


if __name__ == "__main__":
    scan_ton()
