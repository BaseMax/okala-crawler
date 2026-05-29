# okala-crawler

## Data

Here are list of several store IDs, and all main categories IDs.

```
stores = [
    "https://www.okala.com/store/2319",
    "https://www.okala.com/store/10458",
    "https://www.okala.com/store/9871",
    "https://www.okala.com/store/9652",
    "https://www.okala.com/store/2318",
    "https://www.okala.com/store/10381",
    "https://www.okala.com/store/9020",
    "https://www.okala.com/store/9768",
    "https://www.okala.com/store/8840",
    "https://www.okala.com/store/5989",
    "https://www.okala.com/store/10650",
    "https://www.okala.com/store/7500",
    "https://www.okala.com/store/8131",
    "https://www.okala.com/store/9867",
    "https://www.okala.com/store/7791",
    "https://www.okala.com/store/8729",
    "https://www.okala.com/store/9991",
    "https://www.okala.com/store/8662",
]

categories = [
    "https://www.okala.com/store/2319/browse/kalabarg?rootId=1467",
    "https://www.okala.com/store/2319/browse/refreshments?rootId=1467",
    "https://www.okala.com/store/2319/browse/dairy-products?rootId=1462",
    "https://www.okala.com/store/2319/browse/groceries?rootId=1461",
    "https://www.okala.com/store/2319/browse/home-hygiene?rootId=1471",
    "https://www.okala.com/store/2319/browse/beverages?rootId=1465",
    "https://www.okala.com/store/2319/browse/spices?rootId=1469",
    "https://www.okala.com/store/2319/browse/canned-ready-food?rootId=1464",
    "https://www.okala.com/store/2319/browse/cosmetics-hygiene?rootId=1472",
    "https://www.okala.com/store/2319/browse/proteins?rootId=1463",
    "https://www.okala.com/store/2319/browse/breakfast-goods?rootId=1466",
    "https://www.okala.com/store/2319/browse/home-stuff?rootId=1473",
    "https://www.okala.com/store/2319/browse/baby-mother-care?rootId=1474",
    "https://www.okala.com/store/2319/browse/fruits-vegetables?rootId=1470",
    "https://www.okala.com/store/2319/browse/nuts-sweets?rootId=1468",
    "https://www.okala.com/store/2319/browse/multiples?rootId=1850",
]
```

## Requests

Get stores and some products inside each stores in a spefic category

```bash
curl 'https://apigateway.okala.com/api/unicorn/v2/products/nearby?slug=refreshments&lat=35.805851&lon=51.431311' \
  -H 'X-Skip-Authorization: false' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEzRjRFNUExQ0NGNUU4NjRBQTI3MzgyMkM3OENERTIxQTM4MkRBOENSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IkVfVGxvY3oxNkdTcUp6Z2l4NHplSWFPQzJvdyJ9.eyJuYmYiOjE3ODAwNTIxMjAsImV4cCI6MTc4MDA1MzkyMCwiaXNzIjoiaHR0cDovL2NlcmJlcnVzLm1lbWJlcnNoaXAiLCJjbGllbnRfaWQiOiJjdXN0b21lcl9jbGllbnRfaWQiLCJzdWIiOiIxMTE1NzA1MCIsImF1dGhfdGltZSI6MTc4MDA1MDIxNCwiaWRwIjoibG9jYWwiLCJ1c2VySWQiOiIxMTE1NzA1MCIsInVzZXJuYW1lIjoiMDkxMzQ5NTA3ODciLCJhbHRlcm5hdGl2ZUN1c3RvbWVySWQiOiIxMTE1NzA1MCIsInRlbmFudCI6Im9rYWxhIiwidG9rZW4taWQiOiJjMjc4OTcyNi0wNjhlLTQ3MDYtYTgwYi00ZDNjMzBmNzkxMzVfOWFjYTg2ODItMjA3YS00MjkwLTgxMzAtZjYxNWNiZGM2NWJiIiwiY2VyYmVydXNJZCI6ImMyNzg5NzI2LTA2OGUtNDcwNi1hODBiLTRkM2MzMGY3OTEzNSIsImp0aSI6IkUxRDEwRkZGRkM0QUZGQTE2RkZCRDFBMDUxOEZCODJDIiwiaWF0IjoxNzgwMDUyMTIwLCJzY29wZSI6WyJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsiY3VzdG9tZXJfZ3JhbnRfdHlwZSJdfQ.HM1nH-plzP4JXg8UUcCAZdUs4Vo_Nmqaj7g6cDSO1dEDWk1f9rmddKaKsfVaO2qDcKccZJ58cZQJ71Km3XXadXOzZPn7ic9cNERiLazDO1SjBznxyI6ncdSg-rQ0judXwhElW47oQa1JAFvJiEGv_Bg1PaVFsCnzaqLtSpXFdyfGApUMVpymkpCr1um8aK2HDHYkiv8dgZxdTKlUnWNktXqFDEKin0jvhTs9uupJE6ITaIlOft8eKZiufznlaIQNTnTfKdwaDxo3x7M-JgnJ89ULUlwEcOBBgE0X-Q0q0vENK4whtLxxcPUefATvrQWsRHoz3jKLq7XXyyGVMGHDfw' \
  -H 'X-Correlation-Id: 8a22fa5c-28f0-4ebb-8ed5-7052f7d76f2c' \
  -H 'sec-ch-ua: "Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"' \
  -H 'X-User-Unique-Id: 32063c6e-098f-437f-8777-291d5d7c3786' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'ui-version: 2.0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'metrix_user_id: null' \
  -H 'session-id: 2958b08b-3627-4d55-be9d-dd819d4c9cd9' \
  -H 'advertising_id: null' \
  -H 'Referer;' \
  -H 'idfa: null' \
  -H 'source: okala' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
```

Response:

```json
{
    "data": [
        {
            "store": {
                "rank": 12,
                "storeId": 7791,
                "storeName": "شمیرانات اندرزگو",
                "firstDeliveryTime": "60 دقیقه",
                "logo": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/logo/a77f7e22-fbb1-4bdb-b21b-77c82d062e01.png",
                "distance": 1.507182540488638,
                "rate": 4.5,
                "hasOnDemandDelivery": true,
                "hasActiveOperatingHour": true,
                "isActive": true,
                "deliveryPrice": 0,
                "storeTypeId": 1,
                "deliveryMethods": [
                    {
                        "title": "Delivery",
                        "description": "ارسال با پیک"
                    },
                    {
                        "title": "Pickup",
                        "description": "تحویل حضوری"
                    }
                ]
            },
            "products": [
                {
                    "storeId": 7791,
                    "maxOrderLimit": 5,
                    "discountPercent": 50,
                    "isShowDiscount": true,
                    "quantity": 60,
                    "hasQuantity": true,
                    "id": 182424,
                    "name": "کروسان با مغز کاکائویی مکس پچ پچ 50 گرمی",
                    "price": 450000.0,
                    "okPrice": 225000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/8cc162e7-ef18-47bf-a969-c93fb537892b.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194755
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 50,
                    "discountPercent": 29,
                    "isShowDiscount": true,
                    "quantity": 87,
                    "hasQuantity": true,
                    "id": 200751,
                    "name": "کروسان با مغزی کرم کاکائویی دوبل پچ پچ 70 گرمی",
                    "price": 620000.0,
                    "okPrice": 435000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/5d685329-acd9-4872-a6d3-24179687443f.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195122
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 5,
                    "discountPercent": 50,
                    "isShowDiscount": true,
                    "quantity": 22,
                    "hasQuantity": true,
                    "id": 182425,
                    "name": "کروسان با مغز کاکائو فندقی مکس پچ پچ 50 گرمی",
                    "price": 450000.0,
                    "okPrice": 225000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/20b48630-32fd-4edb-be05-96cba401e181.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194987
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 10,
                    "discountPercent": 0,
                    "isShowDiscount": true,
                    "quantity": 1,
                    "hasQuantity": true,
                    "id": 18,
                    "name": "ویفر رنگارنگ مینو 14.5 گرمی",
                    "price": 120000.0,
                    "okPrice": 119000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/5549a571-01b0-44a7-bae1-19cf7afea320.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195396
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 50,
                    "discountPercent": 6,
                    "isShowDiscount": true,
                    "quantity": 38,
                    "hasQuantity": true,
                    "id": 2424,
                    "name": "اسنک کرانچی پنیری چی توز 95 گرمی ",
                    "price": 1000000.0,
                    "okPrice": 940000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/6575de1e-9039-496a-bb21-ad67ea8045be.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195362
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 50,
                    "discountPercent": 12,
                    "isShowDiscount": true,
                    "quantity": 16,
                    "hasQuantity": true,
                    "id": 2865,
                    "name": "چيپس سيب زمينی سرکه نمكی چی توز 60 گرمی",
                    "price": 700000.0,
                    "okPrice": 615000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/169b4733-2361-40d6-b928-1157092940f2.JPG",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194927
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 50,
                    "discountPercent": 5,
                    "isShowDiscount": true,
                    "quantity": 16,
                    "hasQuantity": true,
                    "id": 2864,
                    "name": "چيپس سيب زمينی ساده نمكی چی توز 60 گرمی",
                    "price": 700000.0,
                    "okPrice": 665000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/47dbdc0c-4c9f-42fb-92f5-cead6abbc9e4.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195035
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 50,
                    "discountPercent": 8,
                    "isShowDiscount": true,
                    "quantity": 9,
                    "hasQuantity": true,
                    "id": 3273,
                    "name": "اسنك پنيری طلايی چی توز 90 گرمی",
                    "price": 900000.0,
                    "okPrice": 828000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/2bbcf6ce-0404-401b-815a-7ff7bc26ae0f.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195153
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 50,
                    "discountPercent": 12,
                    "isShowDiscount": true,
                    "quantity": 9,
                    "hasQuantity": true,
                    "id": 2867,
                    "name": "چيپس پياز و جعفری چی توز 60 گرمی",
                    "price": 700000.0,
                    "okPrice": 615000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/16660dcd-6a53-45e8-b772-8d1b8450e946.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195020
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 50,
                    "discountPercent": 8,
                    "isShowDiscount": true,
                    "quantity": 19,
                    "hasQuantity": true,
                    "id": 8888,
                    "name": "اسنک چرخی چی توز 80 گرمی",
                    "price": 900000.0,
                    "okPrice": 828000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/7fdd5647-c763-45d5-9c82-db64f49c342f.JPG",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195211
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 50,
                    "discountPercent": 19,
                    "isShowDiscount": true,
                    "quantity": 7,
                    "hasQuantity": true,
                    "id": 203401,
                    "name": "کیک مینیز مافینز 160 گرمی سلفون 20 عددی هپی پچ پچ",
                    "price": 980000.0,
                    "okPrice": 785000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/7bd7d9ee-f966-4b46-bc6c-e7ebb28fc242.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194869
                },
                {
                    "storeId": 7791,
                    "maxOrderLimit": 10,
                    "discountPercent": 5,
                    "isShowDiscount": true,
                    "quantity": 50,
                    "hasQuantity": true,
                    "id": 3545,
                    "name": "بیسکویت مادر ممتاز ویتانا 70 گرمی ",
                    "price": 359000.0,
                    "okPrice": 339000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/7321ba4d-dbdf-425a-b3c8-34ae95e35ec0.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195011
                }
            ],
            "suppliedCount": 12,
            "exactMatchCount": 0,
            "totalScore": 1.2383472846011989E+17,
            "personalizedCount": 0
        },
        {
            "store": {
                "rank": 15,
                "storeId": 53664,
                "storeName": "کیا دربندسری",
                "firstDeliveryTime": "60 دقیقه",
                "logo": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/logo/a77f7e22-fbb1-4bdb-b21b-77c82d062e01.png",
                "distance": 1.6217119926940406,
                "rate": 4.4,
                "hasOnDemandDelivery": true,
                "hasActiveOperatingHour": true,
                "isActive": true,
                "deliveryPrice": 0,
                "storeTypeId": 1,
                "deliveryMethods": [
                    {
                        "title": "Delivery",
                        "description": "ارسال با پیک"
                    }
                ]
            },
            "products": [
                {
                    "storeId": 53664,
                    "maxOrderLimit": 5,
                    "discountPercent": 50,
                    "isShowDiscount": true,
                    "quantity": 105,
                    "hasQuantity": true,
                    "id": 182424,
                    "name": "کروسان با مغز کاکائویی مکس پچ پچ 50 گرمی",
                    "price": 450000.0,
                    "okPrice": 225000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/8cc162e7-ef18-47bf-a969-c93fb537892b.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194755
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 5,
                    "discountPercent": 32,
                    "isShowDiscount": true,
                    "quantity": 47,
                    "hasQuantity": true,
                    "id": 200751,
                    "name": "کروسان با مغزی کرم کاکائویی دوبل پچ پچ 70 گرمی",
                    "price": 620000.0,
                    "okPrice": 416392.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/5d685329-acd9-4872-a6d3-24179687443f.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195122
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 5,
                    "discountPercent": 50,
                    "isShowDiscount": true,
                    "quantity": 55,
                    "hasQuantity": true,
                    "id": 182425,
                    "name": "کروسان با مغز کاکائو فندقی مکس پچ پچ 50 گرمی",
                    "price": 450000.0,
                    "okPrice": 225000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/20b48630-32fd-4edb-be05-96cba401e181.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194987
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 10,
                    "discountPercent": 0,
                    "isShowDiscount": false,
                    "quantity": 23,
                    "hasQuantity": true,
                    "id": 18,
                    "name": "ویفر رنگارنگ مینو 14.5 گرمی",
                    "price": 120000.0,
                    "okPrice": 120000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/5549a571-01b0-44a7-bae1-19cf7afea320.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195396
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 50,
                    "discountPercent": 6,
                    "isShowDiscount": true,
                    "quantity": 7,
                    "hasQuantity": true,
                    "id": 2424,
                    "name": "اسنک کرانچی پنیری چی توز 95 گرمی ",
                    "price": 1000000.0,
                    "okPrice": 940000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/6575de1e-9039-496a-bb21-ad67ea8045be.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195362
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 50,
                    "discountPercent": 12,
                    "isShowDiscount": true,
                    "quantity": 37,
                    "hasQuantity": true,
                    "id": 2865,
                    "name": "چيپس سيب زمينی سرکه نمكی چی توز 60 گرمی",
                    "price": 700000.0,
                    "okPrice": 615000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/169b4733-2361-40d6-b928-1157092940f2.JPG",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194927
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 50,
                    "discountPercent": 5,
                    "isShowDiscount": true,
                    "quantity": 11,
                    "hasQuantity": true,
                    "id": 2864,
                    "name": "چيپس سيب زمينی ساده نمكی چی توز 60 گرمی",
                    "price": 700000.0,
                    "okPrice": 665000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/47dbdc0c-4c9f-42fb-92f5-cead6abbc9e4.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195035
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 20,
                    "discountPercent": 0,
                    "isShowDiscount": false,
                    "quantity": 16,
                    "hasQuantity": true,
                    "id": 8696,
                    "name": "بیسكويت پتی بور طعم دار مینو 100 گرمی",
                    "price": 450000.0,
                    "okPrice": 450000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/11a6ef04-71ab-430f-acee-d96216626a7c.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194558
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 50,
                    "discountPercent": 19,
                    "isShowDiscount": true,
                    "quantity": 4,
                    "hasQuantity": true,
                    "id": 203401,
                    "name": "کیک مینیز مافینز 160 گرمی سلفون 20 عددی هپی پچ پچ",
                    "price": 980000.0,
                    "okPrice": 785000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/7bd7d9ee-f966-4b46-bc6c-e7ebb28fc242.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194869
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 10,
                    "discountPercent": 5,
                    "isShowDiscount": true,
                    "quantity": 42,
                    "hasQuantity": true,
                    "id": 3545,
                    "name": "بیسکویت مادر ممتاز ویتانا 70 گرمی ",
                    "price": 359000.0,
                    "okPrice": 339000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/7321ba4d-dbdf-425a-b3c8-34ae95e35ec0.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195011
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 50,
                    "discountPercent": 0,
                    "isShowDiscount": false,
                    "quantity": 25,
                    "hasQuantity": true,
                    "id": 32871,
                    "name": "كرانچی تند و آتشین چی توز 75 گرمی",
                    "price": 1000000.0,
                    "okPrice": 1000000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/178eb600-ae7a-4bbe-aa4e-0df09399069a.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195320
                },
                {
                    "storeId": 53664,
                    "maxOrderLimit": 5,
                    "discountPercent": 50,
                    "isShowDiscount": true,
                    "quantity": 12,
                    "hasQuantity": true,
                    "id": 18002,
                    "name": "ویفر شکلاتی با کرم نارگیل کوپا 30 گرمی",
                    "price": 350000.0,
                    "okPrice": 175000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/f5004ce1-262f-4583-8f70-2ea561648e4a.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194603
                }
            ],
            "suppliedCount": 12,
            "exactMatchCount": 0,
            "totalScore": 1.2383472846011989E+17,
            "personalizedCount": 0
        },
        {
            "store": {
                "rank": 5,
                "storeId": 2319,
                "storeName": "دربند",
                "firstDeliveryTime": "60 دقیقه",
                "logo": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/logo/a77f7e22-fbb1-4bdb-b21b-77c82d062e01.png",
                "distance": 0.5272027734695012,
                "rate": 4.7,
                "hasOnDemandDelivery": true,
                "hasActiveOperatingHour": true,
                "isActive": true,
                "deliveryPrice": 0,
                "storeTypeId": 1,
                "deliveryMethods": [
                    {
                        "title": "Delivery",
                        "description": "ارسال با پیک"
                    },
                    {
                        "title": "Pickup",
                        "description": "تحویل حضوری"
                    }
                ]
            },
            "products": [
                {
                    "storeId": 2319,
                    "maxOrderLimit": 5,
                    "discountPercent": 50,
                    "isShowDiscount": true,
                    "quantity": 236,
                    "hasQuantity": true,
                    "id": 182424,
                    "name": "کروسان با مغز کاکائویی مکس پچ پچ 50 گرمی",
                    "price": 450000.0,
                    "okPrice": 225000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/8cc162e7-ef18-47bf-a969-c93fb537892b.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 194755
                },
                {
                    "storeId": 2319,
                    "maxOrderLimit": 50,
                    "discountPercent": 29,
                    "isShowDiscount": true,
                    "quantity": 69,
                    "hasQuantity": true,
                    "id": 200751,
                    "name": "کروسان با مغزی کرم کاکائویی دوبل پچ پچ 70 گرمی",
                    "price": 620000.0,
                    "okPrice": 435000.0,
                    "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/5d685329-acd9-4872-a6d3-24179687443f.jpg",
                    "isBundle": false,
                    "supplyStatus": 1,
                    "masterProductId": 195122
                },
...
```

### Get all products in a spefic store and spefic category

**Store ID:** 7791

**Category ID:** 1467

**Category Slug:** refreshments

```bash
curl 'https://apigateway.okala.com/api/unicorn/v2/products/store/7791?pC_Id=1467&slug=refreshments' \
  -H 'X-Skip-Authorization: false' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEzRjRFNUExQ0NGNUU4NjRBQTI3MzgyMkM3OENERTIxQTM4MkRBOENSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IkVfVGxvY3oxNkdTcUp6Z2l4NHplSWFPQzJvdyJ9.eyJuYmYiOjE3ODAwNTIxMjAsImV4cCI6MTc4MDA1MzkyMCwiaXNzIjoiaHR0cDovL2NlcmJlcnVzLm1lbWJlcnNoaXAiLCJjbGllbnRfaWQiOiJjdXN0b21lcl9jbGllbnRfaWQiLCJzdWIiOiIxMTE1NzA1MCIsImF1dGhfdGltZSI6MTc4MDA1MDIxNCwiaWRwIjoibG9jYWwiLCJ1c2VySWQiOiIxMTE1NzA1MCIsInVzZXJuYW1lIjoiMDkxMzQ5NTA3ODciLCJhbHRlcm5hdGl2ZUN1c3RvbWVySWQiOiIxMTE1NzA1MCIsInRlbmFudCI6Im9rYWxhIiwidG9rZW4taWQiOiJjMjc4OTcyNi0wNjhlLTQ3MDYtYTgwYi00ZDNjMzBmNzkxMzVfOWFjYTg2ODItMjA3YS00MjkwLTgxMzAtZjYxNWNiZGM2NWJiIiwiY2VyYmVydXNJZCI6ImMyNzg5NzI2LTA2OGUtNDcwNi1hODBiLTRkM2MzMGY3OTEzNSIsImp0aSI6IkUxRDEwRkZGRkM0QUZGQTE2RkZCRDFBMDUxOEZCODJDIiwiaWF0IjoxNzgwMDUyMTIwLCJzY29wZSI6WyJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsiY3VzdG9tZXJfZ3JhbnRfdHlwZSJdfQ.HM1nH-plzP4JXg8UUcCAZdUs4Vo_Nmqaj7g6cDSO1dEDWk1f9rmddKaKsfVaO2qDcKccZJ58cZQJ71Km3XXadXOzZPn7ic9cNERiLazDO1SjBznxyI6ncdSg-rQ0judXwhElW47oQa1JAFvJiEGv_Bg1PaVFsCnzaqLtSpXFdyfGApUMVpymkpCr1um8aK2HDHYkiv8dgZxdTKlUnWNktXqFDEKin0jvhTs9uupJE6ITaIlOft8eKZiufznlaIQNTnTfKdwaDxo3x7M-JgnJ89ULUlwEcOBBgE0X-Q0q0vENK4whtLxxcPUefATvrQWsRHoz3jKLq7XXyyGVMGHDfw' \
  -H 'X-Correlation-Id: 0adab688-6ff2-4938-adfd-752c67f2f419' \
  -H 'sec-ch-ua: "Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"' \
  -H 'X-User-Unique-Id: 32063c6e-098f-437f-8777-291d5d7c3786' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'ui-version: 2.0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'metrix_user_id: null' \
  -H 'session-id: 2958b08b-3627-4d55-be9d-dd819d4c9cd9' \
  -H 'advertising_id: null' \
  -H 'Referer: https://www.okala.com/' \
  -H 'idfa: null' \
  -H 'source: okala' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
```

Response:

```json
{
    "data": [
        {
            "storeId": 7791,
            "maxOrderLimit": 5,
            "discountPercent": 50,
            "isShowDiscount": true,
            "quantity": 62,
            "hasQuantity": true,
            "id": 182424,
            "name": "کروسان با مغز کاکائویی مکس پچ پچ 50 گرمی",
            "price": 450000.0,
            "okPrice": 225000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/8cc162e7-ef18-47bf-a969-c93fb537892b.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705010000,
            "masterProductId": 194755
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 50,
            "discountPercent": 29,
            "isShowDiscount": true,
            "quantity": 87,
            "hasQuantity": true,
            "id": 200751,
            "name": "کروسان با مغزی کرم کاکائویی دوبل پچ پچ 70 گرمی",
            "price": 620000.0,
            "okPrice": 435000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/5d685329-acd9-4872-a6d3-24179687443f.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009998,
            "masterProductId": 195122
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 5,
            "discountPercent": 50,
            "isShowDiscount": true,
            "quantity": 25,
            "hasQuantity": true,
            "id": 182425,
            "name": "کروسان با مغز کاکائو فندقی مکس پچ پچ 50 گرمی",
            "price": 450000.0,
            "okPrice": 225000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/20b48630-32fd-4edb-be05-96cba401e181.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009997,
            "masterProductId": 194987
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 10,
            "discountPercent": 0,
            "isShowDiscount": true,
            "quantity": 1,
            "hasQuantity": true,
            "id": 18,
            "name": "ویفر رنگارنگ مینو 14.5 گرمی",
            "price": 120000.0,
            "okPrice": 119000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/5549a571-01b0-44a7-bae1-19cf7afea320.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009996,
            "masterProductId": 195396
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 50,
            "discountPercent": 6,
            "isShowDiscount": true,
            "quantity": 38,
            "hasQuantity": true,
            "id": 2424,
            "name": "اسنک کرانچی پنیری چی توز 95 گرمی ",
            "price": 1000000.0,
            "okPrice": 940000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/6575de1e-9039-496a-bb21-ad67ea8045be.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009994,
            "masterProductId": 195362
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 50,
            "discountPercent": 5,
            "isShowDiscount": true,
            "quantity": 16,
            "hasQuantity": true,
            "id": 2864,
            "name": "چيپس سيب زمينی ساده نمكی چی توز 60 گرمی",
            "price": 700000.0,
            "okPrice": 665000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/47dbdc0c-4c9f-42fb-92f5-cead6abbc9e4.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009992,
            "masterProductId": 195035
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 50,
            "discountPercent": 12,
            "isShowDiscount": true,
            "quantity": 16,
            "hasQuantity": true,
            "id": 2865,
            "name": "چيپس سيب زمينی سرکه نمكی چی توز 60 گرمی",
            "price": 700000.0,
            "okPrice": 615000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/169b4733-2361-40d6-b928-1157092940f2.JPG",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009991,
            "masterProductId": 194927
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 50,
            "discountPercent": 8,
            "isShowDiscount": true,
            "quantity": 9,
            "hasQuantity": true,
            "id": 3273,
            "name": "اسنك پنيری طلايی چی توز 90 گرمی",
            "price": 900000.0,
            "okPrice": 828000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/2bbcf6ce-0404-401b-815a-7ff7bc26ae0f.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009990,
            "masterProductId": 195153
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 50,
            "discountPercent": 8,
            "isShowDiscount": true,
            "quantity": 19,
            "hasQuantity": true,
            "id": 8888,
            "name": "اسنک چرخی چی توز 80 گرمی",
            "price": 900000.0,
            "okPrice": 828000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/7fdd5647-c763-45d5-9c82-db64f49c342f.JPG",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009989,
            "masterProductId": 195211
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 50,
            "discountPercent": 12,
            "isShowDiscount": true,
            "quantity": 9,
            "hasQuantity": true,
            "id": 2867,
            "name": "چيپس پياز و جعفری چی توز 60 گرمی",
            "price": 700000.0,
            "okPrice": 615000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/16660dcd-6a53-45e8-b772-8d1b8450e946.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009988,
            "masterProductId": 195020
        },
        {
            "storeId": 7791,
            "maxOrderLimit": 10,
            "discountPercent": 5,
            "isShowDiscount": true,
            "quantity": 50,
            "hasQuantity": true,
            "id": 3545,
            "name": "بیسکویت مادر ممتاز ویتانا 70 گرمی ",
            "price": 359000.0,
            "okPrice": 339000.0,
            "imageUrl": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/7321ba4d-dbdf-425a-b3c8-34ae95e35ec0.jpg",
            "isBundle": false,
            "supplyStatus": 1,
            "docRankT": 10319560705009985,
            "masterProductId": 195011
        },
...
```

### Get details of a product

For example:

**Store ID:** 7791

**Product ID:** 182424

```bash
curl 'https://apigateway.okala.com/api/Unicorn/v1/catalog/pdp?sId=7791&pId=182424' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9,fa;q=0.8,it;q=0.7,tr;q=0.6' \
  -H 'advertising_id: null' \
  -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEzRjRFNUExQ0NGNUU4NjRBQTI3MzgyMkM3OENERTIxQTM4MkRBOENSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IkVfVGxvY3oxNkdTcUp6Z2l4NHplSWFPQzJvdyJ9.eyJuYmYiOjE3ODAwNTIxMjAsImV4cCI6MTc4MDA1MzkyMCwiaXNzIjoiaHR0cDovL2NlcmJlcnVzLm1lbWJlcnNoaXAiLCJjbGllbnRfaWQiOiJjdXN0b21lcl9jbGllbnRfaWQiLCJzdWIiOiIxMTE1NzA1MCIsImF1dGhfdGltZSI6MTc4MDA1MDIxNCwiaWRwIjoibG9jYWwiLCJ1c2VySWQiOiIxMTE1NzA1MCIsInVzZXJuYW1lIjoiMDkxMzQ5NTA3ODciLCJhbHRlcm5hdGl2ZUN1c3RvbWVySWQiOiIxMTE1NzA1MCIsInRlbmFudCI6Im9rYWxhIiwidG9rZW4taWQiOiJjMjc4OTcyNi0wNjhlLTQ3MDYtYTgwYi00ZDNjMzBmNzkxMzVfOWFjYTg2ODItMjA3YS00MjkwLTgxMzAtZjYxNWNiZGM2NWJiIiwiY2VyYmVydXNJZCI6ImMyNzg5NzI2LTA2OGUtNDcwNi1hODBiLTRkM2MzMGY3OTEzNSIsImp0aSI6IkUxRDEwRkZGRkM0QUZGQTE2RkZCRDFBMDUxOEZCODJDIiwiaWF0IjoxNzgwMDUyMTIwLCJzY29wZSI6WyJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsiY3VzdG9tZXJfZ3JhbnRfdHlwZSJdfQ.HM1nH-plzP4JXg8UUcCAZdUs4Vo_Nmqaj7g6cDSO1dEDWk1f9rmddKaKsfVaO2qDcKccZJ58cZQJ71Km3XXadXOzZPn7ic9cNERiLazDO1SjBznxyI6ncdSg-rQ0judXwhElW47oQa1JAFvJiEGv_Bg1PaVFsCnzaqLtSpXFdyfGApUMVpymkpCr1um8aK2HDHYkiv8dgZxdTKlUnWNktXqFDEKin0jvhTs9uupJE6ITaIlOft8eKZiufznlaIQNTnTfKdwaDxo3x7M-JgnJ89ULUlwEcOBBgE0X-Q0q0vENK4whtLxxcPUefATvrQWsRHoz3jKLq7XXyyGVMGHDfw' \
  -H 'idfa: null' \
  -H 'metrix_user_id: null' \
  -H 'origin: https://www.okala.com' \
  -H 'priority: u=1, i' \
  -H 'sec-ch-ua: "Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'session-id: 2958b08b-3627-4d55-be9d-dd819d4c9cd9' \
  -H 'source: okala' \
  -H 'ui-version: 2.0' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36' \
  -H 'x-correlation-id: 4fac4316-e21e-4530-aabe-d114136d4d40' \
  -H 'x-skip-authorization: false' \
  -H 'x-user-unique-id: 32063c6e-098f-437f-8777-291d5d7c3786'
```

Response:

```json
{
    "id": 182424,
    "storeId": 7791,
    "storeName": "شمیرانات اندرزگو",
    "name": "کروسان با مغز کاکائویی مکس پچ پچ 50 گرمی",
    "okPrice": 225000.0,
    "price": 450000.0,
    "quantity": 60,
    "supplyStatus": 1,
    "isBundle": false,
    "isShowDiscount": true,
    "categoryName": "کیک و کلوچه",
    "categoryWebLink": "/category/cake-muffins-pastry",
    "description": "کروسان با مغز کاکائویی مکس پچ پچ 50 گرمی",
    "brandName": "پچ پچ",
    "brandLatinName": "Pechpech",
    "brandImage": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/brand/176534.png",
    "images": [
        "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn/product/8cc162e7-ef18-47bf-a969-c93fb537892b.jpg"
    ],
    "discountPercent": 50,
    "storeTypeId": 1,
    "maxOrderLimit": 5
}
```

## Author

Copyright 2026, Seyyed Ali Mohammadiyeh (MAX BASE)

License MIT
