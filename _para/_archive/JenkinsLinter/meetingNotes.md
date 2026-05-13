Ran into issues with Jenkins Listing server
- Yesterday modified a ton of jenkins emails in 1 pr
- Email sent wasn't able to be opened

Once email is sent, data not stored anywhere besides the email
Filter different categories
export to csv or pdf

Search for linting results from backend

Hayden: provide a link back to the Jenkins Build artifact instead
Aiden: Json not readable
Hayden: How about csv

Aiden: Bulk of issues are formatting errors
- Different errors like cron scheduling
Should we include all the warnings and errors that are not format

Hayden: An xlsx file with a different sheet of each type?
Aidan: Its very easy to make csv files but xlsx
- Vast majority of the warnings are formatting warnings
- 100 modified jenkins files, only a few were non formatting

Hayden: How easy would it be to auto fix the formatting
Aiden: Some are easy, like requiring a space before an open bracket
- More complicated ones like requiring indentation level
- Problem with that: Lot of scenarios where it makes sense to mess with indentations like a ton of parameters

Hayden: SO can some formatting errors be auto corrected?
Aidan: 3/4 main warnings we are checking for
1. spaces before opening bracket
2. MAx 1 indentation level change
3. after opening bracket, have to indent by 1
- Easiest thing to do is the spaces before open bracket

Hayden: Can we add that to the linter itself
Aidan: Hesitant, maybe we could add a step where its yes or no to auto commit
- Maybe a second jenkins job to 

Hayden: Send out email sounds good with a pause 
Aidan: Yeah we probably need a second job so we could do an autofixer vs 

Hayden: email includes build, but with jenkins build artifcat
Aidan: all errors in email?
Hayden: yes at least summary

Aidan: Have errors in table, have warnings in table, beside the format warnings, then includes

Jenkins file can create build aritfacts like evi_categrory_report_machinery_live

Might do an excel sheet with the different package

Email just has summary then link to the excel

Hayden: Could archive the files at one point

2 things to do
1. modify jenkins pipeline to do the stuff
2. new jenkins job that automatically do the formatting errors
