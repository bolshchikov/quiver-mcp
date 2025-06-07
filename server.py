import os
import httpx
import json
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType


# Create an HTTP client for your API
# Bearer token authentication
api_client = httpx.AsyncClient(
    base_url="https://api.quiverquant.com",
    headers={"Authorization": f"Bearer {os.getenv('QUIVER_ACCESS_TOKEN')}"}
)

# Load your OpenAPI spec 
with open(os.path.join(os.path.dirname(__file__), "spec.json")) as f:
    openapi_spec = json.load(f)

# Create the MCP server
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=api_client,
    route_maps=[
        RouteMap(
            tags={"Tier 1"},
            mcp_type=MCPType.TOOL,
        ),
    ],
    name="Quiver API Server"
)

if __name__ == "__main__":
    mcp.run()