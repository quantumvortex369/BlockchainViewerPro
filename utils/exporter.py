import csv
import datetime

def export_to_csv(table, filters):
    """
    Exports the transaction data from the table to a CSV file.
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"transacciones_filtradas_{timestamp}.csv"
        
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Hash", "Valor (BTC)", "Fee (BTC)", "Hora"])

            for row in range(table.rowCount()):
                txid = table.item(row, 0).text()
                value_btc = float(table.item(row, 1).text())
                fee_btc = float(table.item(row, 2).text())
                timestamp = table.item(row, 3).text()

                if "Todas" not in filters:
                    if "Ballenas" in filters and value_btc < 10:
                        continue
                    if "Fee Bajo" in filters and fee_btc > 0.0005:
                        continue
                    if "Mixers" in filters:
                        continue

                writer.writerow([txid, value_btc, fee_btc, timestamp])
        
        return filename, None

    except Exception as e:
        return None, e
