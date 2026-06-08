
# Replace Data Value with Object 

If you have a large variety of primitive fields, try to group some of them into their own class. One better would be moving the behavior associated with this data into the class as well



Problem
- A class contains a data field. The field has its own behavior and associated data

order
- customer string

Solution. Make new class and move the old field and its behavior into the new class
order
- Customer customer

customer
- name
