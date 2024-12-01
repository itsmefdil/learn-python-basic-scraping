# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import pymongo
import sqlite3


class MongodbPipeline:
    collection_name = "transcripts"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://fadil:fadil@cluster0.c29s4zv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client["My_Database"]
        logging.warning("Spider Opened")

    def close_spider(self, spider):
        self.client.close()
        logging.warning("Spider Closed")


    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item

class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("transcripts.db")
        self.c = self.connection.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS transcripts(
                title TEXT,
                plot TEXT,
                transcript text,
                url TEXT
            )
        ''')

        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()
        # logging.warning("Spider Closed")


    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO transcripts (title, plot, transcript, url) VALUES(?,?,?,?)
        ''', (
                item.get('title'),
                item.get('plot'),
                item.get('transcript'),
                item.get('url'),
        ))
        self.connection.commit()
        return item
