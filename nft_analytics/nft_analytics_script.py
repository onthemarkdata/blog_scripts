import networkx as nx
import pandas as pd

# import data
metadata = "metadata_0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D_04302022.csv"
sales = "sales_0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D_04302022.csv"
transfers = "transfers_0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D_04302022.csv"

bayc_metadata = pd.read_csv(f"bayc_nft_data/{metadata}")
bayc_sales = pd.read_csv(f"bayc_nft_data/{sales}")
bayc_transfers = pd.read_csv(f"bayc_nft_data/{transfers}")

bayc_metadata.info()
bayc_sales.info()
bayc_transfers.info()

