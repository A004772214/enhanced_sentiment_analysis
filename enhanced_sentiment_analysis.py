from lm import LM
import datetime
import os
import csv

start_time = datetime.datetime.now()

ca_pdf_path = "Your_file_path"

header_written = False


for root, path, files in os.walk(ca_pdf_path):
    for file in files:
        file_name = str(file).rstrip(".txt")
        file_path = root + "//" + file

        try:

            with open(file_path, "r+", encoding="utf-8", errors='ignore') as txt:
                element_text_list = txt.readlines()
            element_txt_str = " ".join(element_text_list)

            word_count = len(element_text_list)

            lm = LM()
            tokens = lm.tokenize(element_txt_str)
            score = lm.get_score(tokens)

            extra_key = "File"
            extra_value = file_name

            country_code = extra_value.split("_")[0]
            year = extra_value.split("_")[1]
            firm_code = extra_value.split("_")[2]
            report_type = extra_value.split("_")[3]

            country_code_key = "country_code"
            year_key = "year"
            firm_code_key = "firm_code"
            report_type_key = "report_type"

            score_with_file_name = {extra_key: extra_value, country_code_key: country_code, year_key: year, firm_code_key: firm_code, report_type_key: report_type}
            score_with_file_name.update(score)

            print(score_with_file_name)

            csv_file = root + "//" + "Your_file_name.csv"

            with open(csv_file, 'a', newline='') as csvfile:
                # Create a csv writer object
                csvwriter = csv.writer(csvfile)

                # Write the header (keys of the first dictionary)

                if not header_written:
                    csvwriter.writerow(score_with_file_name.keys())
                    header_written = True

                # Write the data (values of each dictionary)
                csvwriter.writerow(score_with_file_name.values())

            print(f"Sentiment Analysis Score of {file_name} has been exported to {csv_file}")
        except Exception as e:
            print(e)

finish_time = datetime.datetime.now()
total_time = finish_time - start_time

print(total_time)





