import google.generativeai as ai 

    
   


Api_Key = 'AIzaSyDrLp8xuAScNrBHc0Y81qEcUBEVthuOV1c'

ai.configure(api_key = Api_Key)

model =ai.GenerativeModel("gemini-pro")
chat =model.start_chat()
thank =['bye','goodbye','tschuss']
while True:
    message = input('You:')
    if message == "" :
        message = "i need your assistance"
    if message.lower() in thank:
        print('chatbot: GoodBye!')
        break
    response= chat.send_message(message)
    print('chatbot:',response.text)