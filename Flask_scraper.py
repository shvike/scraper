from autoscraper import AutoScraper
from flask import Flask, request, jsonify
from pprint import pprint


app = Flask(__name__)     # Attention: after first run you should block str.72 and unblock str.73-74


def create_scraper_rules():
    url = "https://rabota.by/vacancies/podrabotka?area=2237&clusters=true&page=0"
    wanted_list = ["Кассир в пиццерию (г. Солигорск)", "до 850 бел. руб.", "ООО Сиванабел", "Борисов"]
    scraper = AutoScraper()
    scraper.build(url, wanted_list)
    res = scraper.get_result_similar(url, grouped=True)
    # pprint(res)

    keys = res.keys()
    print(keys)
    print(len(keys))
    key0, key1, key2, key3 = list(keys)[0], list(keys)[1], list(keys)[2], list(keys)[3]
    print(f"\nKey '{key0}' shows the Position\nKey '{key1}' shows the Salary\n"
          f"Key '{key2}' shows the Company\nKey '{key3}' shows the Location\n(All extra rules are redundant)")

    scraper.set_rule_aliases({key0: "Position", key1: "Salary", key2: "Company", key3: "Location"})
    scraper.keep_rules([key0, key1, key2, key3])
    scraper.save("rabota-scraper")
    return "Created scraper's rules in the file 'Rabota-scraper'"


def scrap(new_url):
    rabota_scraper = AutoScraper()
    rabota_scraper.load("rabota-scraper")
    result = rabota_scraper.get_result_similar(new_url, group_by_alias=True)
    # pprint(result)
    print(f'Count of "Company" is: {len(result["Company"])}')
    print(f'Count of "Salary" is: {len(result["Salary"])}\n')


    # pprint((result["Position"][1]))

    # worker_scraper = AutoScraper()
    # worker_scraper.build(new_url, list(result["Position"][1]))
    # worker = rabota_scraper.get_result_exact(new_url, group_by_alias=True)
    # print(worker)

    # scraper = AutoScraper()
    # for i in result["Position"]:
    #     print(i)
        # scraper.build(new_url, list(i))
        # worker = rabota_scraper.get_result_exact(new_url, group_by_alias=True)
        # print(worker)
    #     # final_result.append(worker)
    #     pprint(worker)
    # pprint(final_result)
    # wanted_list = [result["Position"][0]]
    # scraper.build(new_url, wanted_list)
    # worker = rabota_scraper.get_result_exact(new_url, group_by_alias=True)
    # pprint(worker)

    final_result = []
    for i in range(len(list(result.values())[0])):
        try:
            final_result.append({x: result[x][i] if result[x][i] else "12345" for x in result})
        except:
            pass
            # final_result.append({"Record with empty 'Salary' field"})
    pprint(final_result)
    print(f'\nCount of "final_result" is: {len(final_result)}')
    return final_result


create_scraper_rules()
# new_url = "https://rabota.by/vacancies/podrabotka?area=2237&clusters=true&page=3"
# scrap(new_url)


@app.route("/")
def applic():
    pass
#
#
# def get_rabota_result(search_query):
#     # url = "https://rabota.by/search/vacancy?text=&area=1002&area=2237&salary=&currency_code=BYR&experience=" \
#     #   "doesNotMatter&order_by=relevance&search_period=30&items_on_page=20&no_magic=true&grouping=AREA&datasetName=" \
#     #   "&utm_source=google&utm_medium=cpc&utm_campaign=S%20%7C%20%D0%A1%D0%BE%D0%B8%D1%81%D0%BA%D0%B0%D1%82%D0%B5%D0%BB%" \
#     #   "D0%B8%20%7C%20%D0%9C%D0%B8%D0%BD%D1%81%D0%BA&utm_content=applicant_BY_minsk&utm_term=%D1%80%D0%B0%D0%B1%D0%BE%D1%" \
#     #   "82%D0%B0%20%D0%B2%20%D0%BC%D0%B8%D0%BD%D1%81%D0%BA%D0%B5&gclid=EAIaIQobChMI99rUj7_O8wIVg-F3Ch1hNArvEAAYASAAEgJjDvD_BwE"
#
#     url = "https://www.amazon.in/s?k=%s" % search_query
#
#     result = rabota_scraper.get_result_similar(url, group_by_alias=True)
#     return _aggregate_result(result)
#
# def _aggregate_result(result):
#     final_result = []
#     print(list(result.values())[0])
#     for i in range(len(list(result.values())[0])):
#         try:
#             final_result.append({alias: result[alias][i] for alias in result})
#         except:
#             pass
#     return final_result
#
# @app.route("/", methods={"GET"})
# def search_api():
#     query = request.args.get("q")
#     print(query)
#     # return dict(result=get_rabota_result(query))
#     return jsonify(query)
#
# # get_rabota_result()
#
#


if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")
