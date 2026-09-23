class Transaction:
    def __init__(self, record):
        if not isinstance(record, dict):
            raise TypeError("record must be a dictionary")

        field_map = {
            "Region": "region",
            "Country": "country",
            "Item Type": "item_type",
            "Sales Channel": "sales_channel",
            "Order Priority": "order_priority",
            "Order Date": "order_date",
            "Order ID": "order_id",
            "Ship Date": "ship_date",
            "Units Sold": "units_sold",
            "Unit Price": "unit_price",
            "Unit Cost": "unit_cost",
            "Total Revenue": "total_revenue",
            "Total Cost": "total_cost",
            "Total Profit": "total_profit",
        }

        for column, attribute in field_map.items():
            setattr(self, attribute, record[column])

    def total(self):
        return self.total_revenue

    def clean(self):
        for field in [
            "region",
            "country",
            "item_type",
            "sales_channel",
            "order_priority",
        ]:
            value = getattr(self, field, None)
            if value is not None:
                setattr(self, field, str(value).strip())

        if self.units_sold < 0:
            self.units_sold = 0

        if self.unit_price < 0:
            self.unit_price = 0

        if self.unit_cost < 0:
            self.unit_cost = 0

        if self.total_revenue < 0:
            self.total_revenue = 0

        if self.total_cost < 0:
            self.total_cost = 0

        if self.total_profit < 0:
            self.total_profit = 0

        return self
