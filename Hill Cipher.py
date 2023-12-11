oldciphertext = input("Input ciphertext: ")
old2ciphertext = oldciphertext.replace(" ","")
ciphertext = old2ciphertext.lower()
Ctext = []
plaintext = ""
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for letter in ciphertext:
    Ctext.append(letter)
print(Ctext)
size = len(Ctext)
Matrix1 = int(input("Input first num of matrix: "))
Matrix2 = int(input("Input second num of matrix: "))
Matrix3 = int(input("Input third num of matrix: "))
Matrix4 = int(input("Input fourth num of matrix: "))
Matrix2 = Matrix2 * -1
Matrix3 = Matrix3 * -1
for i in range(0,size,2):
    Vm1 = alphabet.index(Ctext[i])
    Vm2 = alphabet.index(Ctext[i+1])
    Vm3 = (Vm1 * Matrix1) + (Vm2 * Matrix2)
    Vm4 = (Vm1 * Matrix3) + (Vm2 * Matrix4)
    Vm3Mod = Vm3 % 26
    Vm4Mod = Vm4 % 26
    Plaintext1 = alphabet[Vm3Mod]
    Plaintext2 = alphabet[Vm4Mod]
    plaintext = plaintext + Plaintext1 + Plaintext2
print(plaintext)