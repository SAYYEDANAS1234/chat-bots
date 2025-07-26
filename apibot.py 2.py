from groq import Groq

client = Groq(
    api_key="YOUR_API_KEY"
)
while True :

      user_input=input("yo:")
      if user_input== "quit":
            print ("bot: goodbye!")
            break
      response = client.chat.completions.create(
           model="llama3-70b-8192",
           messages=[
                {"role": "user", "content": user_input}
    ]
)
      print("bot:", response.choices[0].message.content)
      

