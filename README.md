[![Build Status](https://travis-ci.com/leomuskul/JKU-cloud-computing_WS20.svg?branch=main)](https://travis-ci.com/leomuskul/JKU-cloud-computing_WS20)

<h2>What the project about</h2>
<p>The Jupyter Notebook has become a popular user interface for cloud computing, and major cloud providers have adopted the Jupyter Notebook or derivative tools as a frontend interface for cloud users. Examples include Amazon's SageMaker Notebooks, Google's Colaboratory and Microsoft's Azure Notebook.</p>
<p>Colaboratory (also known as Colab) is a free Jupyter notebook environment that runs in the cloud and stores its notebooks on Google Drive. Colab was originally an internal Google project; an attempt was made to open source all the code and work more directly upstream, leading to the development of the "Open in Colab" Google Chrome extension, but this eventually ended, and Colab development continued internally. As of October 2019, the Colaboratory UI only allows you to create notebooks with Python 2 and Python 3 kernels; however, if you have an existing notebook whose kernelspec is IR or Swift, that will work, since both R and Swift are installed in the container. Julia language can also work on Colab (with e.g. Python and GPUs; Google's tensor processing units also work with Julia on Colab).</p>
<p>It is possible to build an own server wich would compute machine learning tasks like Google Colaboratory does</p> 

<h3>What should be done:</h3>
<center><img src="https://github.com/leomuskul/JKU-cloud-computing_WS20/blob/main/Code/Picture1.jpg" alt="Supposed scheme"></center>

<ol>
	<li>Run the remote server wich would provide a performance with cloud technology that we have learned in "class"</li>
	<li>Do a <a href="https://nextjournal.com/gkoehler/pytorch-mnist">tutorial task</a> on both environment (on a server with and without cloud technology and on a client computer)</li>
	<li>Compare the impact of cloud technology</li>
</ol>

Big Thanks to authors:<br>
-  <a href='https://github.com/ghego/travis_anaconda_jupyter'>travis_anaconda_jupyter</a>
- <a href="https://nextjournal.com/gkoehler/pytorch-mnist">Gregor Koehler</a>