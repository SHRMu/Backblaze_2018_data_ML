import datetime
# 计算与2018-01-01的时间间隔作为时间序列标识
def time_interval_from_fileName(fileName):
    date_start = datetime.datetime(2018,1,1)
    # 硬盘当前的记录时间从文件名中解析
    date = fileName.split('.')[0]
    year = date.split('-')[0]
    month = date.split('-')[1]
    day = date.split('-')[2]
    date_end = datetime.datetime(int(year),int(month),int(day))
    # print(str(year) + '-' + str(month) + '-' + str(day))
    interval = date_end - date_start
    return interval.days

# 
def time_interval_to_fileName(time_interval):
    day_start = datetime.datetime(2018,1,1)
    day_end = day_start + datetime.timedelta(days = time_interval)
    fileName = str(day_end).split(' ')[0] + ".csv"
    return fileName