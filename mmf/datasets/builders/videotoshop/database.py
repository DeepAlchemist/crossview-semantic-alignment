

# Last Change:  2024-05-08 06:39:48
from typing import Dict, List, Optional, Tuple

import json
from tqdm import tqdm
import torch
from mmf.utils.file_io import PathManager


class VideoToShopDatabase(torch.utils.data.Dataset):
    SPLITS = {"train": ["train"], "val": ["val"], "test": ["test"]}

    def __init__(self, config, splits_path, dataset_type, *args, **kwargs):
        super().__init__()
        self.config = config
        self.dataset_type = dataset_type
        self.splits = self.SPLITS[self.dataset_type]

        if self.dataset_type in ['train', 'val']:
            self.data = self._load_annotation_db(splits_path, config.debug)
        elif self.dataset_type == "test":
            if "gallery" in splits_path:
                self.data = self._load_annotation_db_gallery(splits_path)
            else:
                assert "query" in splits_path
                self.data = self._load_annotation_db_query(splits_path)
        else:
            raise NotImplementedError

    @staticmethod
    def _load_annotation_db(splits_path: str, debug: bool = False):
        data = []

        #with PathManager.open(splits_path, "r") as f:
        #    annotations_json = json.load(f)
        _cnt = -1
        annotations_txt = open(splits_path)
        for _item in tqdm(annotations_txt, desc=f"parsing annotations"):
            _cnt += 1
            # Fetch a few samples for debugging
            if debug and _cnt == 10000: break
            item = _item.strip().split("\t")
            video_id = item[0]
            frame_path_lst = eval(item[1])
            image_id = item[3]
            image_path = item[4]
            image_title = item[5]
            category_id = item[6]
            category_name = item[7]
            spu_id = item[8]
            video_asr = item[9]

            data.append(
                {
                    "video_id": video_id,
                    "video_path": frame_path_lst,
                    "image_id": image_id,
                    "image_path": image_path,
                    "sentences": "video to image retrieval",
                    "image_title": image_title,
                    "attributes_id": None,
                    "category_id": category_id,
                    "subcategory_id": spu_id,
                }
            )

        if len(data) == 0:
            raise RuntimeError("Dataset is empty")

        return data
    
    @staticmethod
    def _load_annotation_db_query(splits_path: str):
        data = []

        with PathManager.open(splits_path, "r") as f:
            annotations_json = json.load(f)
 
        for video_id, _item in tqdm(annotations_json.items(), desc=f"parsing query annotations"):
            live_id = '-'.join(video_id.split("-")[:5])
            frame_path_lst = _item["frames"]
            gt = _item["gt"]

            data.append(
                {
                    "testset_type": "query",
                    "live_id": live_id,
                    "video_id": video_id,
                    "video_path": frame_path_lst,
                    "image_id": video_id,  # Fake ID
                    "image_path": frame_path_lst[0],  # Fake path for code adaptation
                    "sentences": "video to image retrieval",
                }
            )

        if len(data) == 0:
            raise RuntimeError("Dataset is empty")

        return data

   
    @staticmethod
    def _load_annotation_db_gallery(splits_path: str):
        data = []

        annotations_txt = open(splits_path)
        for _item in tqdm(annotations_txt, desc=f"parsing gallery annotations"):
            image_path = _item.strip()
            live_id, image_name = image_path.split("/")

            image_id = "-".join(image_name.split("-")[:5])

            data.append(
                {
                    "testset_type": "gallery",
                    "live_id": live_id,
                    "video_id": image_id,  # NOTE: Fake
                    "video_path": [image_path],  # NOTE: Fake
                    "image_id": image_id,
                    "image_path": image_path,
                    "sentences": "video to image retrieval",
                }
            )

        if len(data) == 0:
            raise RuntimeError("Dataset is empty")

        return data


    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
