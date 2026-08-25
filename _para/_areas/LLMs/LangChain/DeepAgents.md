# Deep Agents

Higher level of abstraction over langGraph and LangChain Create Agent

Goal
- Give builders a good out of the box experience
- Configurability

Building blocks for building harnesss, allowing users 

If you want to support skills, or memory, there is Middleware defined for that
- Summarization Middleware

### V 0.7
- Released week of 8/6/2026
- Frontier models are very good, don't need hand holding. Smaller models need the hand holding
- They have base prompts defined we can overwrite


Before a tool call you want to makes sure the inputs don't have any pii data exposed

Sub agent Isolated Tasks and have main agent over it
[Sub Agents](https://docs.langchain.com/oss/python/deepagents/subagents)
You can attach specific skills to sub agents 

Skills and subagents solve similar problems in different ways
Subagents are good 
1. context isolation

Skill contains domain knowledge

Skills have markdown file - when its


What happens when you load a skills?
[Skills spec](https://agentskills.io/specification) 
spec does 

frontmatter 
on agent start, only frontmatter is loaded into context window
So then when agent reads frontmatter and needs the skills, it will read the skills

SKILL.md loaded into agent on start
