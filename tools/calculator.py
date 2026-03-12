def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


def register_calculator_tools(mcp):

    @mcp.tool()
    def add_numbers_tool(a: int, b: int):
        """Add two numbers."""
        return add_numbers(a, b)