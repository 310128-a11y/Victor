#轉換西元出生年為生肖
def birth_year_to_animal(year:int)-> str:
    animals = ["猴", "雞", "狗", "豬", "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊"]
    return animals[year % 12]
#測試程式
if __name__ == "__main__":
    test_years = [1996, 2000, 2003, 2012, 2021]
    for year in test_years:
        animal = birth_year_to_animal(year)
        print(f"{year} 年的生肖是：{animal}")