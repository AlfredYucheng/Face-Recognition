# Face-Recognition
###
1. The logic behind the flow
For the first step I read the image and transfer the image to data in numpy array in length = 300
Then I split the data to three variables r,g,b refer to the value of red, green and blue for each pixel.
For the next step, I set up k*3 random number between 0 to 255 as our initial centroids and I also set up the label space for label for every pixel.

Then we get into the learning part. For each generation, we first assign every points to the nearst center. The logic is that: for every point, we go through all the k centers and calculate the distance, and if we find out ta smaller distance than current center's, we change the label of this point.

After we assign all the pixels to the nearest center, we then recalculate the new center based on the label. I go through all the labels and add up the r/g/b value group by label.And then I take average of them update the new center.

And we repeat the previous two step till there is no change to the label, we return the label and the center value.
###
2.explain the variables

img_color : read the image.
r,g,b : the values of red/ green, blue for every pixels
rsig,gsig,bsig : the standard deviation of r,g,b.

pre : the place to save the previous label information
centroid: the place I save the information of each center
label: the place I save the information of which group each pixel belong to.
change: an indicator of wheather there is a change to label. If not, the loop is end.

temp: refer to the current distance between the current point and the current center I go through.
mindis: refer to minimum distance, if I see a smaller distance, the mindis will be updated
label_count and the while label_count < len(centroid): go through all the pixel and make sure all the values are sum up group by label.
t_r,  t_g, t_b : total value of red / green / blue
count : refer to the number of each label.
###
3.limitation:
Actually the algorithm can be improved by rewrite some of the logic inside the loop to avoid extreme long running time and unnecessary calculation(memory). One of the main problem is that the loop takes really a long time to run especially when we increase the k value.
The other problem is that the loop is unstable due to the random initial center points.
we can solve this problem by two ways: 1. repeat the loop for a few times. 2. introduce the k-means + algorithm.
