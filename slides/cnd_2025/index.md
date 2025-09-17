---
marp: true
theme: uncover
class: invert
paginate: true
---

<!-- _paginate: skip -->
# Graph data modelling for Agentic AI
stuff

---

# Graph data???

---

# But why?



---

# Context Rot

- LLMs do not use their context uniformly
- Decreased performance as input length increases
- Smaller inputs lead to better results

<br><br>
###### https://research.trychroma.com/context-rot

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

# Relational data

- Info on a single entity requires joining multiple tables
- Fine for small datasets
- Not so much if you have TBs of data
- Ask your local data analyst how easy it is to find the data you need

Consider UFO data, normalized and stuff

insert tables here

---

Demo: little mcp server to Neo4j?
