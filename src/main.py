import asyncio

from pydantic_ai import Agent
from rich import print as pprint
from structlog.stdlib import get_logger

from agent import sightings_agent
from settings import setup_logging

setup_logging()

logger = get_logger()


async def run_agent(agent: Agent, prompt: str) -> None:
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
