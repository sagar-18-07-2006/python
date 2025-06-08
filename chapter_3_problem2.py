a =input("name of you")
date = input("enter date in DD/MM/YYYY format")
print(f"Dear {a}")
print("You are selected")
print(f"{date}")
# second option
letter ="""Dear <|Name|>
           You Are Selected
          <|Date|>"""
print(letter.replace("<|Name|>" , "Sagar").replace("<|Date|>" , "08/06/2025"))