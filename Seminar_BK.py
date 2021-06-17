from bitcoinrpc.authproxy import AuthServiceProxy

def main():
    print("Molimo unesite pristupne podatke za poslužitelj:\n")
    node = input("Molimo unesite puni naziv hosta:\n")
    user = input("Molimo unesite korisničko ime:\n")
    port = input("Molimo unesite port:\n")
    password = input("Molimo unesite lozinku:\n")

    link = "http://" + user + ":" + password + "@" + node + ":" + port
    rpc_connection = AuthServiceProxy(link)
    
    #hash headera najnovijeg bloka u najboljem blockchainu
    block = rpc_connection.getbestblockhash()

    #informacije o bloku izvučene preko hasha api pozivom getblock, 1 je za vađenje json bloka
    block_information = rpc_connection.getblock(block, 1)
    print("Hash bloka: ", block_information['hash'])
    print("Vrijeme bloka od 1.1.1970: ", block_information['time'])
    print("Velicina bloka (byte): ", block_information['size'])
    print("Tezina bloka: ", block_information['weight'])
    print("Visina bloka: ", block_information['height'])
    print("Verzija bloka: ", block_information['version'])
    print("Nonce bloka: ", block_information['nonce'])
    print("Poteškoća bloka: ", block_information['difficulty'])
    print("Korijen merkle: ", block_information['merkleroot'])
    print("Broj potvrda: ", block_information['confirmations'])
    print("Broj transakcija u bloku: ", block_information['nTx'])    
    print("\n")
    print("\n")

    #getblockstats računa statistiku po bloku
    statistics_per_block = rpc_connection.getblockstats(block)
    print("Nagrada za rudarenje bloka :", statistics_per_block['subsidy'],"Satoshija")
    print("Maksimalna naknada je :", statistics_per_block['maxfee'],"Satoshija")
    print("Stopa maksimalne naknade je :", statistics_per_block['maxfeerate'],"Satoshija po virtualnom bajtu")    
    print("Minimalna naknada je :", statistics_per_block['minfee'],"Satoshija") 
    print("Stopa minimalne naknade je :", statistics_per_block['minfeerate'],"Satoshija po virtualnom bajtu")
    print("Broj transakcija (bez coinbase transakcija) :", statistics_per_block['txs'])
    print("\n")
    print("\n")
    
    #getblockchaininfo daje informacije o trenutnom stanju blockchaina
    blockchain = rpc_connection.getblockchaininfo()
    print("Ime mreže po BIP70: ",blockchain['chain'])
    print("Trenutni broj blokova: ",blockchain['blocks'])
    print("Trenutni broj headera koji su validirani: ",blockchain['headers'])
    print("Hash najboljeg bloka: ",blockchain['bestblockhash'])
    print("Trenutna poteškoća: ",blockchain['difficulty'])
    print("Verifikacija: ",blockchain['verificationprogress'])
    print("Procjena jeli čvor u modu Initial Block Download: ",blockchain['initialblockdownload'])
    print("Veličina bloka i undo fileova na disku: ",blockchain['size_on_disk'],"bajtova")
    print("Upozorenja vezana za mrežu i blockchain: ",blockchain['warnings'])
    print("\n")
    print("\n")
    
    #getmempoolinfo vraća informacije o trenutnom mempoolu transakcija čvora
    mempool = rpc_connection.getmempoolinfo()
    print("Trenutni broj transakcija: ", mempool['size'])
    print("Zbroj svih virtualnih veličina transakcija: ", mempool['bytes'])
    print("Ukupna zauzeta memorija mempoolom: ", mempool['usage'], "bajtova")
    print("Maksimalna iskorištena memorija za mempool: ", mempool['maxmempool'], "megabajta")
    print("Minimalna stopa naknade u BTC/kB da bi se transakcija prihvatila: ", mempool['mempoolminfee'], "megabajta")
    print("Trenutna najmanji relay fee za transakciju: ", mempool['minrelaytxfee'],"BTC/kb")
    print("\n")
    print("\n")

    #getdifficulty vraća proof-of-work poteškoću kao umnožak minimalne poteškoće
    print("Poteškoća:",rpc_connection.getdifficulty())
    print("\n")
    print("\n")
    
    #addnode dodaje, miče ili se jednom pokušava povezati na čvor(add, remove ili onetry)
    rpc_connection.addnode(node, 'add')
    
    #getaddednodeinfo vraća informacije o dodanom čvoru ili svim dodanim čvorovima(ručno dodanim), osim onetry čvorova. 
    node_details = rpc_connection.getaddednodeinfo(node)
    print("Dodani čvor: ", node_details[0]['addednode'])

    #getconnectioncount daje broj konekcija na ostale čvorove
    print("Broj konekcija : ", rpc_connection.getconnectioncount())
    
    #uptime vraća broj sekundi koliko je server upaljen
    print("Server je upaljen: ", rpc_connection.uptime(), "sekunda.")
    
    #getnetworkinfo vraća informacije o vezi čvora sa mrežom
    network_details = rpc_connection.getnetworkinfo()
    print("Verzija servera: ", network_details['version'])
    print("Verzija protokola: ", network_details['protocolversion'])
    print("P2P mreža je dozvoljena?: ", network_details['networkactive'])
    print("Minimalna relay naknada za transakcije: ", network_details['version'],"BTC/kB")
    print("\n")

    #pretraga hasha bloka u najboljem blockchainu(bloka kojem unesemo visinu)
    print("Ispis hasha traženog bloka u naboljem blockchainu za unesenu visinu.\n")
    entry= int(input('Unesite visinu bloka za kojeg treba ispisati hash: '))
    search = rpc_connection.getblockhash(entry)
    print("Hash: ", search)
    
    rpc_connection.addnode(node, 'remove')
main()
