# EFES - Easier and Fast Experiment Setup for ML

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) 

*Authors: Chan Park*

Machine Learning Research consists of 3 main parts: "Prepare data", "Construct models", 
and "Run experiments". \
This project suggests guidelines for easier & faster Machine Learning Experiment Setup
using [PyTorch](https://pytorch.org/), [MLflow](https://mlflow.org/).

## Installation

Use the package manager [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) to install basic environments

```bash
# Clone this github repository
git clone https://~~~
cd ~~~
conda env create -f environment.yml
conda activate efes
```

## Guidelines

> Part 1 : Prepare Data

When you write some codes to handle data, you can realize that this part of programming
is highly dependent on **the form of the data** or **the purpose of the research**.

- [ ] 풀 문제를 정해라

- [ ] 사용할 데이터셋을 정해라

- [ ] `Dataset`, `DataLoader`를 정의

> Part 2 : Construct Models

- [ ] 사용할 model 클래스 정의

- [ ] loss, optimizer 정의

- [ ] train logic 정의

- [ ] params, metrics 정의

> Part 3 : Run Experiments

- [ ] 



<!-- 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/) -->