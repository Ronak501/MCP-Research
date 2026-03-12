def get_weather(city: str) -> str:
    """Get weather for a city"""
    return f"The weather in {city} is sunny."


def register_weather_tools(mcp):

    @mcp.tool()
    def get_weather_tool(city: str):
        return get_weather(city)