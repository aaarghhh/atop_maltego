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

<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218276173-a65c04f9-dc35-4f88-b5e0-233fb9624f1f.png" />
</p>
After that,  we have to install the Entity package `atop.mtx`

<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218276399-24639bdb-1563-4351-8251-7ef9176ae720.png" />
</p>

We'll be able to see and use all the new entities imported. Eech entity has 2 properties the address and the name attribute. The TON address entity will contain information about the current balance and the related nickname used by the owner.
<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218276509-8ccb7585-1b90-4ef1-a1dd-c67e8f2ad650.png" />
</p>

### CREATION OF EACH TRANSFORM

Unfortunately each transfor must be created manually.   
  
**STEP #1**: Select "Add Local Transform" and complete the form like the image below. As you can see in "Imput Entity Type" this transform will work only for the standard "Phone Maltego entity".  
<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218277527-5614115e-3f16-462d-8461-b8e38fb77b89.png" />
</p>

**STEP #2**:
In the next part of the form, we'll be able to set the path of the atop-maltego.py script.  
<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218277566-6ba9d4bf-4d48-4b35-83e3-278e0dbd7263.png" />
</p>

> To enable Domain and nickname transform we have to follow STEP1 and STEP2 and create 2 new local transforms.  

The domain transform will be created as "Domain Maltego alias" for "Imput Entity Type".  
<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218285951-9b94de85-52b3-4c1f-9e94-24655f1a6a65.png" />
</p>

To enable the nickname transform, we have to create a new Maltego transform related to an "Alias Maltego alias" as "Imput Entity Type".
<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218286016-51b4ebcc-2ca7-4286-b15c-54b51ad06c70.png" />
</p>

## EXECUTION

From a Domain, Alias or Telephone entity we'll be able to selecte the relating ATOP transform. Launching the procedure, Maltego will render all identified assets. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218276997-a2f36ce8-706b-456e-bdfb-53fc6b518a82.png" />
</p>
The graph will contains TON domain, nickname, domains and NFT related to an identified TON owner. **For a domain search, ATOP will make an extra pivoting trying to identify any possible ENS domain**, in this case ETH address and a first related ENS domain will added to the relations.
<p align="center">
  <img src="https://user-images.githubusercontent.com/968839/218277133-507e7c44-fad3-44ca-8a13-d25e51c1fa5b.png" />
</p>
Keep in mind that Maltego CE supports only 12 new entity for single transform so the result could be incomplete. 






