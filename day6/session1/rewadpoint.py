class VISACARD:
    def __init__(self,holder_name,card_number):
        self.holder_name=holder_name
        self.card_number=card_number
        
    def display_details(self):
        print(self.holder_name)
        print(self.card_number)
    def computer_rewards(self,purchase_type,amount):
        reward=amount*0.01
        print("reward for visa is :",reward)
class HPVISACARD(VISACARD):
    def computer_rewards(self,purchase_type,amount):
        reward=amount*0.01
        if purchase_type=="FUEL":
            reward+=10
        print("reward for HPVISA is :",reward)
        
        
card_type=input("enter VISA/HPVISA").strip()
if card_type not in ["VISA","HPVISA"]:
    print("invalid card choice")
else:
    holder_name=input("enetr the name :").strip()
    card_number=input("enter the card number :").strip()    
    amount=float(input("enetr the amount"))
    purchase_type=input("enter the purchase typr :").strip()
    
    if card_type=="VISA":
        card=VISACARD(holder_name,card_number)
    else:
        card=HPVISACARD(holder_name,card_number)
    card.display_details()
    card.computer_rewards(purchase_type,amount)
    