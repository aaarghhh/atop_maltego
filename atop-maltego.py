import json
import atop
import datetime
from MaltegoTransform import *

###  CREATE TON ACCOUNT AMOUNT ADDRESS
###  CREATE 

asset=sys.argv[1]

def scan_ton():
    current_parser = atop.atop.Ton_retriever(asset,False,False)
    current_parser.start_searching()

    ### TO PROCESS DATA
    trx = MaltegoTransform()

    if current_parser.owner_name != "":
        print("###TODO handle name ", )

    if current_parser.info != "":
        print("###TODO handle info ", )

    if current_parser.transactions and len(current_parser.transactions):
        last_date = datetime.fromtimestamp(current_parser.transactions[0]["utime"])
        print("###TODO handle last date ", )

    if current_parser.nfts:
        if "data" in current_parser.nfts.keys():
            if "nftItemsByOwner" in current_parser.nfts["data"].keys():
                processnft = True

    if processnft:
        first = True
        for nftff in current_parser.nfts["data"]["nftItemsByOwner"]["items"]:
            print("###TODO handle Address:")
            print("###TODO handle Name:")
            print("###TODO handle Kind:")
            print("###TODO handle Collection:")
            print("###TODO handle Url:")

    try:
            trx.addEntity("maltego.TonAddress", str(publicEmail)).setNote("Public Email")
    except:
        pass

if __name__ == '__main__':
    scan_ton()
