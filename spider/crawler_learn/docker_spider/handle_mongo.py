import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient(host='192.168.199.140',port=27017)
db = client['docker_appium_data']


def handle_save_data(item):
    #抖音
    if item['item_type'] == 'douyin_item':
        print('3333333333333333333333')
        douyin_data_collection = Collection(db,'douyin')
        douyin_data_collection.insert(item)
    #快手
    elif item['item_type'] == 'kuaishou_item':
        kuaishou_data_collection = Collection(db,'kuaishou')
        kuaishou_data_collection.insert(item)
    #今日头条
    elif item['item_type'] == 'jinritoutiao_item':
        jinritoutiao_data_collection = Collection(db,'jintitoutiao')
        jinritoutiao_data_collection.insert(item)
