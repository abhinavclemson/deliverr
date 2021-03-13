import requests
from collections import defaultdict
import json


class DeliverrModel:

        #Constructor for the DeliverrModel
        def __init__(self, url=None, access_token=None):

            self.url = url
            self.access_token = access_token
            self.model = {}
            self.__prod_detail = defaultdict(list)


        #private function for internal use
        def __isValidResponse(self):
            """for error handling"""

            #presuming response is correct
            return True



        def getAllProducts(self):
            #for accessing all available items in Customer's Catalog

            url = self.url
            access_token =self.access_token

            #for authentication
            params = {
                "access_token": access_token,
                "format": "json",
            }

            #using Post HTTP request to get all the available products details as response
            response = requests.post(url, params=params)


            #converting the response into json type
            json_res = response.json()

            #further filtering the response
            data =json_res['data']


            for product in data:


                self.filter(product)



            return json.dumps(self.__prod_detail)




        #private function for internal use
        def filter(self, product):

            prod_detail= self.__prod_detail


            for val in product.values():

                title = val['description']


                variants = val['variants']

                for var in variants:

                    var = var["Variant"]
                    sku = var['sku']
                    product_id = var['product_id']


                    prod_dic = {
                        "productid": product_id,
                        "sku": sku,
                        "title": title
                    }

                    prod_detail["Product"].append(prod_dic)







if __name__=='__main__':
    url = "https://merchant.wish.com/api/v2/product/multi-get"

    # Here I have used my token you can replace it with your, it would work.
    access_token = "bb3325853daa45e4ae77135e9c71b90e"

    obj = DeliverrModel()

    obj.access_token = access_token
    obj.url = url

    response  = obj.getAllProducts()

    print(response)





