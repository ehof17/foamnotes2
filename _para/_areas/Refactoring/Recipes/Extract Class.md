
# Extract Class
> Helps if part of behavior of the large class can be spun off into a separate component

## Problem:
- When one class does the work of two, awkwarness reslts

person
- name
- officeAreaCode
- officeNumber
- getTelephoneNumber

Solution:
Create a new class


person       Telephone Number
- name -----> - office area code
              - officeNumber
              - getTelephoneNumber
              