# edge-detection

**Edge detector for gray scale images**

Steps:

-> Smoothing the input image using a Gaussian filter.

-> Using the Sobel operator to compute the image gradients, and then compute the gradient magnitude.

-> Using thresholding to get the edges.

Experimentation was done by changing sigma and threshold values as below:

![image](https://user-images.githubusercontent.com/79351706/108866327-1d6f6900-761a-11eb-99c9-3d375fc6149c.png)

![image](https://user-images.githubusercontent.com/79351706/108866535-4c85da80-761a-11eb-8991-ae0dfd8a9c36.png)

![image](https://user-images.githubusercontent.com/79351706/108866705-74753e00-761a-11eb-843c-d8c043ec1a62.png)
