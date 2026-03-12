def register_search_tools(mcp):

    @mcp.tool()
    def search_web(query: str):
        return f"Searching for {query}"