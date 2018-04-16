# coding: utf-8
__author__ = "Yemilice_lau"

import requests

a = requests.get("https://wxapp.58.com/list/detail?isRefreshOnLoginBack=false&loading=true&pageInfo=&pageType=detail&pageName=detail&title=&btnFlag=true&verifyload=false&verifyPic=&verifyValue=&verifyFocus=true&currInfoId=&currentCateCode=&detail=&hideApplyButton=true&resumeId=&applyed=false&isTelAlertShow=false&telNum=&telCountTime=180&dispLocalName=cd&cateCode=2&infoId=33761762144430&dispCateName=hezu&cateId=0&appCode=1", verify=False)
print(a.text)