pw=[]
inputa = map(int, input("Please type in the code you would like to encode: ").split())
pw = list(inputa)
length=len(pw)
encoded=[]
decoded=[]


def encoder(val):
  final=val+3
  return final


def decoder(vala):
  finala=vala-3
  return finala


for i in range(length):
  val=pw[i]
  encoded.append(encoder(val))


print("This is the encoded code: ", end="")
for k in range(length):
  print(encoded[k], end="")


for j in range(length):
  vala=encoded[j]
  decoded.append(decoder(vala))


print("\nThis is the decoded code: ", end="")


for f in range(length):
  print(decoded[f], end="")

