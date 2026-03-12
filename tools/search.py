def search_web(query: str) -> str:
    """Search the web for a query."""
    return f"Searching for {query}"


def register_search_tools(mcp):

    @mcp.tool()
    def search_web_tool(query: str):
        return search_web(query)