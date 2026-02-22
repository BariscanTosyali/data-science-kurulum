import pandas as pd
import numpy as np
from olist.data import Olist

class Order:
    def __init__(self):
        # Verileri data.py'daki Olist sınıfından çekiyoruz
        self.data = Olist().get_data()

    def get_wait_time(self):
        """Her sipariş için bekleme sürelerini hesaplar."""
        orders = self.data['orders'].copy()
        
        # Tarih dönüşümleri
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
        orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

        # Süre hesaplamaları (Gün bazında)
        orders['wait_time'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days
        orders['expected_wait_time'] = (orders['order_estimated_delivery_date'] - orders['order_purchase_timestamp']).dt.days
        
        # Gecikme: Gerçekleşen - Tahmin (Erken teslimatlar 0 kabul edilir)
        orders['delay_vs_expected'] = (orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']).dt.days
        orders['delay_vs_expected'] = orders['delay_vs_expected'].apply(lambda x: x if x > 0 else 0)

        return orders[['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected']]

    def get_review_score(self):
        """Her sipariş için inceleme puanlarını getirir."""
        reviews = self.data['order_reviews'].copy()
        return reviews[['order_id', 'review_score']]

    def get_training_data(self):
        """Bekleme süreleri ile puanları tek bir tabloda birleştirir."""
        wait_time = self.get_wait_time()
        review_score = self.get_review_score()
        
        # order_id üzerinden tabloları birbirine dikiyoruz
        training_set = wait_time.merge(review_score, on='order_id')
        
        # Eksik verileri (NaN) temizleyelim
        return training_set.dropna()
