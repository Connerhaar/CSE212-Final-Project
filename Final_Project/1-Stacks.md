# Stacks
## What is a Stack?
A stack is a data structure that allows you to `push` and item into the list and `pop` the last item that was pushed. Stacks can be used for many different things and are very useful when recalling previous errors.

### Last in, First Out
The easiest way to understand how stacks work is using the acronym LIFO which stand for Last in, First out. Basically the Last item that is in the stack will be the first item that is pulled out. So you are always pushing and popping out of the end of the list as shown below.

### Stack of Pennies
An example of this would be a stack of pennies. You can keep adding to a stack of pennies on the top side. Then when you remove a penny you take it off the top as you can see below. If you try to take a penney from the bottom the stack will most definetly break and fall over. So to get to teh penney on the very bottome you have to pop every penney before it

![](Images/Pennies.jpeg)


## The Performance
The [performance](performance.md) of a stack can vary depending on what part of the stack you are trying to get to. As you can see above the performance of `pushing` and `popping` from a stack is O(1). The problem occurs when we want to reach the bottom of the stack or the first item in the stack. This is a problem becuase you have to go through every other penny in the stack before getting to the last one. This would result in a performance of O(n).


## What are stacks used for?
stacks are mainly used for undoing things becuase of their great performance in removing the last action that was inputed. 

## Example: Undo Action
```python
list_of_numbers = [0,1,2,3,4,5,6,7,8,9]
undos = int(input("Enter the number of undos you want: "))
do = int(input("Enter the number of actions: "))

def undo_actions(values, undos):
    for number in range(undos):
        values.pop()
    print(values)
    return values

def do_action(values, do):
    for number in range(do):
        values.append("action")
    print(values)
    return values

undo_actions(list_of_numbers, undos)
do_action(list_of_numbers, do)
undo_actions(list_of_numbers, undos)

output:
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 'action', 'action', 'action']
[0, 1, 2, 3, 4, 5, 6, 7, 'action']
```
## Sample Problem

Write a program that will let someone write a sentence, then give them the option to undo, redo or add on another sentence. 

once you have finished the program you can try these different tests:
- type: "My name is conner", then hit enter
- type: "u" (this should undo the last word in the sentence), then hit enter
- type: "Conner and i like to play basketball" , then hit enter
- type: "u", then hit enter
- type: "u", then hit enter
- type: "u", then hit enter
- type: "u", then hit enter
- type: "u", then hit enter
- type: "I like to play basketball."

here is an example of the output should look like:
```
To continue writing hit enter twice, to undo hit enter and then type (u)
Please start writing: My name is conner
u
My name is

My name is Conner and i like to play basketball
u
My name is Conner and i like to play
u
My name is Conner and i like to
u
My name is Conner and i like
u
My name is Conner and i
u
My name is Conner and

My name is Conner and I like to play basketball.
```
If you have tried the problem and can not figure it out here is a [possible solution](Python_Files/Sample_answer1.py). 





