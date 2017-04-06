#task_7

american_date = "05.17.2016"
month_american = american_date[3:6]
day_american = american_date[0:3]
year = american_date[7:]
european_date = month_american + day_american + year
print(european_date)

# task_8

first_str = "Элeктpooтpицaтeльнocть мoлeкyляpнoй мaccы вeщecтвa " \
            "пoдчиняeтcя зaкoнy Aвoгaдpo и плaнeтapнoй мoдeли aтoмa и cвязaнa кoвaлeнтнoй cвязью"
second_str = "Yчитывaя кoмбинaтopныe пpoцeccы, инкopпopиpyющиe " \
             "языки aгглютиниpyютcя блaгoдapя тeopии вoлнoвoй " \
             "coнopнocти, диcкpeдитиpyющeй тpaнcцeндeнтaльныe гипepo- гипoнимичecкиe cвязи"
mid_idx = len(second_str)//2
one_sec_str = second_str[0:mid_idx]
two_sec_str = second_str[mid_idx:]
new_s_s = one_sec_str + first_str + two_sec_str
print(new_s_s)

mid_idx1 = len(first_str)//2
one_fir_srt = first_str[0:mid_idx1]
two_fir_str = first_str[mid_idx1:]
new_f_s = one_fir_srt + new_s_s + two_fir_str

print(new_f_s)

# task_9

word = "sdkfj laskf sadkfs"
sec_w = word.split()
sec_w1 = sec_w[1].upper()
new_word = sec_w[0] + " " + sec_w1 + " " + sec_w[2]

print(new_word)

# task_10

leo = "Leo Tolstoy*1828-08-28*1910-11-20"
idx1 = leo.find('*')
name = leo[:idx1]
idx2 = leo.find('-')
date_idx = leo.find('*', idx1 + 1)
birthday = leo[idx1 + 1:idx2]
full_final = leo[date_idx + 1:]
en_idx2 = full_final.find('-')
final = full_final[:en_idx2]
count_years = int(final) - int(birthday)

print(name + "," + " " + str(count_years))
