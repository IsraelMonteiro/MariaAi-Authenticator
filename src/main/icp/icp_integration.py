from token.src.icp.icrc1.index import Token
from token.src.icp.icrc1.token_type import Principal
from token.src.icp.icrc1.utils import safeParseJSON
from token.src.utils.safeParseJSON import safeParseJSON
from dfinity_agent import HttpAgent

# Initial configuration
def initialize_icp_integration(canister_id, token_standard):
    """
    Initialize the integration with ICP tokens using the Token module.

    :param canister_id: The Canister ID of the token.
    :param token_standard: The token standard (e.g., ICRC1, DIP20).
    :return: Token instance or None if initialization fails.
    """
    try:
        # Configure the agent
        agent = HttpAgent({"host": "https://ic0.app"})

        # Instantiate the token
        token = Token({
            "canisterId": canister_id,
            "agent": agent,
            "tokenStandard": token_standard
        })

        return token
    except Exception as e:
        print(f"Error initializing ICP integration: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Token configurations
    canister_id = "ryjl3-tyaaa-aaaaa-aaaba-cai"  # Replace with the correct Canister ID
    token_standard = "ICRC1"  # Supported standards: ICRC1, DIP20, EXT, etc.

    # Initialize the integration
    token_instance = initialize_icp_integration(canister_id, token_standard)

    if token_instance:
        try:
            # Retrieve basic information
            balance = token_instance.balanceOf("wallet-address")
            name = token_instance.name()
            symbol = token_instance.symbol()
            total_supply = token_instance.totalSupply()

            # Print results
            print(f"Token Name: {name}")
            print(f"Token Symbol: {symbol}")
            print(f"Total Supply: {total_supply}")
            print(f"Wallet Balance: {balance}")

        except Exception as ex:
            print(f"Error retrieving token data: {ex}")
