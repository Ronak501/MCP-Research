from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Demo MCP Server")

# Import tools
from tools.calculator import register_calculator_tools
from tools.weather import register_weather_tools
from tools.database import register_database_tools
from tools.search import register_search_tools

# Register tools
register_calculator_tools(mcp)
register_weather_tools(mcp)
register_database_tools(mcp)
register_search_tools(mcp)

if __name__ == "__main__":
    mcp.run()