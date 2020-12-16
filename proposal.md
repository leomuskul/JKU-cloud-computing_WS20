<h2>What the project about</h2>
<p>The Jupyter Notebook has become a popular user interface for cloud computing, and major cloud providers have adopted the Jupyter Notebook or derivative tools as a frontend interface for cloud users. Examples include Amazon's SageMaker Notebooks, Google's Colaboratory and Microsoft's Azure Notebook.</p>
<p>Colaboratory (also known as Colab) is a free Jupyter notebook environment that runs in the cloud and stores its notebooks on Google Drive. Colab was originally an internal Google project; an attempt was made to open source all the code and work more directly upstream, leading to the development of the "Open in Colab" Google Chrome extension, but this eventually ended, and Colab development continued internally. As of October 2019, the Colaboratory UI only allows you to create notebooks with Python 2 and Python 3 kernels; however, if you have an existing notebook whose kernelspec is IR or Swift, that will work, since both R and Swift are installed in the container. Julia language can also work on Colab (with e.g. Python and GPUs; Google's tensor processing units also work with Julia on Colab).</p>
<p>It is possible to build an own "server" wich would compute machine learning tasks.</p>

<h3>What should be done: Build a pipeline to get a MNIST model with CI</h3> 
<li>Source code of a <a href="https://nextjournal.com/gkoehler/pytorch-mnist">task</a> to run is uploaded from a client to GitHub repository.</li>
<li>Travis CI sees a new commit and executes the step from the build pipeline.</li>
<li>"Server" downloads the code, runs it and uploads back to repository.</li>
<li>Travis again sees a new commit and executes the next step.</li>
<li>Client gets the message from Travis and downloads the modified code back.</li></ul>
<p align="middle">
<img src="https://github.com/leomuskul/JKU-cloud-computing_WS20/blob/main/code/Picture1.jpg?raw=true" alt="pipeline"></p>
