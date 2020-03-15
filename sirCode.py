from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from games.models import Game
from games.models import MyModel
from games.serializers import GameSerializer
from games.serializers import DataSerializer
import pandas as pd



class CreateMYSQLInstance:
    def __init__(self):
        from sqlalchemy import create_engine
        # create sqlalchemy engine
        self.engine = create_engine("mysql+pymysql://{user}:{pw}@192.168.0.106:3306/{db}"
                       .format(user="root",
                               pw="pass@1234",
                               db="mydatabase"))
        print("CreateMYSQLInstance")
        print(self.engine)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'           
        super(JSONResponse, self).__init__(content, **kwargs)



@csrf_exempt
def createmodel(request,modeltopredict=""):
    print("create Model")
    if request.method == 'GET': 
        #modeltopredict="rf"
        import pandas as pd
        mydata=  pd.read_csv("wiki_movie_plots_deduped.csv")
        mydata = mydata.fillna('')
        #preprocessing logic
        import nltk
        nltk.download('stopwords')
        from nltk.corpus import stopwords
        from nltk.stem.porter import PorterStemmer        

        import re
        corpus = []

        for i in range(0, len(mydata)):
            review = re.sub('[^a-zA-Z]', ' ', mydata['Plot'][i])
            review = review.lower()
            review = review.split()
            ps = PorterStemmer()
            review = [ps.stem(word) for word in review if not word iwn set(stopwords.words('english'))]
            review = ' '.join(review)
            corpus.append(review)
  
        # Creating the Bag of Words model
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer(max_features = 2500)
        X = cv.fit_transform(corpus).toarray()    
        y = mydata.iloc[:, 2].values
        
        from sklearn.externals import joblib
        joblib.dump(cv, "cv")
        
        import pickle as pt
        dbfile= open('pcv','ab')
        pt.dump(cv, dbfile)
        
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        Y=le.fit_transform(y)

        import numpy as np
        np.save("lec",le.classes_)
        
        
        if modeltopredict.lower() == 'rf':        
            from sklearn.ensemble import RandomForestClassifier
            rf = RandomForestClassifier(n_estimators=7)
            rf.fit(X,Y)
            
            import pickle as pt
            dbfile2 = open('rf', 'ab')    
            # source, destination 
            pt.dump(rf, dbfile2)                     
            dbfile2.close() 
            
        #nlp logic
        print("converting Json")
        print( mydata )
        return JSONResponse("Model created")


@csrf_exempt
def predictmodel(request,modeltouse="",Description=""):
    print("Predict Model")
    #Description=""" Grandma Louisa (Spring Byington) begins dating grocer Henry Hammond (Edmund Gwenn), much to the disgust of her son Hal (Ronald Reagan) and the rest of the family. To make matters worse, Hala’s boss, Mr. Burnside (Charles Coburn), also becomes a rival for Louisa’s affections """
    #print(Description)
    modeltouse="rf"
    
    if request.method == 'GET': 
        import pandas as pd
        mydata=  "prdicted genere" 
        print("predict model logic")
        if modeltouse== 'rf':
            innerdata = []
            innerdata.append(Description)
            predictdata=[]
            predictdata.append(innerdata)
            newdata = pd.DataFrame(predictdata,columns=['Plot'])

            import nltk
            nltk.download('stopwords')
            from nltk.corpus import stopwords
            from nltk.stem.porter import PorterStemmer        

            import re
            corpus = []

            for i in range(0, len(newdata)):
                review = re.sub('[^a-zA-Z]', ' ', newdata['Plot'][i])
                review = review.lower()
                review = review.split()
                ps = PorterStemmer()
                review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
                review = ' '.join(review)
                corpus.append(review)            
        
        from sklearn.externals import joblib
        CV = joblib.load("cv")
        XPREDICT2 = CV.transform(corpus).toarray()
        
        import pickle  as pt    
        dbfileload = open('pcv', 'rb')    
        cov =  pt.load(dbfileload)
        XPREDICT = cov.transform(corpus).toarray()
        
        dbfilerf = open('rf', 'rb')    
        rfp =  pt.load(dbfilerf)
        PRED= rfp.predict(XPREDICT)
        
        import numpy as np
        from sklearn.preprocessing import LabelEncoder
        le2 = LabelEncoder()
        le2.classes_= np.load("lec.npy",allow_pickle=True)
        predicteddata=le2.inverse_transform(PRED)

        
        print( predicteddata[0] )
        return JSONResponse(predicteddata[0])


