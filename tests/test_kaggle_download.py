import os
import kagglehub


path = kagglehub.dataset_download(
    "kishorkhengare/cement-sales-demand",
    force_download=True
)


print(path)


for root, dirs, files in os.walk(path):

    print("ROOT:", root)

    print("FILES:", files)
