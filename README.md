# SimilarLineFromDMM

>
In this repository, I saved the files for my personal app which does: 
####  1) web scraping from "DMM English uknow" site pages on Python and *selenium* package, 
   - ./local_files/1. Scraping_DMM_uKnow.ipynb 
   ![](./img/SimilarLineFromDMM_01.JPG)
</br>

####  2) establishment of data pipeline to calculate Japanese sentence similarity based on TF-IDF processed over scraped Japanese sentences at step 1) and encoded by *MeCab*, 
   - ./local_files/2. Generate Sentence Similarity.ipynb
</br>

####  3) deployment as an app returning similar Japanese sentence by similarity order against user-posted Japanese sentence using *Flask*, and 
   - ./AWS_files/similarity.py
   - ./AWS_files/app.py
</br>

####  4) making the app externally accessible through HTML by running it on AWS Linux instance.
</br>

