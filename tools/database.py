def register_database_tools(mcp):

    @mcp.tool()
    def get_users():
        """Return list of users"""
        return [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]