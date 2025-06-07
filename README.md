# Quiver MCP Server
> MCP server for Quiver API

# Running locally

## Claude Desktop

```json
{
  "mcpServers": {
    "quiver-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--with", "httpx",
        "--with", "fastmcp",
        "python",
        "<full-path>/quiver-mcp/server.py"
      ],
      "env": {
        "QUIVER_ACCESS_TOKEN": "<your-quiver-access-token>"
      }
    }
  }
}