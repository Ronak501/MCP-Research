def get_users() -> list:
    """Return list of users"""
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]


def register_database_tools(mcp):

    @mcp.tool()
    def get_users_tool():
        return get_users()