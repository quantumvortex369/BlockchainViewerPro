import requests
import time
from constants import MEMPOOL_API_URL

def fetch_transactions(filters):
    """
    Fetches transactions from the mempool.space API and filters them.
    """
    try:
        response = requests.get(MEMPOOL_API_URL)
        if response.status_code != 200:
            print(f"Error in API response: {response.status_code}")
            return []

        transactions = response.json()
        transactions_to_add = []

        for tx in transactions:
            value_btc = round(tx.get("value", 0) / 1e8, 8)
            fee_btc = round(tx.get("fee", 0) / 1e8, 8)

            # Apply filters
            if "Todas" not in filters:
                if "Ballenas" in filters and value_btc < 10:
                    continue
                if "Fee Bajo" in filters and fee_btc > 0.0005:
                    continue
                if "Mixers" in filters:
                    # Placeholder for mixers logic
                    continue
            
            tx_data = {
                "txid": tx.get("txid", ""),
                "value_btc": value_btc,
                "fee_btc": fee_btc,
                "timestamp": time.strftime("%H:%M:%S")
            }
            transactions_to_add.append(tx_data)

        return transactions_to_add

    except Exception as e:
        print(f"Error fetching real data: {e}")
        return []
