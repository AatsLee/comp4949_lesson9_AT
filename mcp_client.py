import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    async with streamablehttp_client("https://aaronmcp.onrender.com/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool("get_weather", {"city": "Vancouver"})
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
