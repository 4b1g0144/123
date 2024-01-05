class BeverageExample:
    def __init__(self, name, flavor, size):
        # 初始化屬性
        self.name = name
        self.flavor = flavor
        self.size = size

    def describe(self):
        # 描述飲料
        return f"{self.size} {self.flavor} {self.name}"

    def serve(self):
        # 提供飲料
        return f"Serving {self.size} {self.flavor} {self.name}"

    def enjoy(self):
        # 品味飲料
        return f"Enjoying a {self.size} {self.flavor} {self.name}"

# 創建三個飲料物件
drink1 = BeverageExample("Coffee", "Latte", "Medium")
drink2 = BeverageExample("Tea", "Green", "Large")
drink3 = BeverageExample("Smoothie", "Berry", "Small")

# 分別呼叫物件的函式
result1 = drink1.describe()
result2 = drink1.serve()
result3 = drink1.enjoy()
result4 = drink2.describe()
result5 = drink2.serve()
result6 = drink2.enjoy()
result7 = drink3.describe()
result8 = drink3.serve()
result9 = drink3.enjoy()
# 印出結果
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
