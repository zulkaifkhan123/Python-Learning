"""
Pattrens in Loop :


*
**
***
****
*****

"""

rows = 5
                
for i in range(1, rows + 1):       # Outer loop for rows
    for j in range(1, i + 1):       # Inner loop for columns
        print("*", end=" ")         # Print star in same line
    print()                         # Move to next line after each row


"""

*****
****
***
**
*

"""


               


















