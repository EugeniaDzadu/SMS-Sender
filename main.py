from requests import get
def sms_database():
     sms_input = int(input('****Welcome to SMS Sender**** \n'
                      '1.Send SMS \n'
                      '2. Check balance \n'
                   
                      '3. Exit App \n\n'
                      'Provide option:'))
     return sms_input
 
def user_option(sms_input):
    if sms_input == 1:
        send_sms()
        
    elif sms_input == 2:
       check_balance()
   
    elif sms_input == 3:
        print('Thanks for using our platform')
        exit 
    else:
        print('Invalid response, try again')

    option = sms_database()
    user_option(option)   

def send_sms():
    type_sms = input('Enter SMS Content:')
    receipient_sms = input('Enter Receipient:')
    send_sms = input('Enter Sender ID:')
    
    results = content(receipient_sms, type_sms, send_sms)
    print(results)
    
def content(to,msg,sender):
    results = get(f'http://sms.smsnotifygh.com/smsapi?key=48485dee-500e-4634-97a1-76342c62346f&to={to}&msg={msg}&sender_id={sender}')
    return results.text
    
    
    
def check_balance():
    balance = get('http://sms.smsnotifygh.com/api/smsapibalance?key=48485dee-500e-4634-97a1-76342c62346f')
    balances = balance.text
    print(f'Your balance is GHC{balances}')


option = sms_database()
user_option(option)