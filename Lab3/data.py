import re

#根据软件类别和是否收费筛选行
def category_price_filter(file,category_name, price_choice):
    newfile = []

    for row in file:
        if category_name=='ALL' or row[1] == category_name:
            if price_choice == 'All':
                newfile.append(row)
            elif price_choice == 'Free' and row[7] == '0':
                newfile.append(row)
            elif price_choice == 'Paid' and row[7] != '0':
                newfile.append(row)

    return newfile


def parse_installs(installs):
    numeric_value = int(installs.replace(',', '').replace('+', ''))
    return numeric_value
def get_dot(file):
    Rating=[]
    Installs = []  # 下载数
    App = []  # App的名称
    for row in file:
        if row[0] != 'App':
            App.append(row[0])

        if row[3] != 'Rating':
            Rating.append(row[2])

        if row[5] != 'Installs':
            Installs.append(parse_installs(row[5]))



    return [Rating, Installs, App]
#下载量和数据收集
def get_size(newfile):

    size_category = [
        '0~300K', '300K~600K', '600K~900K', '900K~25M', '25M~50M',
        '50M~75M','75M~100M', 'Varies with device'
    ]
    size_list = []
    for i in range(len(size_category)):
        size_list.append(0)
    variesNum = 0

    for row in newfile:

        if row[4][-1] == 'M':
            num = float(row[4][0:-1])
            size_list[int(num // 25) + 3] += 1
        elif row[4][-1] == 'k':
            num = float(row[4][0:-1])
            if num > 900:
                size_list[3] += 1
            else:
                size_list[int(num // 300)] += 1
        elif row[4] == 'Varies with device':
            size_list[-1] += 1

    return [size_category, size_list]

def get_price(newfile):

    price_list=[]

    for row in newfile:

        if row[7] == 'Price':
            continue
        elif row[7] == '0':
            price_list.append(0)
        else:
            price_list.append(float(row[7][1:]))
    x_list=list(set(price_list))
    y_list=[]
    for i,x in enumerate(x_list):
        y_list.append(price_list.count(x))

    return x_list,y_list

def get_ratingpeople(newfile):
    rating_category = [
        'Everyone', 'Teen', 'Everyone 10+',
        'Mature 17+', 'Adults only 18+', 'Unrated'
    ]
    ratingpeople_list=[]

    for i in range(len(rating_category)):
        ratingpeople_list.append(0)

    for row in newfile:
        if row[8] != "Content Rating":
            ratingpeople_list[rating_category.index(row[8])] += 1

    return rating_category,ratingpeople_list

def get_color(temp,maxCount):
    return 'rgb({r}, {g}, {b})'.format(
        r=int((temp/maxCount)*200),
        g=int((1-temp/maxCount)*200),
        b=int((1-temp/maxCount)*200)
    )

def get_ratingcount(newfile):
    ratingcount_list=[]
    for row in newfile:
        if row[2]!='NaN' and row[2]!='Rating':
            ratingcount_list.append(float(row[2]))
    maxcount=len(ratingcount_list)

    xlist = list(set(ratingcount_list))
    ylist = []
    for i, x in enumerate(xlist):
        ylist.append(ratingcount_list.count(x))

    colorlist=[]

    for i,y in enumerate(ylist):
        colorlist.append(get_color(y,maxcount))



    return xlist,ylist,colorlist

