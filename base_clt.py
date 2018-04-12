
import pandas as pd
path="D:/Tangui/2_Projet_total/base_client_et_commandes/dsi_customer_export_2018_03.csv"

clt=pd.read_csv(path, error_bad_lines=False,sep=";",encoding='utf-8',dtype={"clt_num_tel_jour": str})

import math

clt=clt[~clt['clt_id'].isna()]

len_new_file=len(clt)
path2=path.split(".csv")[0]+'_clean.csv'

path_len_last_month='/'.join(path.split('/')[0:-1])+'/len_last_month.txt'
file= open(path_len_last_month, "r")
len_last=file.readline()
if(int(len_last)>len_new_file):
    print("error : Le fichier du mois dernier contenait plus de clients")
elif (int(len_last)==len_new_file):
    print("Attention : Le fichier du mois dernier contenait le même nombre de clients ")
else:
    clt.to_csv(path2, sep=";", index=False, encoding='utf-8-sig', float_format='%.0f')
    file = open(path_len_last_month, "w")
    file.write(str(len_new_file))
    file.close()

