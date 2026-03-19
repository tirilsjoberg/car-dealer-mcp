from mcp.server.fastmcp import FastMCP
from functions import (
    get_highest_horsepower_cars,
    get_most_fuel_efficient_cars,
    get_origin_statistics,
    get_best_power_to_weight_cars,
)

mcp = FastMCP("car-dealer")


@mcp.tool()
def highest_horsepower_cars(n: int = 5) -> list[dict]:
    """Return the n cars with the highest horsepower, highlighting performance strengths."""
    result = get_highest_horsepower_cars(n).copy()

    result["sales_highlight"] = result.apply(
        lambda row: f"{row['name']} stands out with {row['horsepower']} horsepower, making it a strong choice for customers who value performance.",
        axis=1
    )

    return result[["name", "horsepower", "mpg", "origin", "sales_highlight"]].to_dict(orient="records")

@mcp.tool()
def most_fuel_efficient_cars(n: int = 5) -> list[dict]:
    """Return the n most fuel-efficient cars, highlighting economy benefits."""
    result = get_most_fuel_efficient_cars(n).copy()

    result["sales_highlight"] = result.apply(
        lambda row: f"{row['name']} delivers {row['mpg']} mpg, making it an attractive option for customers who want lower fuel costs.",
        axis=1
    )

    return result[["name", "mpg", "horsepower", "origin", "sales_highlight"]].to_dict(orient="records")

@mcp.tool()
def best_power_to_weight_cars(n: int = 5) -> list[dict]:
    """Return the n cars with the best power-to-weight ratio, highlighting lightweight performance."""
    result = get_best_power_to_weight_cars(n).copy()
    result["sales_highlight"] = result.apply(
        lambda row: f"{row['name']} combines {row['horsepower']} horsepower with a weight of {row['weight']}, giving it a strong power-to-weight ratio for customers interested in a more responsive driving experience.",
        axis=1,
    )
    return result[["name", "horsepower", "weight", "mpg", "origin", "power_to_weight", "sales_highlight"]].to_dict(orient="records")

@mcp.tool()
def origin_statistics() -> list[dict]:
    """Return summary statistics grouped by car origin."""
    result = get_origin_statistics().reset_index()
    return result.to_dict(orient="records")


if __name__ == "__main__":
    mcp.run()