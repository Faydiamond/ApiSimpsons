# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:26:43 2022

@author: Fabian Barbon
"""
class imageSimpson:
    def randomLetter (self):
        import random 
        import string
        self.rstr = random.choice(string.ascii_letters)
        return  self.rstr
    
    def randonNumber(self):
        from random import randint
        return randint(0,555)
    
    def saveImg(self,imgg,request):
        from PIL import Image
        self.imgg     = imgg
        self.request  = request
        with open(self.imgg, 'wb') as f:
            f.write(self.request.data)
        # creating a object
        im = Image.open(self.imgg)
        im.show()
        
    def saveImgRepeat (self,imagge,reqque):
        self.imagge    = imagge.split('.')
        self.reqque    = reqque
        self.letterOne = self.randomLetter()
        self.letterTwo = self.randomLetter()
        self.imagge = '{img}.{number}.{lOne}{lTwoo}.png'.format(img=self.imagge[0],number=self.imagge[1],lOne=self.letterOne,lTwoo=self.letterTwo )
        self.saveImg(self.imagge,reqque)

    def request (self):
        import json
        import requests
        import urllib3
        
        self.response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
        self.todos = json.loads(self.response.text)
        self.image = self.todos[0]['image']
        self.http = urllib3.PoolManager()
        self.req = self.http.request('GET', self.image)
        
       
        self.nameimg = 'img.{}.png'.format(self.randonNumber())
        print('Numero  ' , self.nameimg)
        try:
            file = open( self.nameimg )
            print("existe")
            print(file) # File handler
            self.saveImgRepeat(self.nameimg , self.req)
        except FileNotFoundError:
            print('No existe')
            self.saveImg(self.nameimg , self.req)
   
        
    
    
imgSim = imageSimpson()
imgSim.request()
imgSim.randonNumber()