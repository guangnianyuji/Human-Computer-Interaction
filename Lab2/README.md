# Lab 2: Information Retrieval

## Function

1. Upload a image.
2. Overview the total number of the similar images.
3. Overview the tags of all results .
4. Add the images to the favorite.
5. Click the favorite to see the favorite images.
6. Click on tag button to see the images which hold this tag only.
8. Clear the image and choose another one.

## Development Environment

- **Development Environment:** Win 11
- **Development Software:**
  1. PyCharm 2023.1 (Community Edition)
  1. Google Chrome  版本109.0.5414.120
- **Development Language:**
  1. python3.9
  2. HTML
  3. JavaScript
  4. CSS
  5. jQuery

## Project Structure

```
│  README.md   
│  Report.md   
│  Report.pdf   
├─picture
└─lab2-image-retrieval  
    │  rest-server.py   
    │  
    ├─database   
    │  ├─dataset   
    │  └─tag  
    ├─imagenet
    ├─uploads
    ├─static   
    │  ├─css   
    │  │      imgtable.css   
    │  │      imgtag.css   
    │  │      jumbotron-narrow.css
    │  │      bootstrap.min.css
    │  │      bootstrap.min.css.map
    │  │
    │  ├─images   
    │  │      ajax-loader.gif   
    │  │      background.jpg
    │  │      ico.jpg
    │  │      
    │  ├─js   
    │  │      bootstrap.js   
    │  │      bootstrap.min.js   
    │  │      jquery.min.js   
    │  │      myjs.js   
    │  ├─dataset      
    │  └─result   
    └─templates   
            syfmain.html   
```



## How to Run

1. **File configuration from the folder 'lab2-image-retrieval' the teacher provided:**
   - Please replace folder **'static'** with mine. 
   - Please replace folder **'templates'** with mine. 
   - Please replace the file **image_vectorizor.py** with mine.
   - Please replace the file **rest-server.py** with mine.
   - Please copy folder **'database/dataset'** into folder **'static'**.
   - Final the folder structure will be as above.
2. Start the server by **running image_vectorizor.py and rest-server.py**. This project uses flask based REST implementation for UI.

```
  cd Lab2-image-retrieval/server
  python image_vectorizer.py
  python rest-server.py 
```

3. Once the server starts up, access <http://localhost:5000/> to get the UI. 

   PS:You shoule open in Google Chrome,other browser may show unsuccessfully.

   ![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab2/picture/1.png?raw=true)

4. **Upload** any image and click "**Search!**", then you can see the image and loading icon.

   ![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab2/picture/2.png?raw=true)

5. You can  see 9 images and all the tags.

   ![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab2/picture/3.png?raw=true)

6. You can **click the tag button** , and then you will see the images which have this tag only.

   ![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab2/picture/4.png?raw=true)

7. You can **add any image to the favorites**, it means you want to hold it in the favorites.

   ![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab2/picture/5.png?raw=true)

8. **Click the favorites button**, then you will see the images which you collect.

   ![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab2/picture/6.png?raw=true)

10. Click "**Clear**" to get back to the homepage, and you can upload another image again.



