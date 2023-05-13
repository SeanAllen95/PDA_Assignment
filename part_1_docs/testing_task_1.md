### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
#This CardGame class needs a def__init__(self):
# This function uses an assignment (=) operator instead of a comparison operator (==)
#This function is missing a colon after else (else:)

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2

#This function starts with dif but it should start with def
#card1 and card2 should be separated with a comma
#if, else and the returns need to be indented
#return card should be return card1
  


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total


#The total variable needs to be assigned to 0 to start of the summing up
#The return statement is in the for loop, it needs to be indented back one so it lines up with the "for"
#The return statement won't be able to concatenate the string and the total, the total needs to be converted into a string with the str() function
#A space needs to be added to the end of the string in the return
```
