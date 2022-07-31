import scrapy
import pandas as pd
import json
import numpy as np


class A02GettingProductsRatingSpider(scrapy.Spider):
    name = 'frag'

#    start_urls=['https://api.bazaarvoice.com/data/reviews.json?Filter=contentlocale%3Aen*&Filter=ProductId%3AP483156&Sort=SubmissionTime%3Adesc&Limit=6&Offset=0&Include=Products%2CComments&Stats=Reviews&passkey=caQ0pQXZTqFVYA1yYnnJ9emgUiW59DXA85Kxry8Ma02HE&apiversion=5.4&Locale=en_US']
    start_urls=['https://api.bazaarvoice.com/data/reviews.jsonhttps://api.bazaarvoice.com/data/reviews.json']

    def parse(self, response):
            
            ids = pd.read_csv('C:/Users/Nadir/Desktop/B/Projects/Fragrance_project/data/data_products_ids.csv')

            # Loop over all the products
            for i in ids.index:
                    num=0
                    pr = 1

                        
                    #Get the product id number i 
                    product_id = ids['prod_id'][i]


                    URL = "https://api.bazaarvoice.com/data/reviews.json?Filter=contentlocale%3Aen*&Filter=ProductId%3A"+str(product_id)+"&Sort=SubmissionTime%3Adesc&Limit=100&Offset=0&Include=Products%2CComments&Stats=Reviews&passkey=caQ0pQXZTqFVYA1yYnnJ9emgUiW59DXA85Kxry8Ma02HE&apiversion=5.4&Locale=en_US"
                        
                    yield response.follow(URL,callback=self.parse_Product_detail,meta={'index':i,'pr':pr,'product_i':product_id})
                


            # Product index
            pr=pr+1
            
            yield 


    def parse_Product_detail(self,response):
        data=json.loads(response.body)

        # Scrape Info about the product using the productID that we got 
        items = {
            'product_id':data['Includes']['Products'][response.meta['product_i']]['Id'],
            'Brand':data['Includes']['Products'][response.meta['product_i']]['Brand']['Name'],
            'Name':data['Includes']['Products'][response.meta['product_i']]['Name'],
            'Description':data['Includes']['Products'][response.meta['product_i']]['Description'],
            'recommended':data['Includes']['Products'][response.meta['product_i']]['ReviewStatistics']['RecommendedCount'],
            'not_recommended':data['Includes']['Products'][response.meta['product_i']]['ReviewStatistics']['NotRecommendedCount'],

            'overall_rating':data['Includes']['Products'][response.meta['product_i']]['ReviewStatistics']['AverageOverallRating'],

                    
                    
            'max_review':data['TotalResults'],

            'produit':response.meta['pr'],
            'User1':data['Results'][0]['Rating'],
            'User2':data['Results'][1]['Rating'],
            'User3':data['Results'][2]['Rating'],
            'User4':data['Results'][3]['Rating'],
            'User5':data['Results'][4]['Rating'],
            'User6':data['Results'][5]['Rating'],
            
            'User7':data['Results'][0]['Rating'],
            'User8':data['Results'][1]['Rating'],
            'User9':data['Results'][2]['Rating'],
            'User10':data['Results'][3]['Rating'],
            'User11':data['Results'][4]['Rating'],
            'User12':data['Results'][5]['Rating'],

            'User13':data['Results'][0]['Rating'],
            'User14':data['Results'][1]['Rating'],
            'User15':data['Results'][2]['Rating'],
            'User16':data['Results'][3]['Rating'],
            'User17':data['Results'][4]['Rating'],
            'User18':data['Results'][5]['Rating'],

            'User19':data['Results'][0]['Rating'],
            'User20':data['Results'][1]['Rating'],
            'User21':data['Results'][2]['Rating'],
            'User22':data['Results'][3]['Rating'],
            'User23':data['Results'][4]['Rating'],
            'User24':data['Results'][5]['Rating'],

            'User25':data['Results'][0]['Rating'],
            'User26':data['Results'][1]['Rating'],
            'User27':data['Results'][2]['Rating'],
            'User28':data['Results'][3]['Rating'],
            'User29':data['Results'][4]['Rating'],
            'User30':data['Results'][5]['Rating'],

            'User31':data['Results'][0]['Rating'],
            'User32':data['Results'][1]['Rating'],
            'User33':data['Results'][2]['Rating'],
            'User34':data['Results'][3]['Rating'],
            'User35':data['Results'][4]['Rating'],
            'User36':data['Results'][5]['Rating'],

            'User37':data['Results'][0]['Rating'],
            'User38':data['Results'][1]['Rating'],
            'User39':data['Results'][2]['Rating'],
            'User40':data['Results'][3]['Rating'],
            'User41':data['Results'][4]['Rating'],
            'User42':data['Results'][5]['Rating'],
            
            'User43':data['Results'][0]['Rating'],
            'User44':data['Results'][1]['Rating'],
            'User45':data['Results'][2]['Rating'],
            'User46':data['Results'][3]['Rating'],
            'User47':data['Results'][4]['Rating'],
            'User48':data['Results'][5]['Rating'],

            'User49':data['Results'][0]['Rating'],
            'User50':data['Results'][1]['Rating'],
            'User51':data['Results'][2]['Rating'],
            'User52':data['Results'][3]['Rating'],
            'User53':data['Results'][4]['Rating'],
            'User54':data['Results'][5]['Rating'],

            'User55':data['Results'][0]['Rating'],
            'User56':data['Results'][1]['Rating'],
            'User57':data['Results'][2]['Rating'],
            'User58':data['Results'][3]['Rating'],
            'User59':data['Results'][4]['Rating'],
            'User60':data['Results'][5]['Rating'],

            'User61':data['Results'][0]['Rating'],
            'User62':data['Results'][1]['Rating'],
            'User63':data['Results'][2]['Rating'],
            'User64':data['Results'][3]['Rating'],
            'User65':data['Results'][4]['Rating'],
            'User66':data['Results'][5]['Rating'],

            'User67':data['Results'][0]['Rating'],
            'User68':data['Results'][1]['Rating'],
            'User69':data['Results'][2]['Rating'],
            'User70':data['Results'][3]['Rating'],
            'User71':data['Results'][4]['Rating'],
            'User72':data['Results'][5]['Rating'],

            'User1':data['Results'][0]['Rating'],
            'User73':data['Results'][1]['Rating'],
            'User74':data['Results'][2]['Rating'],
            'User75':data['Results'][3]['Rating'],
            'User76':data['Results'][4]['Rating'],
            'User77':data['Results'][5]['Rating'],
            
            'User78':data['Results'][0]['Rating'],
            'User79':data['Results'][1]['Rating'],
            'User80':data['Results'][2]['Rating'],
            'User81':data['Results'][3]['Rating'],
            'User82':data['Results'][4]['Rating'],
            'User83':data['Results'][5]['Rating'],

            'User84':data['Results'][0]['Rating'],
            'User85':data['Results'][1]['Rating'],
            'User86':data['Results'][2]['Rating'],
            'User87':data['Results'][3]['Rating'],
            'User88':data['Results'][4]['Rating'],
            'User89':data['Results'][5]['Rating'],

            'User90':data['Results'][0]['Rating'],
            'User91':data['Results'][1]['Rating'],
            'User92':data['Results'][2]['Rating'],
            'User93':data['Results'][3]['Rating'],
            'User94':data['Results'][4]['Rating'],
            'User95':data['Results'][5]['Rating'],

            'User96':data['Results'][0]['Rating'],
            'User97':data['Results'][1]['Rating'],
            'User98':data['Results'][2]['Rating'],
            'User99':data['Results'][3]['Rating'],
            'User100':data['Results'][4]['Rating'],



        
        }


        print(items)
        print(len(items))


        yield items