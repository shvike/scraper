from autoscraper import AutoScraper
from pprint import pprint

rabota_url = "https://rabota.by/search/vacancy?text=&area=1002&area=2237&salary=&currency_code=BYR&experience=doesNotMatter&" \
      "order_by=relevance&search_period=30&items_on_page=20&no_magic=true&grouping=AREA&datasetName=&utm_source=" \
      "google&utm_medium=cpc&utm_campaign=S%20%7C%20%D0%A1%D0%BE%D0%B8%D1%81%D0%BA%D0%B0%D1%82%D0%B5%D0%BB%D0%B8%20%7C%" \
      "20%D0%9C%D0%B8%D0%BD%D1%81%D0%BA&utm_content=applicant_BY_minsk&utm_term=%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%" \
      "D0%B2%20%D0%BC%D0%B8%D0%BD%D1%81%D0%BA%D0%B5&gclid=EAIaIQobChMI99rUj7_O8wIVg-F3Ch1hNArvEAAYASAAEgJjDvD_BwE"

wanted_list = ["Комплектовщик подработка", "от 1 300 бел. руб."]


scraper = AutoScraper()

result = scraper.build(rabota_url, wanted_list)

res = scraper.get_result_similar(rabota_url, grouped=True)

# pprint(res)

keys = res.keys()
key0, key1 = list(keys)[0], list(keys)[1]
# print(f"\nKey '{key0}' shows the Position\nKey '{key1}' shows the Salary")

scraper.set_rule_aliases({key0: "Position", key1: "Salary"})

scraper.keep_rules([key0, key1])

scraper.save("rabota-scraper")
# res2 = scraper.get_result_similar(rabota_url, group_by_alias=True)
# print()
# pprint(res2)
# res3 = scraper.get_result_similar("https://rabota.by/search/vacancy?text=&area=1002&area=2237&salary=&currency_code="
#                                   "BYR&experience=doesNotMatter&order_by=relevance&search_period=30&items_on_page=20&"
#                                   "no_magic=true&grouping=AREA&datasetName=&utm_source=google&utm_medium=cpc&"
#                                   "utm_campaign=S+%7C+%D0%A1%D0%BE%D0%B8%D1%81%D0%BA%D0%B0%D1%82%D0%B5%D0%BB%D0%B8+%7C+"
#                                   "%D0%9C%D0%B8%D0%BD%D1%81%D0%BA&utm_content=applicant_BY_minsk&utm_term=%D1%80%D0%B0%"
#                                   "D0%B1%D0%BE%D1%82%D0%B0+%D0%B2+%D0%BC%D0%B8%D0%BD%D1%81%D0%BA%D0%B5&gclid="
#                                   "EAIaIQobChMI99rUj7_O8wIVg-F3Ch1hNArvEAAYASAAEgJjDvD_BwE&page=1", group_by_alias=True)
# pprint(res3)
# scraper.load("rabota-scraper")

def scrap3():
      rabota_url = "https://rabota.by/search/vacancy?text=&area=1002&area=2237&salary=&currency_code=BYR&experience=does" \
                   "NotMatter&order_by=relevance&search_period=30&items_on_page=20&no_magic=true&grouping=AREA&datasetName=" \
                   "&utm_source=google&utm_medium=cpc&utm_campaign=S+%7C+%D0%A1%D0%BE%D0%B8%D1%81%D0%BA%D0%B0%D1%82%D0%B5" \
                   "%D0%BB%D0%B8+%7C+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA&utm_content=applicant_BY_minsk&utm_term=%D1%80%D0%B0" \
                   "%D0%B1%D0%BE%D1%82%D0%B0+%D0%B2+%D0%BC%D0%B8%D0%BD%D1%81%D0%BA%D0%B5&gclid=EAIaIQobChMI99rUj7_O8wIVg-" \
                   "F3Ch1hNArvEAAYASAAEgJjDvD_BwE"

      wanted_list = ["Комплектовщик подработка", "от 1 300 бел. руб."]

      scraper = AutoScraper()
      er = scraper.build(rabota_url, wanted_list)
      print(er)
      res = scraper.get_result_similar(rabota_url, grouped=True)
      print(res)
      keys = res.keys()
      key0 = list(keys)[0]
      key1 = list(keys)[1]
      scraper.set_rule_aliases({key0: "Position", key1: "Salary"})
      scraper.keep_rules([key0, key1])
      scraper.save("rabota-scraper")
      result = scraper.get_result_similar(rabota_url, group_by_alias=True)
      return result