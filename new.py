from requests import get
def sms_database():
    sms_input = int(input('****Welcome to SMS Sender**** \n'
                      '1.Send SMS \n'
                      '2. Check balance \n'
                      '3. Exit App \n\n'
                      'Provide option: '))
    return sms_input

def user_option(sms_input):
    if sms_input == 1:
        send_sms()
    
    elif sms_input == 2:
        pass
    
    elif sms_input == 3:
        print("Thanks for using our platform")
        exit
        
    else:
        print("Invalid user option")
        
    option = sms_database()
    user_option(option)
    
def send_sms():
    content = input("Enter sms: ")
    recipient = input("Enter recipient: ")
    sender_id = input("Enter sender_id: ")
    
    res = sms_content(content, recipient, sender_id)
    print(res)
    
def sms_content(to, msg, sender):
    res = get(f"http://sms.smsnotifygh.com/smsapi?key=583f400837f3057d6276&to={to}&msg={msg}&sender_id={sender}")
    return res.text

option = sms_database()
user_option(option)