# Demo Bedrock

- **Objective**: Generate a PDF using Bedrock

## How does this work?

1. Configure the data source to add to your knowledge base (preprocess)
2. Upload it to an Amazon S3 Bucket
3. Ingest the data by **generating Embeddings** (the weird numbers) with a FM (in this case it would be Cohere Embed Multilingual. Why? Because aquí hablamos español) and store them in a **supported vector store**.
4. Set up the application or **agent** to query the knowledge base and return **augmented responses**.

> All of this work because of Retrieval Augmented Generation (RAG)

## What the F is RAG ?

A technique for enhancing accuracy and reliability of gen AI models with facts feteched from external sources.

- To enable effective retrieval from private data, a common practice is to first split the documents into manageable chunks for efficient retrieval.
- The chunks are then converted to embeddings and written to a vector index, while maintaining a mapping to the original document.
- These embeddings are used to determine semantic similarity between queries and text from the data sources.
- The following image illustrates pre-processing of data for the vector database.

![Preprocessing](images/preprocess.png)

- At runtime, an embedding model is used to convert the user's query to a vector.
- The vector index is then queried to find chunks that are semantically similar to the user's query by comparing document vectors to the user query vector.
- In the final step, the user prompt is augmented with the additional context from the chunks that are retrieved from the vector index.
- The prompt alongside the additional context is then sent to the model to generate a response for the user.
- The following image illustrates how RAG operates at runtime to augment responses to user queries.

![Runtime](images/runtime.png)

## Models to be used

| Models    | Name                      |
| --------- | ------------------------- |
| Embedding | Cohere Embed Multilingual |
| Query     | Anthropic Claude v2.1     |

## Generative AI in government

- McGuire Research Services for Avanade, shows 82% of government employees are using AI on a daily or weekly basis.
- While 84% of organisations plan to increase their IT investments by up to 24% to take advantage of AI.
- It can bring vast pools of data together from Word documents and Excel spreadsheets, calendars and emails, chats and meeting notes, along with Power BI reports.
- It can then use this data to generate new content and deliver information and insights when most needed: as a brief summary, an answer to a question or the first draft of a detailed proposal or report.

> In a sector where huge amounts of time and energy are spent on mundane and repetitive tasks, the impact is dramatic. A copilot can help employees by prepopulating digital forms with data from word documents, then automating reminders and follow-up communications, summarising meetings and drafting paperwork

> According to Avanade’s research, improving efficiency is the number one objective for AI in government right now, according to 44% of respondents. It’s estimated that by automating mundane tasks, workers might gain up to 20 hours per week to focus on activities where their intervention counts.

Main use cases:

1. Content synthesis
2. Summarisation
