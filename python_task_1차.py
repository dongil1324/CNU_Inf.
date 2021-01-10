# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:08:08 2021

@author: Psh
"""

swim=('sw','hy')
run=('gh','sh')
bowling=('sw','gh')
badminton=('hy','sw')
all_name=swim+run+bowling+badminton
sh_score=all_name.count('sh')
hy_score=all_name.count('hy')
sw_score=all_name.count('sw')
gh_score=all_name.count('gh')
result=[[("전파정보통신공학과",'한승우','202033333'), sw_score],
        [("전파정보통신공학과",'이건하','202044444'), gh_score],
        [("전파정보통신공학과",'오혜윤','202022222'), hy_score],
        [("전파정보통신공학과",'박서현','202011111'), sh_score]]
result[2][1]=hy_score-0.5
result[0][1]=sw_score-0.5