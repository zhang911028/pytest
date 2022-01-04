import pymysql
import openpyxl
import os


wb = openpyxl.Workbook(write_only=True)
ws = wb.create_sheet("data")
os.chdir(r"D:\pythontest\pytest\demo")

conn_drds_smc_clc_prd = pymysql.connect(host='10.68.72.177', user='chizhou',
                                        password='EzM6v3uu', db='drds_smc_clc_prd', charset='utf8')

cursor_daiyuguanli = conn_drds_smc_clc_prd.cursor()

sql = f'select '
