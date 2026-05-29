trade sites time dependent
on dev they check like see what should we pull to staging

What if you want only A and C on a git flow
If you have A, B and C on dev

Either have to revert or cherry pick B

Without release branch, at any point in time you can't roll back 


Hybrid strategy
Trade pub sites
- check into staging and it auto merges

main is source of truth
dev - throwaway branch
- 
feature/A

When they are ready for merge, NORMAL merge into dev, not squash
- can continue to do merge 

Create release branch off of main
at that point do squash merge into release

release branch auto deployed to staging or simething
At this point, 

If need bugfix
- create bugfix branch off of release
- Then re merge down to the dev branch

Trade sites
- dev rollout to machinery trader, and they only test machinery trader
- so stuff cant be caught til its up to staging


Gotcha
- dev is throwaway
- stg is where the real integration validation happens
- Longstanding feature branch, just need to git merge 
- traceability gap


wrap things into a feature flag
Use an es thing to toggle it on or off

is dev auto built to dev environments
dev branch -> pipeline listens -> every time it checks in and stuff it runs to dev
release branch -> staging ->
main -> master

squash to release but not to dev

in git projects everything is moved over
in tfvc projects, trunk branch is brought to main branch in github

webhook
- when u commit change to github
- fires off something to azure devops server
- Triggers stuff like unitTests

Pipelines in devops rather than github actions
Not that you can't, just have to make sure its the
azure doesnt do docker
github does so we might want to convert to github

Azure pipeline is so friggin fast so it doesn't really matter

first person to check in goes to pipeline
then rest go to q
so we dont have a ton of stuff rolling to pipeline

framework projects in a special 'sync' state, where changes in tfvc AND git have to be synced
All references in the project.cs is to the TFVC path
loren has to fix it via a script
- Script is like am I a git project or tfvc
- 

still gotta do stuff that can't be automated... like updating paths
2 weeks should start moving some projects over
framework projegc

a ton of repos 
Process can create a repo name,
so we can update the name


Some other caveats
- way we operate with tfvc, we dont need to get like framework models
- WE will have to manually clone everything
- framework models is strongest case for submodules

nuget npm style of stuff

snow wiki articles
