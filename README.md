# crossview-semantic-alignment

The official code of ICCV 2023 paper
[Cross-view Semantic Alignment for Livestreaming Product Recognition](https://openaccess.thecvf.com/content/ICCV2023/html/Yang_Cross-view_Semantic_Alignment_for_Livestreaming_Product_Recognition_ICCV_2023_paper.html)
<p align="center">
  <img width="800" height="500" src="./images/model.png">
</p>

## 1.Requirements

## 2.Preparing data

## 3.Evaluation

| |    | CUHK-SYSU  |  | PRW |
| ---- |  :----:  | :----:  | :----:  | :----:  |
| Method |  mAP   | rank1  | mAP   | rank1  |
| OIM [1] | [88.1](https://drive.google.com/file/d/1Im4o0d7hytno-aycSDPHgNkxnJN785v0/view?usp=sharing)  | 89.2 | [36.0](https://drive.google.com/file/d/1l7eKIwOYJxEopguMk_tl8bKQW0f83PJv/view?usp=sharing) | 76.7 |
| NAE [4] | [89.8](https://drive.google.com/file/d/1mCCEnvwQC8Ckn7ElIJFMGqvfZMD6MX1P/view?usp=sharing)  | 90.7 | [37.9](https://drive.google.com/file/d/1zUGlmIoScRR_qFhDGdl8jtmR9cy3YrBF/view?usp=sharing) | 77.3 |
| baseline | [90.0](https://drive.google.com/file/d/17ViFt0rFNXupSNri1DvEhSFpebtqa4Xl/view?usp=sharing) | 91.0 | [40.5](https://drive.google.com/file/d/1H3f2C5GplCxxsxtKgdtdzRsX9mincwC8/view?usp=sharing) | 81.3 |


<table>
    <thead>
        <tr>
            <th colspan=3></th>
            <th colspan=2>LPR4m</th>
            <th colspan=2>MovingFashion</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ICL</td>
            <td>PMD</td>
            <td>PFR</td>
            <td>R1</td>
            <td>ckpt</td>
            <td>R1</td>
            <td>ckpt</td>
        </tr>
        <tr>
          <td>&#10004</td>
          <td></td>
          <td></td>
          <td>22.63</td>
          <td><a href="https://drive.google.com/file/d/1DKJRDzsYAih_LBe2eTaeIF8hK3-J6rnU/view?usp=drive_link">URL</a></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>&#10004</td>
          <td>&#10004</td>
          <td></td>
          <td>25.99</td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>&#10004</td>
          <td>&#10004</td>
          <td>&#10004</td>
          <td>27.17</td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
    </tbody>
</table>

## 4.Training

## 5.Citation

```bibtex
@InProceedings{Yang_2023_ICCV,
    author    = {Yang, Wenjie and Chen, Yiyi and Li, Yan and Cheng, Yanhua and Liu, Xudong and Chen, Quan and Li, Han},
    title     = {Cross-view Semantic Alignment for Livestreaming Product Recognition},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2023},
    pages     = {13404-13413}
}
``` 
