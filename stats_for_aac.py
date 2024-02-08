# Statistics for an Athletic Association
# source = https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python

import statistics
def stat(strg):
    if strg  == "" :   
        result_string = ""
        
    else :
        result = []
        for timeStrg in strg.split(', ') :
            time = []
            i = 0
        
            for unit in timeStrg.split('|'): 
                time.append(int(unit)*(60**(2-i)))
                i += 1
            result.append(sum(time))
        result_string = "Range: %s Average: %s Median: %s" %((hms(max(result)-min(result))),(hms(int(statistics.mean(result)))),(hms(int(statistics.median(result)))))
    return result_string

def hms(seconds):
    h , remain_s =divmod(seconds,3600)
    m , s =divmod(remain_s,60)
    return f"{h:02d}|{m:02d}|{s:02d}"

print(stat("11|15|59, 10|16|16, 12|17|20, 9|22|34, 13|19|34, 11|15|17, 11|22|00, 10|26|37, 12|17|48, 9|16|30, 12|20|14, 11|25|11"))
