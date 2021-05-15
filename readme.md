# Heart-Saver

[![Contributors](https://img.shields.io/github/contributors/dsckgec/heart-saver.svg)](https://github.com/dsckgec/heart-saver/graphs/contributors) [![Forks](https://img.shields.io/github/forks/dsckgec/heart-saver.svg)](https://github.com/dsckgec/heart-saver/network/members) [![Issues](https://img.shields.io/github/issues/dsckgec/heart-saver.svg)](https://github.com/dsckgec/heart-saver/issues) [![Pull Request](https://img.shields.io/github/issues-pr-closed-raw/dsckgec/heart-saver)](https://github.com/dsckgec/heart-saver/pulls)


A basic GitHub repository template for initializing open source projects on a single click.


1. [Description](#description)
2. [Getting started](#getting-started)
3. [Project Structure](#project-structure)
4. [Live demo](#live-demo)
5. [Contributing](#contributing)
6. [Authors](#authors)
7. [License](#license)

## Description

Is your heart healthy enough? Do you want to predict whether you risk a heat attack? Then this project is for you!<br/>
Use your ML skills to predict the chances of a person will suffer from a heart attack.<br/> Don't forget to try to increase its accuracy!

## Project structure

```
  ├── datasets/         Dataset of heart-saver.
  ├── notebooks/        Contains the jupyter notebook files of heart-saver.
      ├── heart_nb      .ipynb file containing the notebook used for the gbc.pkl file  
  ├── templates/        Contains the HTML files for web app.
      ├── index.html    Homepage for the web app.
      ├── result.html   Result page for the predictions.    
  ├── app.py            Contains the flask API.
  ├── gbc.pkl           Contains the pickled file for app.py.
  ├── Procfile          Contains the information for deployment.
  ├── requirements.txt  Contains the modules and their versions required to setup the web app.
```
# Datasets and Notebooks

- `heart-saver.csv` is the dataset used for the notebook `heat_nb.ipynb`
- `gbc.pkl` is the pickled file made from `heart_nb.ipynb`

## Getting started


### Prerequisites

#### Software Needed
 
  1. A web browser. 

  2. A standard code-editor (VS Code, Sublime Text, Spyder, Pycharm).
         
  3. Anaconda software/ Google Colab/ Kaggle notebook.

#### Knowledge Needed
- Very basic understanding of git and github:

    1.  What are repositories (local - remote - upstream), issues, pull requests.
    2.   How to clone a repository, how to fork a repository, how to set upstreams.
    3.   Adding, committing, pulling, pushing changes to remote repositories.

- For Visualisation and models implementation:
 
    1. Basic syntax and working of ```python```.(This is a must)
    2. Basic knowledge of ```pandas``` library. [Reading this blog might help.](https://www.dataquest.io/blog/pandas-python-tutorial/)
    3. Basic knowledge of ```matplotlib``` library. [Reading this blog might help.](https://blog.quantinsti.com/python-matplotlib-tutorial/)
    4. Basic knowledge of ```seaborn``` library. [Reading this blog might help.](https://www.mygreatlearning.com/blog/seaborn-tutorial/)
    5. Basic knowledge of ```scikit learn``` library. [Reading this blog might help.](https://www.dataquest.io/blog/sci-kit-learn-tutorial/)
    6. Knowledge of various ML models such as Logistic Regression, Naive Bayes, Extreme Gradient Boost, etc. and use of Flask.

- For the web app
    1. HTML
    2. CSS   

  However the code is well explained, so anyone knowing the basics of Python can get a idea of what's happening and contribute to this.

### Installing

There are two ways of running the code.
  1. Running the code on web browser.(Google Colab) [Recommended]
      - Head on to [Google colab](https://colab.research.google.com/notebooks/intro.ipynb)
      - Then click on ```Upload Notebook``` Tab.
      - Upload the notebook that you got from this repo.
        ![Imgur](https://i.imgur.com/a4zM1GW.png)

      - Connect with the runtime, wait for a while. You will see the RAM and Disk info just below.
        ![Imgur](https://i.imgur.com/YYbpnMv.png)

      - Upload your dataset.
        ![Imgur](https://i.imgur.com/YpgxLfE.png)

      - Then Click on ```Run All```.
        ![Imgur](https://i.imgur.com/sr8FHWB.png)

      - Start Editing.

  2. You can also run the code locally in your computer by installing Anaconda.
      - Install Anaconda. [Follow these steps to install Anaconda on your computer](https://www.edureka.co/blog/python-anaconda-tutorial/#:~:text=on%20our%20systems.-,Installation%20And%20Setup,the%20instructions%20in%20the%20setup.)
      - Install jupyter notebook using ```conda```. [Follow these steps to install jupyter notebook.](https://test-jupyter.readthedocs.io/en/latest/install.html)
      - Make sure to install ```pandas```, ```matplotlib```, ```seaborn``` and ```scikit-learn``` to run the notebook.
      - Start Editing.

  3. For the web app
      - You can use any standard editor to edit the app.py file.
      - Make sure to install all the necessary modules and check their versions from `requirements.txt`.
## Live demo

Here is the web app for heart-saver.<br>
https://heart-saver.herokuapp.com/

- Homepage: Contains the necessary boxes to fill the details as mentioned in [Attribute Information](#Attribute-Information).
  ![Imgur](https://i.imgur.com/lVnUUhI.png)
- Click on **Submit** button.
- See the results/predictions.
  ![Imgur](https://i.imgur.com/MEpdhtM.png)

### Attribute Information
1. age (in years)
2. sex (male=1, female=0)
3. chest pain type (4 values)
4. resting blood pressure
5. serum cholestoral in mg/dl
6. fasting blood sugar > 120 mg/dl
7. resting electrocardiographic results (values 0,1,2)
8. maximum heart rate achieved
9. exercise induced angina
10. oldpeak = ST depression induced by exercise relative to rest
11. the slope of the peak exercise ST segment
12. number of major vessels (0-3) colored by flourosopy
13. thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
14. target: 0= less chance of heart attack 1= more chance of heart attack


## Contributing

### IMPORTANT
Make sure you first **fork the repo** and then **clone** it.

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. 
Any contributions you make are **greatly appreciated**. 
Contributing is also a great way to learn more about social coding on Github, new technologies and and their ecosystems and how to make constructive, helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.

### Guidelines

- Before starting to work on any issue or feature, open an issue explaining the changes you want to make and wait for any of the project maintainers to assign it to you.
- Once the issue has been assigned, we'd recommend you creating a new branch with name `issue-xx` where xx is the issue number that you were assigned to.
- Use better commit messages that explain the changes you make. View the example below:
    - Bad commit message: `updated readme`
    - Good commit message: `updated contributors list in readme`
- You **should not**, in any case, use resources or code snippets from sources that do not allow their public use.

## Authors

<a href="https://github.com/DSCKGEC/heart-saver/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DSCKGEC/heart-saver" />
</a>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

