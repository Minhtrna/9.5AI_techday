
# IMPORTANT
When using imto3dv2.py speed is slow when calling api maybe due to internet speed of the server or the limit of free sup 
get huggingface pro may reduce the generate time. 

for greatest performance please use imto3dv2.ipynb <a target="_blank" href="https://colab.research.google.com/github/https://colab.research.google.com/github/Minhtrna/9.5AI_techday/blob/main/imto3dv2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

or https://www.kaggle.com/code/minhtranv/image-to-3d-web-app-with-gradio-and-ngrok


# How to use 

## ACCESS TOKEN

![image](https://github.com/user-attachments/assets/79826df4-ef30-4559-a11d-0069f8d1bdb5)

requires a token generated from, remember to gain READ in token setting: https://huggingface.co/settings/tokens
also u need to fill in the access form in this link : https://huggingface.co/stabilityai/stable-fast-3d

## Best performance

Following step in 

<a target="_blank" href="https://colab.research.google.com/github/https://colab.research.google.com/github/Minhtrna/9.5AI_techday/blob/main/imto3dv2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

if colab runout of compute unit then use kaggle : https://www.kaggle.com/code/minhtranv/image-to-3d-web-app-with-gradio-and-ngrok

the app will be access via the public link 

![image](https://github.com/user-attachments/assets/8d86d949-9b7e-4bca-8bd6-8f6000d4aa32)

While runing on kaggle. Kaggle block direct web deploy on thier server so we need to use ngrok to create a tunnel link to our local host on kaggle server 
You will access app via tunel link. Remember to read instruction in kaggle 

app should look like this 

![image](https://github.com/user-attachments/assets/1cab368e-11ba-471e-9efa-d7a8a0c6b675)

## Slower way

create a folder named: Github , then u need to set the clone directory in to that folder.

which should look like that : ./Github

then clone the repo to github folder u created before

final link should look like : ./Github/9.5AI_techday

 library require
 1 : gradio 
 2 : Opencv

Finally run imto3dv2.py and the app will deploy in the local link which will show in your terminal. 



