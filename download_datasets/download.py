import fiftyone.zoo as foz
import fiftyone as fo

def main():
    dataset = foz.load_zoo_dataset(
       "open-images-v6",
       split="validation",
       label_types=["detections"],
       classes=["Car"],
       max_samples=400,
       only_matching=True,
    )
    # 名前を付けて
    dataset.name = "open-images-v6-car-04201305"
    # 永続化する
    dataset.persistent = True

    classes = ["Car"]

    train_dataset = dataset[:700]
    val_dataset = dataset[700:800]
    test_dataset = dataset[800:]

    # YOLO V5 形式でエクスポート
    train_dataset.export(
        export_dir=f"~/content/data/train",
        dataset_type=fo.types.YOLOv5Dataset,
        split="train",
        classes=classes,
    )
    val_dataset.export(
        export_dir=f"~/content/data/val",
        dataset_type=fo.types.YOLOv5Dataset,
        split="val",
        classes=classes,
    )
    test_dataset.export(
        export_dir=f"~/content/data/test",
        dataset_type=fo.types.YOLOv5Dataset,
        split="test",
        classes=classes,
    )

if __name__ == "__main__":
    main()