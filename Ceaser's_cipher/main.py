alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
#text_len=len(text)


def ceasar(text, shift, direction):
  if direction=="decode":
    shift*=-1
  new_alphabet= alphabet[shift:]+alphabet[:shift]
  shifted_alphabet= ''.join(str(e) for e in new_alphabet)
  indexes= list(range(len(text)))
  
  final_encryption=''
  for l in text:
    if l in alphabet:
      given_index=int(alphabet.index(l)) 
      encrypted_word= shifted_alphabet[given_index]
      final_encryption+=encrypted_word
    else:
      final_encryption+=l
  print(final_encryption)

'''
def decrypt(text, shift):
  new_alphabet= alphabet[-shift:]+alphabet[:-shift]
  shifted_alphabet= ''.join(str(e) for e in new_alphabet)
  indexes= list(range(len(text)))
  l=0
  final_decryption=''
  for l in text:
    given_index=int(alphabet.index(l))
    encrypted_word= shifted_alphabet[given_index]
    final_decryption+=encrypted_word
  print(final_decryption)
'''
from art import logo
print(logo)


should_end= False
while not should_end:
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 text = input("Type your message:\n").lower()
 shift_number = int(input("Type the shift number:\n"))
 shift=int(shift_number%26)
 ceasar(text, shift, direction)
 restart=input("Type yes to continue or no to end")
 if restart=="no":
   should_end=True
   print("Goodbye")