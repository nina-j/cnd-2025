from functools import partial
from typing import Any

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

from models import RelatedSightings
from settings import Settings


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
