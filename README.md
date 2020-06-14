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
git clone https://github.com/coldpak/efes.git
cd efes

# Set Python environment using conda
conda env create -f environment.yml
conda activate efes
```

## Guidelines

아래의 가이드라인을 따라가면서 root directory에 `env` 파일을 만들고 python 클래스 및 함수들을 정의하자.

> Part 1 : Prepare Data

When you write some codes to handle data, you can realize that this part of programming
is highly dependent on **the form of the data** or **the purpose of the research**.

- [ ] 풀 문제를 정해라

- [ ] 사용할 데이터셋을 정해라

- [ ] data location 정해라 -> uri 정보를 env에 입력

- [ ] data_loader.py에 `Dataset`, `DataLoader`을 응용해 커스텀 클래스들을 정의하라

> Part 2 : Construct Models

- [ ] model/ 내부에 사용할 model 클래스 정의

- [ ] loss, optimizer 정의

- [ ] train logic 정의

- [ ] params, metrics 정의

> Part 3 : Run Experiments

- [ ] MLflow 서버 열기, 아이디 비번 만들어서 env에 입력

- [ ] 실험 아이디, metric 등을 env에 입력



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