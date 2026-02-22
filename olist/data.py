import os
import pandas as pd

class Olist:
    def __init__(self):
        # Verilerin olduğu yolu dinamik olarak tanımlayalım
        self.data_path = os.path.join(os.path.expanduser('~'), ".workintech", "olist", "data", "csv")

    def get_data(self):
        """
        Bu metod ~/.workintech/olist/data/csv altındaki tüm csv'leri okur
        ve bir dictionary döndürür.
        Key: 'orders', 'sellers' vb.
        Value: Pandas DataFrame
        """
        # 1. Dosya isimlerini listeleyelim
        file_names = [f for f in os.listdir(self.data_path) if f.endswith('.csv')]

        # 2. Key isimlerini temizleyelim (ör: 'olist_customers_dataset.csv' -> 'customers')
        key_names = [f.replace('olist_', '').replace('_dataset', '').replace('.csv', '') for f in file_names]

        # 3. Sözlüğü oluşturalım
        data = {}
        for key, file in zip(key_names, file_names):
            data[key] = pd.read_csv(os.path.join(self.data_path, file))

        return data

    def ping(self):
        return "pong"
