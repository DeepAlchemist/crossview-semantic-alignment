<div align="center">

# Cross-view Semantic Alignment for Livestreaming Product Recognition

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
[![Conference](https://img.shields.io/badge/ICCV-2023-6790AC.svg)](https://iccv2023.thecvf.com/)
[![Paper](http://img.shields.io/badge/Paper-arxiv.2308.04912-B31B1B.svg)](https://arxiv.org/pdf/2308.04912.pdf)

</div>

The official code of ICCV 2023 paper
[Cross-view Semantic Alignment for Livestreaming Product Recognition](https://openaccess.thecvf.com/content/ICCV2023/html/Yang_Cross-view_Semantic_Alignment_for_Livestreaming_Product_Recognition_ICCV_2023_paper.html)

This work makes two contributions: :grin: (1) collecting a large-scale and diverse dataset for the video-to-shop task, which aims to match products (i.e., clothes) in videos to online shopping images. :grin: (2) proposing a novel pre-training framework to exploit the specialties of e-commerce data.

In the original paper, we reported the performance of the model trained on the complete dataset of 4 million samples using 8 V100 GPUs. However, we had concerns about the accessibility of the dataset and the reproducibility of the model performances. The reasons are as follows: :warning: (1) the large size of 4 million samples makes the data difficult to download (time-consuming and error-prone) and requires large storage space (4 TB). :warning: (2) using 8 V100 GPUs sets high resource requirements for model training. Considering these factors, we made the following adjustments in this repository: :grin: (1) we reduced the number of training samples. We sampled a training subset containing ***750K*** samples from the full 4 million samples, which only reduced the number of samples of the head categories without sampling the tail categories. :grin: (2) we used the more widely available ***RTX 3090 GPU*** instead of ***V100 GPU*** to train the model, facilitating the reproduction of model results.

## Architecture
<p align="center">
  <img width="600" height="400" src="./images/model.png">
</p>

## Requirements
+ python=3.7.16
+ pytorch=1.12.1
+ torchvision=0.13.1
+ numpy=1.21.6
+ scikit-learn=1.0.2
+ ffmpeg=4.3
  
Other requirements please refer to ***requirements.txt***. You can also create conda env by
```bash
conda env create --file=requirements.txt
```

## Data Preparation
### Prepare LPR750K
Download the sampled 750k samples of LPR4M dataset.
```bash
bash scripts/download_lpr750k.sh
```
The LPR750K dataset takes about 370GB.
```bash
|--lpr750k
    |--annotations
    |    |--training_videoinfo_750k.txt
    |    |--test_videoid_to_gtimage_20079.json
    |    |--...
    |--query
    |    |--query_video_1
    |    |--query_video_2
    |    |--...
    |--gallery
    |    |--livestreaming_id_1
    |    |    |--gallery_image_1
    |    |    |--gallery_image_2
    |    |    |--...
    |    |--livestreaming_id_2
    |    |    |--gallery_image_k
    |    |    |--gallery_image_m
    |    |    |--...
    |    |--...
    |--training_image
    |--training_video_00
    |--training_video_01
    |--...
    |--training_video_07
```

### Prepare MovingFashion
The dataset can be downloaded from the [official code repository](https://github.com/HumaticsLAB/SEAM-Match-RCNN) (takes about 24GB)

```bash
|--movingfashion
    |--videos
    |    |--xxx.mp4
    |    |--xxx.mp4
    |    |--...
    |--imgs
    |    |--xxx.jpg
    |    |--xxx.jpg
    |    |--...
    |--test.json
    |--train.json
```
Then run the following script to prepare movingfashion dataset.
```bash
python prepare_movingfashion.py --data_root /path/to/movingfashion/dataset/
```

## Evaluation
:star2: We perform ablation study on LPR4M and compare the proposed method with SOTA on LPR4M and MovingFashion (the results on WAB dataset is coming soon).

### Ablation study 
<table align="center">
    <thead>
        <tr>
            <th colspan=3></th>
            <th colspan=2>LPR4M</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ICL</td>
            <td>PMD</td>
            <td>PFR</td>
            <td>R1</td>
            <td>ckpt</td>
        </tr>
        <tr>
          <td>&#10004</td>
          <td></td>
          <td></td>
          <td>22.63</td>
          <td><a href="https://drive.google.com/file/d/1DKJRDzsYAih_LBe2eTaeIF8hK3-J6rnU/view?usp=drive_link">Google Drive</a></td>
        </tr>
        <tr>
          <td>&#10004</td>
          <td>&#10004</td>
          <td></td>
          <td>25.99</td>
          <td><a href="https://drive.google.com/file/d/1X-cNDd8k-0NItx9-8CDqPclaxLQJlk6h/view?usp=drive_link">Google Drive</a></td>
        </tr>
        <tr>
          <td>&#10004</td>
          <td>&#10004</td>
          <td>&#10004</td>
          <td>27.17</td>
          <td><a href="https://drive.google.com/file/d/12Mu1QuVjLs2GbU2e7NcsHMzQJqWMMOmf/view?usp=drive_link">Google Drive</a></td>
        </tr>
    </tbody>
</table>
 
:star2: We train the model using 2 x RTX 3090 GPUs with 24GB of memory each and a global batch size of 96. For the rest of the configuration, please refer to the training script in  `./scripts`. Note that, On LPR4M, this project uses 750K training samples and a batch size of 96, while the original paper used 4 million training samples and a batch size of 256, thus the performance reported in this project is lower than that in the paper. However, as a baseline model for the proposed dataset, the performance level is not a key factor and does not affect readers from following this work.

Evaluating ICL on LPR4M
```bash
python lpr4m_embedding_eval.py --data_root /lpr4m/data/root/ --n_gpu 2 --sim_header mean_pooling  --one_stage --embedding_sim --ckpt_path /checkpoint/path
```

Evaluating ICL+PMD on LPR4M
```bash
python lpr4m_embedding_eval.py --data_root /lpr4m/data/root/ --n_gpu 2 --sim_header cross_attention --cross_num_hidden_layers 2 --embedding_sim --ckpt_path /checkpoint/path
```

Evaluating ICL+PMD+PFR on LPR4M
```bash
python lpr4m_embedding_eval.py --data_root /lpr4m/data/root/ --n_gpu 2 --sim_header cross_attention --cross_num_hidden_layers 2 --recons_feat --embedding_sim --ckpt_path /checkpoint/path
```
The evaluation script for each model on MovingFashion is similar to that for LPR4M, i.e.,
```bash
python movingfashion_eval.py ...
```

### Comparing with SOTA
<table align="center">
    <thead>
        <tr>
            <th rowspan=2></th>
            <th colspan=4>LPR4M</th>
            <th colspan=4>MovingFashion</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td>R1</td>
            <td>R5</td>
            <td>R10</td>
            <td>ckpt</td>
            <td>R1</td>
            <td>R5</td>
            <td>R10</td>
            <td>ckpt</td>
        </tr>
        <tr>
          <td>FashionNet</td>
          <td></td>
          <td></td>
          <td></td>
          <td><a href="">URL</a></td>
          <td></td>
          <td></td>
          <td></td>
          <td><a href="">URL</a></td>
        </tr>
        <tr>
          <td>TimeSFormer</td>
          <td></td>
          <td></td>
          <td></td>
          <td><a href="">URL</a></td>
          <td></td>
          <td></td>
          <td></td>
          <td><a href="">URL</a></td>
        </tr>
        <tr>
          <td>Swin-B</td>
          <td></td>
          <td></td>
          <td></td>
          <td><a href="">URL</a></td>
          <td></td>
          <td></td>
          <td></td>
          <td><a href="">URL</a></td>
        </tr>
        <tr>
          <td>RICE</td>
          <td></td>
          <td></td>
          <td></td>
          <td><a href="">URL</a></td>
          <td></td>
          <td></td>
          <td></td>
          <td><a href="">URL</a></td>
        </tr>
    </tbody>
</table>

## Training

Training ICL on LPR750K
```bash
bash scripts/training_icl.sh
```
Training ICL+PMD on LPR750K
```bash
bash scripts/training_icl_pmd.sh
```
Training ICL+PMD+PFR on LPR750K
```bash
bash scripts/training_icl_pmd_pfr.sh
```
If you want to train on MovingFashion, simply set the values of `--dataset` and `--data_root` to point to MovingFashion. 
For example,
```bash
--dataset movingfashion --data_root /path/to/movingfashion/data/ --output_dir /output/root/to/save/the/checkpoint
```
If you want to train other models, such as the Swin-B, please specify the value of `--model_name`.

## Citation

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
