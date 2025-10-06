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
- If I wanted unreliable things in prod I'd use Javascript :)

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

## Relational data
<style scoped>
table {
    font-size: 20px;
}
</style>
<div data-marpit-fragment>

| sighting_id | datetime        | location_id | shape_id | duration_seconds | comments |
| ----------: | :-------------- | ----------: | -------: | ---------------: | :------- |
|          59 | 11/1/2004 19:00 |         161 |       17 |              420 | ...      |
|         185 | 11/1/2004 19:00 |         143 |        9 |               60 | ...      |

</div>

<div data-marpit-fragment>

| location_id | city         | state |   latitude |    longitude |
| ----------: | :----------- | :---- | ---------: | -----------: |
|         143 | agoura hills | ca    | 34.1363889 | -118.7736111 |
|         161 | abingdon     | va    | 36.7097222 |  -81.9775000 |

</div>

<div data-marpit-fragment>


| shape_id | shape   |
| -------: | :------ |
|        9 | light   |
|       17 | unknown |

</div>


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

<br>
<div data-marpit-fragment>

![w:700](./assets/kaggle.png)

</div>

---

## Demo time!

* We have also hacked NASA's database...

<br>
<div data-marpit-fragment>

![w:1150](./assets/nasa.png)

</div>

---

## BASED & RUST PILLED

![bg](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGthdnZ2bGVsMnlocGRxb2Rqd2s1dDVhODB6aXZoZGRzbWh2MmZ6cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ehwuBgKNA2NACoFa7w/giphy.gif)

---

## Python packages

* [pydantic-ai](https://ai.pydantic.dev/) - AI Agent framework
* [pydantic](https://docs.pydantic.dev/) - Data validation
* [logfire](https://logfire.pydantic.dev/docs/) - Logging
* [polars](https://www.polars.org/https://pola.rs/) - Data processing
* [neo4j-rust-ext](https://github.com/neo4j/neo4j-python-driver-rust-ext) - Neo4j Python driver

---
<!--  _footer: "" -->
## Compose file

```yml

services:
  neo4j:
    container_name: cnd-neo4j
    hostname: neo4j
    image: neo4j:latest
    environment:
      - NEO4J_AUTH=neo4j/cloudnative4j
      - NEO4J_PLUGINS=["apoc"]
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - neo4j_data:/data

  neo4j-mcp:
    container_name: cnd-neo4j-mcp
    hostname: neo4j-mcp
    image: mcp/neo4j-cypher:latest
    ports:
      - "8000:8000"
    environment:
      - NEO4J_URI=bolt://neo4j:7687
      - NEO4J_USERNAME=neo4j
      - NEO4J_PASSWORD=cloudnative4j
      - NEO4J_READ_ONLY=true # don't want the agents to write to the database
      - NEO4J_TRANSPORT=http
      - NEO4J_MCP_SERVER_PORT=8000
      - NEO4J_MCP_SERVER_PATH=/api/mcp/
    depends_on:
      - neo4j

volumes:
  neo4j_data:

```

---
<!-- _footer: ""-->

![bg left](./assets/rogue_ai.webp)

## Write access in prod is a great idea!!11!!1

---
<!--  _footer: "" -->
## Loading data

```python
def load_locations(tx: ManagedTransaction) -> None:
    locations = TypeAdapter(list[LocationCsv]).validate_python(
        read_files("locations").to_dicts()
    )
    tx.run(
        """//cypher
        UNWIND $locations AS location
        MERGE (l:Location {location_id: location.location_id})
        SET l += location
        """,
        locations=[location.model_dump() for location in locations],
    )


def load_shapes(tx: ManagedTransaction) -> None:
    shapes = TypeAdapter(list[ShapeCsv]).validate_python(
        read_files("shapes").to_dicts()
    )
    tx.run(
        """//cypher
        UNWIND $shapes AS shape
        MERGE (s:Shape {shape_id: shape.shape_id})
        SET s += shape
        """,
        shapes=[shape.model_dump() for shape in shapes],
    )

```

---
<!--  _footer: "" -->

## Loading data

```python
def load_sightings(tx: ManagedTransaction) -> None:
    sightings = TypeAdapter(list[SightingCsv]).validate_python(
        read_files("sightings").to_dicts()
    )
    tx.run(
        """//cypher
        UNWIND $sightings AS sighting
        MERGE (s:Sighting {sighting_id: sighting.sighting_id})
        SET s.comments = sighting.comments

        MERGE (dt: ObservationTime {value: sighting.datetime})
        MERGE (dur: Duration {value: sighting.duration_seconds})

        WITH *

        MATCH (l:Location {location_id: sighting.location_id})
        MATCH (sh:Shape {shape_id: sighting.shape_id})
        MERGE (s)-[:ON_LOCATION]->(l)
        MERGE (s)-[:FOR_DURATION]->(dur)
        MERGE (s)-[:OBSERVED_AT]->(dt)
        MERGE (s)-[:HAS_SHAPE]->(sh)
        """,
        sightings=[sighting.model_dump() for sighting in sightings],
    )
```
---
<!--  _footer: "" -->

## Loading data

```python
def load_nasa_sightings(tx: ManagedTransaction) -> None:
    nasa_sightings = TypeAdapter(list[NasaSightingCsv]).validate_python(
        read_files("nasa_sightings").to_dicts()
    )
    tx.run(
        """//cypher
        UNWIND $nasa_sightings AS nasa_sighting
        MERGE (ns:NasaSighting {case_id: nasa_sighting.case_id})
        SET ns.credibility_score = nasa_sighting.credibility_score
        SET ns.altitude_est_meters = nasa_sighting.altitude_est_meters
        SET ns.notes = nasa_sighting.notes

        MERGE (dt: ObservationTime {value: nasa_sighting.datetime})
        MERGE (cl: Classification {value: nasa_sighting.classification})
        MERGE (tl: ThreatLevel {value: nasa_sighting.threat_level})
        MERGE (invs: InvestigationStatus {value: nasa_sighting.investigation_status})

        WITH *

        MATCH (l:Location {location_id: nasa_sighting.location_id})
        MATCH (s:Shape {shape_id: nasa_sighting.shape_id})
        MERGE (ns)-[:ON_LOCATION]->(l)
        MERGE (ns)-[:OBSERVED_AT]->(dt)
        MERGE (ns)-[:HAS_SHAPE]->(s)
        MERGE (ns)-[:HAS_CLASSIFICATION]->(cl)
        MERGE (ns)-[:HAS_THREAT_LEVEL]->(tl)
        MERGE (ns)-[:HAS_INVESTIGATION_STATUS]->(invs)
        """,
        nasa_sightings=[nasa_sighting.model_dump() for nasa_sighting in nasa_sightings],
    )

```

---
<!--  _footer: "" -->
## <!-- fit---> Results in graph database
![bg left:70%](./assets/full_graph.png)

---
<!--  _footer: "" -->
## Defining agents

```python
class Sighting(Base):
    sighting_id: int
    comments: str


class NasaSighting(Base):
    case_id: str
    credibility_score: float
    altitude_est_meters: int
    notes: str


class RelatedSightings(Base):
    private_sighting: Sighting
    nasa_sighting: NasaSighting
    datetime: AwareDatetime
    shape: str

```

---
<!--  _footer: "" -->
## Defining agents

```python
def get_agent(output_type: Any) -> Agent:
    """Obtain an agent with the given output type

    Args:
        output_type: The type of the output to be returned by the agent

    Returns:
        An agent with the given output type
    """
    settings = Settings()
    server = MCPServerStreamableHTTP(settings.mcp_url)
    return Agent(
        model=AnthropicModel(
            model_name="claude-sonnet-4-5",
            provider=AnthropicProvider(
                api_key=settings.anthropic_api_key.get_secret_value()
            ),
        ),
        toolsets=[server],
        output_type=output_type,
    )


sightings_agent = partial(get_agent, output_type=list[RelatedSightings])

```

---
<!--  _footer: "" -->
## Running agents

```python
async def run_agent(agent: Agent, prompt: str) -> None:
    """Run an agent with the given prompt

    Args:
        agent: The agent to run
        prompt: The prompt to run the agent with
    """
    await logger.ainfo("Agent starting", prompt=prompt)
    result = await agent.run(prompt)
    await logger.ainfo("Agent done")
    pprint(result.output)


async def main() -> None:
    await run_agent(
        sightings_agent(),
        "Find 5 sightings that are related to a NASA sighting",
    )


if __name__ == "__main__":
    asyncio.run(main())

```

---

## Let's see it in action...

---

## Scully, you're not gonna believe this...

* LLMs are not magic
* Proper data engineering is still important
* Graph data modelling can help provide concise context

![bg contain](https://tenor.com/view/yeah-the-x-files-agent-scully-dana-scully-scully-gif-27518038.gif)

---
<div data-marpit-fragment>

Thanks :alien:

</div>
<br>
<br>

![bg](./assets/truth.jpg)

<div data-marpit-fragment>

![h:300](./assets/linkedin.jpg)

</div>
