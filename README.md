# Software-Requirement-Engineering-using-Machine-Learning-Techniques

## Project Overview

classification of software requirements using the PROMISE_exp dataset

---
## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Model Architectures](#model-architectures)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

--- 

## Dataset
The [PROMISE Software Engineering Repository](https://promisedata.org/2019/index.html) dataset, created by Jane Cleland-Huang in 2007, is publicly available to foster the development and improvement of predictive models in software engineering. It encourages the replication, verification, and enhancement of research results. Distributed under the Creative Commons Attribution-Share Alike 3.0 License, this dataset allows users to share, adapt, and build upon the data while ensuring proper attribution and maintaining the same licensing conditions for derivative works. This open-access approach supports research transparency and collaboration within the software engineering community.


 > The site was visited on December 14, 2019 http://ctp.di.fct.unl.pt/RE2017/pages/submission/data_papers/

The main interest of this study is to identify [Quality Attributes](http://ctp.di.fct.unl.pt/RE2017//downloads/datasets/nfr.arff), so the Quality Attributes database belonging to TeraPROMISE is used and the use of SecReq, which only involves security attributes, is left up for discussion.

you can find datset as nfr.csv and nfr.arff in this [link](https://github.com/Manolomon/tera-promise) 


data example:
```
1,'The system shall refresh the display every 60 seconds.',PE
4,'All screens created as part of the Disputes application must comply with corporate standards for interface creation.',LF
```


| Categoría | Amount | percentage | Size |
| - | -: | -: | -: |
| Funcional (F) | 255 | 40.80% | 20 |
| Avalilability (A) | 21 | 3.36% | 19 |
| Faul Tolerance (FT) | 10 | 1.60% | 19 |
| Legal (L) | 13 | 2.08% | 18 |
| Look & Feel (LF) | 38 | 6.08% | 20 |
| Mantainabilty (MN) | 17 | 2.72% | 28 |
| Operational (O) | 62 | 9.92% | 20 |
| Performance (PE) | 54 | 8.64% | 22 |
| Portability (PO) | 1 | 0.16% | 14 |
| Scalability (SC) | 21 | 3.36% | 18 |
| Security (SE) | 66 | 10.56% | 20 |
| Usability (US) | 67 | 10.72% | 22 |
| **Total** | **625** | **100%** |  |
---

## Model Architectures

---

## Usage
You can [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NimaMeghdadi/Software-Requirement-Engineering-using-Machine-Learning-Techniques/).

---

## Results

---
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.