[[_resources/RAG/table_rag]]

A group of people tried to fix the issue of table format not working with rag. They devised a plan to improve it via table rag.

![Table rag](../../../assets/images/table%20rag%20.png)

> Current rag solution for tables:
> Convert the table to text, chunk the text
> Flattened Tables are segmented and merged with adjacent text spans

This has bad things like
- info loss, since tabular structure integrity is compromised
- lack of a global view
  - Aggs, comps and other reasoning tasks are hard, for things that require an understanding of the whole table


