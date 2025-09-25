---
marp: true
theme: uncover
class: invert
paginate: true
footer: Graph data modelling for Agentic AI • Cloud Native Denmark 2025

---
<!-- _paginate: skip -->

# <!-- fit --> Graph data modelling for Agentic AI
<!-- _footer: Nina Jensen (she/her) • Senior Software Engineer @ [Cernel AI](https://cernel.ai) • Cloud Native Denmark 2025 -->

---

## What is Agentic AI?

> Agentic AI is a class of artificial intelligence that focuses on **autonomous systems** that can make decisions and perform tasks with or without human intervention.
[Wikipedia](https://en.wikipedia.org/wiki/Agentic_AI)

---

## What is Agentic AI?

> Agentic AI is an artificial intelligence system that can accomplish a specific goal with **limited supervision**. It consists of AI agents—machine learning models that mimic human decision-making to solve problems in real time.
[IBM](https://www.ibm.com/think/topics/agentic-ai)

---

## Agentic AI in practice

- stuff
- maybe a diagram

---

## Veracity & reliability

- LLM agents are stochastic processes
- Research from [OpenAI](https://arxiv.org/pdf/2509.04664) shows they will always be prone to "hallucinations"

##### How can we make them more reliable?

---

<style scoped>
img {
    width: 90%;
    height: 100%;
    object-fit: contain;
}
</style>

![](./assets/prompt_engineering.jpg)

---


## Context rot

- LLMs do not use their context uniformly
- Decreased performance as input length increases
- Smaller inputs lead to better results

<br><br>
###### https://research.trychroma.com/context-rot


---
## Context engineering


---

<!-- _paginate: hold -->

## <!-- fit --> ~~Context engineering~~ Data engineering

---

## Relational data

- Info on a single entity requires joining multiple tables
- Fine for small datasets
- Not so much if you have TBs of data
- Ask your local data analyst how easy it is to find the data you need

Consider UFO data, normalized and stuff

insert tables here

---

## Graph data



---

Demo: little mcp server to Neo4j?
