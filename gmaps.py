import sys,pyperclip,webbrowser

if len(sys.argv)>1:
    ad='+'.join(sys.argv[1:])
else:
    ads=input("Enter address: ")
    l=ads.split()
    ad="+".join(l[:])

webbrowser.open("https://www.google.com/maps/place/"+ad)
