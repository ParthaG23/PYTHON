latter='''Dear <|name|> you are selected! 
        your joning date is <|date|>'''
name=input("Enter your name: ")
date=input("Enter a date:")
latter=latter.replace("<|name|>",name)
latter=latter.replace("<|date|>",date)
print(latter)