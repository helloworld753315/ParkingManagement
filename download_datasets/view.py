import fiftyone as fo
import fiftyone.zoo as foz

def main():
    dataset = foz.load_zoo_dataset(
       "open-images-v6",
       split="validation",
       label_types=["detections"],
       classes=["Car"],
       max_samples=400,
       only_matching=True,
    )
    session = fo.launch_app(dataset, port=80)
    session.wait()

if __name__ == "__main__":
    main()