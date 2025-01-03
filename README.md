# Ex.06 Book Front Cover Page Design
## Date: 02-12-2024

## AIM:
To design a book front cover page using HTML and CSS.

## DESIGN STEPS:

### Step 1:
Create a Django Admin project.

### Step 2:
Create an app in the Django interface.

### Step 3:
Create a folder named 'static' in the app folder.

### Step 4:
Create a new HTML file in the static folder.

### Step 5:
Write the HTML code with relevant CSS properties.

### Step 6:
Choose the appropriate style and color scheme.

### Step 7:
Insert the images in their appropriate places.

### Step 8:
Publish the website in the LocalHost.

## PROGRAM:
```
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Cover</title>
</head>
<body style="margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; background:white; height: 100vh;">

    <div style="width: 400px; height: 600px; background: linear-gradient(to bottom right, white, orange); padding: 20px; box-shadow: 0 4px 8px black(0, 0, 0, 0.2); border-radius: 10px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        
        <div style="text-align: center; margin-top: 20px;">
            <h1 style="font-size: 2rem; color:black; margin: 0;">Web Designing</h1>
            <p style="font-size: 1.2rem; color:grey; margin-top: 10px;">Learn HTML and CSS the Easy Way</p>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <div style="font-size: 0.9rem; color:grey;">
                <p style="margin: 0;">8th Edition</p>
                <p style="margin: 0;">Author: Tharunish Vasan.T</p>
                <p style="margin: 5px 0 0;"> SEC</p>
            </div>

            <div style="text-align: center;">
                <img src="img.jpg" alt="Author Photo" style="width: 70px; height: 90px; object-fit: cover; border-radius: 10px; border: 2px solid grey;">
                <p style="font-size: 0.9rem; color:black; margin-top: 5px; font-weight: bold;">SEC</p>
            </div>
        </div>
    </div>
</body>
</html>

```


## OUTPUT:

![alt text](<Screenshot 2024-12-02 232811.png>)


## RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
