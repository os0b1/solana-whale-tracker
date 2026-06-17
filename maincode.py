import asyncio
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
import sys

async def main():
    if len(sys.argv) > 1:
        wallet = sys.argv[1]
    else:
        wallet = input("Enter Solana wallet: ").strip()
    
    if not wallet:
        print("No address provided.")
        return
    
    client = AsyncClient("https://api.mainnet-beta.solana.com")
    
    try:
        pubkey = Pubkey.from_string(wallet)
        print(f"\nFetching transactions for {wallet[:8]}...")
        
        response = await client.get_signatures_for_address(pubkey, limit=10)
        transactions = response.value
        
        if not transactions:
            print("No transactions found.")
            return
        
        print(f"\nFound {len(transactions)} transactions:\n")
        
        for i, tx in enumerate(transactions, 1):
            sig = str(tx.signature)
            print(f"{i}. {sig[:12]}...{sig[-12:]}")
            print(f"   Slot: {tx.slot}")
            print()
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())