p1="make a lot of copy"
p2="buy now"
p3="subscribe now"
p4="click this"
msg=input("enter your message..>")
if (msg in p1) or (msg in p2) or (msg in p3) or (msg in p4):
    print("it is spam protect your pc ..")
else:
    print("not spam...")