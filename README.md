# hanzi-writer-data-in-javascript
 Each characters json in JavaScript file.
 
As we can access js and image file using this
```html
<script src="some-js-file.js"></script>
<img src="some-image.png"></img>
```

To access json 
I have tried same steps but getting ```CORS``` error so I used next steps.
```
<script src="我.json" type="application/json"></script>
```

With example,
To access ```我.json``` file 

#### 1. Copy contents of ```我.json``` into a javascript file, with any variable name
```
var chr_data = {"strokes":["M 350 571 Q 3....}
```
#### 2. Add following tag to access that js file
```html
<!--  Note : file type & name -->
<script src="我.js" type="text/javascript"></script>
```

#### 3. Now also change code in ```_hanzi-writer.min.js```

To change code, first beautify code using this ``` https://beautifier.io```, then make following change
a) Remove the link to load from internet  
b) Change this ``` 200 != r.status ``` and replace/add this ```JSON.parse(JSON.stringify(chr_data))```
( May more good replacement can be done here )

![change_code](https://user-images.githubusercontent.com/12841290/83772020-804c5900-a6b5-11ea-9c0a-59b8ae7a45e0.PNG)

```javascript
....
....
// Note :  chr_data variable come from 我.js file
r.overrideMimeType && r.overrideMimeType("application/json"), r.open("GET", "", !0), r.onerror = function(t) {
....
....
 4 === r.readyState && (200 != r.status ? i(JSON.parse(JSON.stringify(chr_data))) : 0 !== r.status && n && n(r))
....
....

```
#### 4. So final script will be like this
Front side of card
```html
{{Pinyin}}

<div id="character-target-div"></div>

<script src= "我.js" type="text/javascript"></script>
<script>
var data = JSON.stringify(chr_data);
console.log(data);
</script>

<script src="_hanzi-writer.min.js"></script>

<script>
var writer = HanziWriter.create('character-target-div', '', {
  width: 150,
  height: 150,
  showCharacter: false,
  padding: 5
});
writer.quiz();
</script>
```

<b>Above all the steps are for single file 我.js 
It may not work on Anki Desktop because I have tried and sometime working sometime not working.
</b>
To access other character repeat the same.

# License
[HanziWriter](https://github.com/chanind/hanzi-writer-data)
