from mcp.server.fastmcp import FastMCP
from services.excel_services import projetos_pendentes

mcp = FastMCP("ClickupSync")

@mcp.tool()
def listar_projetos():
    return projetos_pendentes().to_dict(orient="records")

if __name__ == "__main__":
    mcp.run()