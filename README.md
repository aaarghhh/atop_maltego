# ATOP Maltego Transform
A new Maltego transform useful to make  inestigations on TON assets like TON nickname, TON dns and TON Telephone Number. These kind of entities are NFT based on TON network. The transfor is base on [ATOP](https://github.com/aaarghhh/a_TON_of_privacy).  

```
 ▄▄▄         ▄▄▄█████▓ ▒█████   ███▄    █     ▒█████    █████▒   
▒████▄       ▓  ██▒ ▓▒▒██▒  ██▒ ██ ▀█   █    ▒██▒  ██▒▓██   ▒    
▒██  ▀█▄     ▒ ▓██░ ▒░▒██░  ██▒▓██  ▀█ ██▒   ▒██░  ██▒▒████ ░    
░██▄▄▄▄██    ░ ▓██▓ ░ ▒██   ██░▓██▒  ▐▌██▒   ▒██   ██░░▓█▒  ░    
 ▓█   ▓██▒     ▒██▒ ░ ░ ████▓▒░▒██░   ▓██░   ░ ████▓▒░░▒█░       
 ▒▒   ▓▒█░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ▒░▒░▒░  ▒ ░       
  ▒   ▒▒ ░       ░      ░ ▒ ▒░ ░ ░░   ░ ▒░     ░ ▒ ▒░  ░         
  ░   ▒        ░      ░ ░ ░ ▒     ░   ░ ░    ░ ░ ░ ▒   ░ ░       
      ░  ░                ░ ░           ░        ░ ░             
                                                                 
 ██▓███   ██▀███   ██▓ ██▒   █▓ ▄▄▄       ▄████▄▓██   ██▓        
▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▒████▄    ▒██▀ ▀█ ▒██  ██▒        
▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒██  ▀█▄  ▒▓█    ▄ ▒██ ██░        
▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▐██▓░        
▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░   ▓█   ▓██▒▒ ▓███▀ ░░ ██▒▓░        
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░   ▒▒   ▓▒█░░ ░▒ ▒  ░ ██▒▒▒         
░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░    ▒   ▒▒ ░  ░  ▒  ▓██ ░▒░         
░░         ░░   ░  ▒ ░     ░░    ░   ▒   ░       ▒ ▒ ░░          
            ░      ░        ░        ░  ░░ ░     ░ ░             
                           ░             ░       ░ ░   
```

## REQUIREMENTS
To run ATOP Maltego transform you need:
- Python3 and pip 
- Install atop `pip install "atop>=0.0.2-08"`
- Install Maltego CE
- Choose a directory where your local transform will be downloaded and clone this repo `git clone https://github.com/aaarghhh/atop_maltego.git`
- Install Entities from the packege atop.mtz
- Create three new local transform in Maltego CE

## INSTALLATION

Firstly, we have to download the project and copy or directly clone it in a directory related to **atop_maltego**. We have to keep in mind that Maltego will call the python script directly like a common command executed by a CLI. 

![001](https://user-images.githubusercontent.com/968839/218276173-a65c04f9-dc35-4f88-b5e0-233fb9624f1f.png)

Adter that we have to install the Entity package `atop.mtx`
![002](https://user-images.githubusercontent.com/968839/218276399-24639bdb-1563-4351-8251-7ef9176ae720.png)

We'll be able to see all the new entities imported.
![003](https://user-images.githubusercontent.com/968839/218276509-8ccb7585-1b90-4ef1-a1dd-c67e8f2ad650.png)

## EXECUTION



