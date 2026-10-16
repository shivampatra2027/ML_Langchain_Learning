```Main Probelms due to LLM:```
    a) Private data
    b) recent developments
    c) Halucinations
pre-traning vs fine tuning

1) supervised tuning  2)cntinued pretrained

2) colect data 2) choose a method , 3) Train for new ephocs and 4) Evaluate & safety-test

3) Fine tuning solves:
    a) Private data prob
    b)recent/latest data probb
    c)Halucination Prob

4) Some major problems with fine tuning
    a) Compututionally expensive
    b) Technical expertise
    c) Repetative task / Increase cost to company.

5) Solution?? In-Context Learning
    It is a core capablity of large language Model like claude llama, where mode learns to solve a task purely by seeing examples in prompt --without updating its weight.
        e.g-> Give examples ..the LLM will learn from example and reply.
        This is also known as Few Shot Prompting.
    
    2) Emegent property is a behavious or ability that suddenly appears in a system when it reaches a certiain scale or complexity --even through it was not explictly programmed or expected from te individual components.

    paper-> Language Paper are few shot learners.

``                       what is RAG now??              ``
3) Rag is a waay to make a language model smrter by giving it extra information at the time you ask your question.


4) Rag=Information retrival + text generation
    a) indexing -> process of building the external knowledge base.
    b) Retrival -> Understand query and finding from external KB for ans.
    c) Agumentation -> Query + prompt
    d) Generation -> prompt -> LLM -> Response Generation

5) In broader way.
    a) Indexing:
        Indexing is process of preparing kB so that it can be efficiently searched at query time. This step consist of 4 sub-steps.

        1) Document Injection- You load ur source knowledge into memory.(Document Loader)
        2) Text Chunking- Break the large document into small sematically meaningfull chunks.
            small chunks=--> Better semantic meaningful chunks.
        use: Text Splitters.
        3) Embedding Generations- Convert each chunk into dense vectors that captures it's meaning.
        4)Store in a Vector Store -> Store these vectors along with the org text into vector store. e.g Chroma etc.
        5) Use this vector store as external Knowledge state.
    b) Retrieval -Retrieval is a real time process of finding out relevant pieces of chunks from a pre-built index.
        1) query -> embedding vectors
        2) semantic search
        3) step 3 -> ranking
        4) fetch the chunks.
    c)Augumentation ->  Create a prompt where we not only provide our query but also will inject our context.
    d) Generation -> query se LLM -> LLm generated response based on parametric and its own KB.
