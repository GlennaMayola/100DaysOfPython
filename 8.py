#Program for Caesar Cipher
def caesar(text,shift,direction):
    final_text=''
    if direction=="decode":
            shift*=-1
    for letter in text:
        if letter in alphabet:
            num1=alphabet.index(letter)
            shift_num=(num1+shift)%26
            final_text+=alphabet[shift_num]
        else:
            final_text+=letter
    print(f"The {direction}d result is {final_text}")


should_continue=True

while should_continue:
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction=input("Type 'encode' to encrypt, type 'decode' decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    response=input("Do you want to continue?Type Yes or No:\n").lower()
    if response=="no":
         should_continue=False
         print("Goodbye")




