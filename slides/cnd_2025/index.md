---
marp: true
theme: uncover
class: invert
paginate: true
footer: Graph data modelling for Agentic AI • Cloud Native Denmark 2025
style: |
  section {
    font-family: 'Iosevka';
  }
  h1, h2 {
    color: #6CC417;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }
---
<!-- _paginate: skip -->

# <!-- fit --> Graph data modelling for Agentic AI
Cloud Native Denmark 2025
<!-- _footer: Nina Jensen (she/her) • Senior Software Engineer @ [Cernel AI](https://cernel.ai) • Illustrated by Ditte Jensen -->
<!--
Hello + name & workplace
Presentation illustrated by Ditte Jensen
Questions after the presentation please :)
-->
---

## What is Agentic AI?

> Agentic AI is a class of artificial intelligence that focuses on **autonomous systems** that can make decisions and perform tasks with or without human intervention.
[Wikipedia](https://en.wikipedia.org/wiki/Agentic_AI)

<!--
Determine AI knowledge + define agentic AI by slides
Note that agentic AI is loosely defined
Describes frameworks rather than a specific technology
-->

---

## What is Agentic AI?

> Agentic AI is an artificial intelligence system that can accomplish a specific goal with **limited supervision**. It consists of AI agents—machine learning models that mimic human decision-making to solve problems in real time.
[IBM](https://www.ibm.com/think/topics/agentic-ai)


<!--
Determine AI knowledge + define agentic AI by slides
Note that agentic AI is loosely defined
Describes frameworks rather than a specific technology
-->

---

## Veracity & reliability

* LLM agents are stochastic processes
* Research from [OpenAI](https://arxiv.org/pdf/2509.04664) shows they will always be prone to "hallucinations"

<div data-marpit-fragment>

##### How can we make them more reliable?

</div>

<!--

Key takeaways from article:
- LLMs guess when uncertain rather than admitting uncertainty
- Training & evaluation reward guessing rather than admitting uncertainty
- "Hallucinations" originate as errors in binary classification

-->

---


![bg](./assets/prompt.png)

<!--
We can do prompt engineering... but it's not really engineering and it doesn't really work super well

There's another problem too
-->

---


## Context rot

* LLMs do not use their context uniformly
* Decreased performance as input length increases
* Smaller inputs lead to better results

<br><br>
###### https://research.trychroma.com/context-rot

<!--
Key takeaways from article:
- LLMs should in principle handle the 10,000th token as reliably as the 1st
- But they don't :)
- Model performance varies significantly even on simple tasks as input length changes
-->

---
## Context engineering

SIKE

<!--
Why are we inventing new engineering disciplines when we already have a perfectly good one?
-->


---

![bg](./assets/data_engineering.jpg)

---
## Data engineering

<div data-marpit-fragment>

### Relational databases

</div>

* Info on a single entity usually requires multiple JOINs
* We denormalize data to make it easier to query analytically
* Ask your local data analyst how easy it is to find the data you need

<!--
Traditionally in data engineering, we work with relational databases, denormalize data and move it into datalakes
The point here:
There's an entire career field dedicated to analysing data and finding correct context
It's not easy!
-->
---


## Relational data

UFO sightings in the US

![bg](./assets/cat_ufo.jpg)

<!--
As an example, we could use ecommerce data... but frankly that's a bit boring

So we'll use UFO sightings instead!
--->

---

<style scoped>
table {
    font-size: 20px;
}
</style>

## Relational data
<br>
<div class="columns">
<div data-marpit-fragment>

| Sightings table  |
| :--------------- |
| sighting_id      |
| datetime         |
| location_id      |
| shape_id         |
| duration_seconds |
| comments         |

</div>

<div data-marpit-fragment>

| Locations table |
| :-------------- |
| location_id     |
| city            |
| state           |
| latitude        |
| longitude       |

</div>

<div data-marpit-fragment>

| Shapes table |
| :----------- |
| shape_id     |
| shape        |

</div>

<!--
This is an example of how our UFO sightings data could be stored in a relational database
It's somewhat normalized which is nice for several good reasons when working transactional systems
-->

---

## Graph databases

* Part of the NoSQL family
* Uses nodes and relationships to represent data
* Flexible schemas & index-free adjacency
* Implementations include [Neo4j](https://github.com/neo4j/neo4j), [dgraph](https://github.com/hypermodeinc/dgraph), [Apache AGE](https://github.com/apache/age)

<!--
Index-free adjacency means that each node references its neighbours
Accessing relationships and related data is a memory pointer lookup
This means that data retrieval is constant in the amount of data _accessed_ not the amount of data _stored_
Relationships are first-class entities
--->

---


## Graph data

<br><br>
<br><br>
<br><br>
<br><br>

![bg 85%](./assets/graph_2.png)

<!--
Example of how UFO data could be stored in a graph database
Note that we have split data into more entities than the three tables shown earlier
This is because we can get deduplication for free!
For example, observation dates can be shared between multiple sightings
which allows us to do effective queries like "give me all sightings in the last month"
--->


---

## Demo time!

* We'll be using [this dataset from Kaggle](https://www.kaggle.com/datasets/NUFORC/ufo-sightings)
* We've also hacked NASA's database...
* All code can be found [here](https://github.com/nina-j/cnd-2025)

<!--
For legal reasons, the NASA part is of course a joke. Not trying to cause an international incident. :D
--->

---

## Scully, you're not gonna believe this...

* LLMs are not magic
* Proper data engineering is still important
* Graph data modelling can help provide concise context

![bg](https://tenor.com/view/yeah-the-x-files-agent-scully-dana-scully-scully-gif-27518038.gif)

---

Thanks :alien:

![bg](./assets/truth.jpg)
