from atop.atop import *
from MaltegoTransform import *

asset_maltego = sys.argv[1]


def check_format(_string):
    if re.match(r"\+?888[0-9\s]{0,12}", _string.strip()):
        return "NUMBER"
    if re.match(r"[a-z0-9-_]+\.ton", _string.strip()):
        return "DOMAIN"
    if re.match(r"@[a-z0-9]", _string.strip()):
        return "NICKNAME"
    return "NONE"


def scan_ton():

    search_maltego = asset_maltego.lower()
    if check_format(search_maltego) == "NONE":
        search_maltego = "@" + search_maltego

    try:
        current_parser = Ton_retriever(search_maltego, True, False, True)
        current_parser.start_searching()
    except Exception as exx:
        print("we got some problem")

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
