import requests
import random
meldung = "Dieses Video ist nicht mehr verfügbar"
meldung2 = "Dieses Video ist nicht mehr verfügbar"
pattern = '"playabilityStatus":{"status":"ERROR","reason":"Dieses Video ist nicht mehr verfügbar"'
base64_chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"0","1","2","3","4","5","6","7","8","9","-","_"]
ids = []
correct = []
true_val = 0
true_vids = []
false_val = 0
for i in range(1000):
    vid = ""
    for j in range(11):
        vid += base64_chars[random.randint(0, 63)]
    ids.append(vid)

for i in ids:
    link = "https://youtu.be/"+str(i)
    r = requests.get(link)
    #print(r.text)
    if meldung in r.text or meldung2 in r.text:
        correct.append(False)
        false_val += 1
    else:
        correct.append(True)
        true_vids.append(link)
        true_val += 1

print("false: " +str(false_val))
print("true: " +str(true_val))
for i in true_vids:
    print(i)
    