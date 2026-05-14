Found es email called email@monroetractor.com.
Renaming to email3 worked
{
    "oldEmail": "email@monroetractor.com",
    "newEmail": "email3@monroetractor.com"
}

Trying to rename email3 back to email failed
{
    "oldEmail": "email3@monroetractor.com",
    "newEmail": "email@monroetractor.com"
}

{
    "RecSysStatus": "active",
    "Message": "The old redis email key has been renamed to the new email key. However, the Elastic update failed. The old email user could not be renamed to the new email user in Elastic. Failed to update elastic user document with ID 134 to have email email@monroetractor.com. Failed to update elastic user document with ID 2132 to have email email@monroetractor.com. Failed to update elastic user document with ID 2200 to have email email@monroetractor.com. Failed to update elastic user document with ID 2754 to have email email@monroetractor.com. ",
    "Success": false
}

Running it again 
{
    "RecSysStatus": "active",
    "RecSysLastClickUTCDateTime": "2026-05-05T21:35:11",
    "RecSysBidPropensity": "Unlikely",
    "Message": "The new email key already exists. No changes were made. However, the Elastic update failed. The old email user could not be renamed to the new email user in Elastic. Failed to update elastic user document with ID 134 to have email email@monroetractor.com. Failed to update elastic user document with ID 2132 to have email email@monroetractor.com. Failed to update elastic user document with ID 2200 to have email email@monroetractor.com. Failed to update elastic user document with ID 2754 to have email email@monroetractor.com. ",
    "Success": false
}


The new email key already exists,
no changes were made
- in es tho it was updated from email3@monroetractor.com
- to email@monroetractor.com


Then re running it from email to email3
{
    "RecSysStatus": "active",
    "Message": "The old redis email key has been renamed to the new email key. However, the Elastic update failed. The old email user could not be renamed to the new email user in Elastic. Failed to update elastic user document with ID 134 to have email email3@monroetractor.com. Failed to update elastic user document with ID 2132 to have email email3@monroetractor.com. Failed to update elastic user document with ID 2200 to have email email3@monroetractor.com. Failed to update elastic user document with ID 2754 to have email email3@monroetractor.com. ",
    "Success": false
}


ran
{
    "oldEmail": "email@monroetractor.com",
    "newEmail": "email3@monroetractor.com"
}

{
    "RecSysStatus": "active",
    "RecSysLastClickUTCDateTime": "2026-05-05T21:35:11",
    "RecSysBidPropensity": "Unlikely",
    "Message": "The new email key already exists. No changes were made in Redis.",
    "Success": true
}

Then i was able to rename to other one
{
    "oldEmail": "email3@monroetractor.com",
    "newEmail": "email@monroetractor.com"
}
{
    "RecSysStatus": "active",
    "Message": "The old redis email key has been renamed to the new email key.",
    "Success": true
}

{
    "oldEmail": "email@monroetractor.com",
    "newEmail": "email3@monroetractor.com"
}

{
    "RecSysStatus": "active",
    "Message": "The old redis email key has been renamed to the new email key.",
    "Success": true
}
